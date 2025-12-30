# Phase 4: Intermediate Code Generation - Three-Address Code
from CalcScriptVisitor import CalcScriptVisitor
from symbol_table import SymbolTable

class Quadruple:
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __repr__(self):
        return f"({self.op}, {self.arg1}, {self.arg2}, {self.result})"

class IRGenerator(CalcScriptVisitor):
    def __init__(self):
        self.code = []
        self.temp_counter = 0
        self.label_counter = 0
        self.symbol_table = SymbolTable()

    def scan_locals(self, ctx, acc):
        import CalcScriptParser
        
        # 1. Assignment Rule (Goal)
        if isinstance(ctx, CalcScriptParser.CalcScriptParser.AssignmentContext):
            acc.add(ctx.ID().getText())
            return
        
        # 2. Block Wrappers (Recurse children)
        if isinstance(ctx, CalcScriptParser.CalcScriptParser.BlockStatContext) or \
           isinstance(ctx, CalcScriptParser.CalcScriptParser.BlockContext):
            for child in ctx.children:
                self.scan_locals(child, acc)
            return

        # 3. Assign StatementWrapper (Recurse to assignment)
        if isinstance(ctx, CalcScriptParser.CalcScriptParser.AssignStatContext):
            self.scan_locals(ctx.assignment(), acc)
            return
            
        # 4. Other Statements
        return


    def new_temp(self):
        self.temp_counter += 1
        return f"t{self.temp_counter}"

    def new_label(self):
        self.label_counter += 1
        return f"L{self.label_counter}"

    def emit(self, op, arg1, arg2, result):
        self.code.append(Quadruple(op, arg1, arg2, result))

    def visitProg(self, ctx):
        self.visitChildren(ctx)
        return self.code
    
    def visitBlockStat(self, ctx):
        self.symbol_table.enter_scope()
        self.visitChildren(ctx)
        self.symbol_table.exit_scope()

    def visitAssignment(self, ctx):
        original_name = ctx.ID().getText()
        
        # 1. Visit Expression FIRST to resolve variables using current symbols
        expr_result = self.visit(ctx.expr())

        # 2. Define/Redefine variable in current scope
        # This returns the new mangled name for the *result* of this assignment
        mangled_name = self.symbol_table.define(original_name, "unknown")
        
        self.emit('=', expr_result, None, mangled_name)

    def visitPrintStat(self, ctx):
        result = self.visit(ctx.printStmt().expr())
        self.emit('PRINT', result, None, None)

    def visitIntExpr(self, ctx):
        return ctx.INT().getText()

    def visitFloatExpr(self, ctx):
        return ctx.FLOAT().getText()

    def visitIdExpr(self, ctx):
        original_name = ctx.ID().getText()
        symbol = self.symbol_table.resolve(original_name)
        if symbol:
            return symbol.mangled_name
        else:
            # Fallback or error, though Semantic Analyzer should have caught this.
            # We'll validly return the original name just in case, or raise error.
            return original_name

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        temp = self.new_temp()
        op = ctx.getChild(1).getText()
        self.emit(op, left, right, temp)
        return temp
    
    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        temp = self.new_temp()
        op = ctx.getChild(1).getText()
        self.emit(op, left, right, temp)
        return temp

    def visitIfStat(self, ctx):
        # if (expr) stat else stat
        if_stmt = ctx.ifStmt()
        
        # Scoping: The condition is in the outer scope, but the blocks are inner scopes.
        # However, standard practice often puts the *entire* if statement in a scope 
        # or just the blocks. The grammar has 'block' as a statement type which handles its own scope.
        # But single statements (like 'if (...) x=1') might not be blocks.
        # To be safe and consistent with 'BlockStat', we rely on the children being BlockStats 
        # if they have braces. Use enter_scope/exit_scope ONLY if your language spec 
        # mandates a new scope for the *implicit* blocks of an if/else without braces.
        # For this project, assuming {} blocks handle their own scopes via visitBlockStat.
        # But if the user writes 'if (..) x=1;', that x usually shadows?
        # Let's enforce scope for the branches to be safe/robust.
        
        expr = self.visit(if_stmt.expr())
        label_else = self.new_label()
        label_end = self.new_label()

        self.emit('IF_FALSE', expr, None, label_else) # Jump to else if expr is false
        
        # THEN Block Scope
        self.symbol_table.enter_scope()
        self.visit(if_stmt.stat(0)) # Then block
        self.symbol_table.exit_scope()
        
        self.emit('GOTO', None, None, label_end)
        
        self.emit('LABEL', None, None, label_else)
        if if_stmt.stat(1): # Check if else block exists
            # ELSE Block Scope
            self.symbol_table.enter_scope()
            self.visit(if_stmt.stat(1))
            self.symbol_table.exit_scope()
        
        self.emit('LABEL', None, None, label_end)

    def visitWhileStat(self, ctx):
        while_stmt = ctx.whileStmt()
        label_start = self.new_label()
        label_end = self.new_label()

        # Enter While Scope (encloses condition + body)
        self.symbol_table.enter_scope()

        # 0. Variable Hoisting / Copy-on-Entry
        # Scan body for assignments that would shadow globals.
        # Define them locally AND initialize them with the outer value if allowed.
        locals_found = set()
        self.scan_locals(while_stmt.stat(), locals_found)
        
        for name in locals_found:
            # Check if it exists in outer scope
            # resolve() looks in ALL scopes. We want to know if it's in OUTER.
            # We haven't defined it locally yet, so resolve() finds outer.
            outer_symbol = self.symbol_table.resolve(name)
            
            # Define locally (Mutable usage will reuse this)
            local_name = self.symbol_table.define(name, "unknown")
            
            if outer_symbol:
                # Emit Copy: local = outer
                self.emit('=', outer_symbol.mangled_name, None, local_name)
            else:
                # If completely new, initialize to 0? Or leave undefined?
                # Usually undefined.
                pass

        # 1. First Condition Check (Pre-Loop)
        # Now local variables exist (initialized from global).
        expr_pre = self.visit(while_stmt.expr())
        self.emit('IF_FALSE', expr_pre, None, label_end)

        self.emit('LABEL', None, None, label_start)
        
        # 2. Body
        # Visiting the body defines the local variables in the current scope.
        stat = while_stmt.stat()
        import CalcScriptParser
        if isinstance(stat, CalcScriptParser.CalcScriptParser.BlockStatContext):
             # Visit children directly (bypass visitBlockStat) to keep variables in THIS scope
             self.visitChildren(stat)
        else:
             self.visit(stat)

        # 3. Second Condition Check (Post-Loop)
        expr_post = self.visit(while_stmt.expr())
        self.emit('IF_FALSE', expr_post, None, label_end)
        
        self.emit('GOTO', None, None, label_start)
        self.emit('LABEL', None, None, label_end)
        
        self.symbol_table.exit_scope()

    def visitRelationalExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        temp = self.new_temp()
        op = ctx.getChild(1).getText()
        self.emit(op, left, right, temp)
        return temp
    
    def visitEqualityExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        temp = self.new_temp()
        op = ctx.getChild(1).getText()
        self.emit(op, left, right, temp)
        return temp

    def visitPowerExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        temp = self.new_temp()
        self.emit('^', left, right, temp)
        return temp

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())
