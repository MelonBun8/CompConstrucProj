# Phase 3: Semantic Analysis - Symbol Table Construction and Type Checking
from CalcScriptVisitor import CalcScriptVisitor
from symbol_table import SymbolTable

class SemanticAnalyzer(CalcScriptVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

    def visitProg(self, ctx):
        self.visitChildren(ctx)
        return self.symbol_table, self.errors

    def visitFuncDecl(self, ctx):
        func_name = ctx.ID().getText()
        
        # Parse params to get signature
        param_types = []
        if ctx.paramList():
            for param in ctx.paramList().param():
                type_node = param.type_()
                param_types.append(type_node.getText())

        # Parse Return Type
        return_type = "void"
        if ctx.type_():
            return_type = ctx.type_().getText()

        # Define Function with Return Type
        self.symbol_table.define(func_name, return_type, "func", param_types) 
        
        self.symbol_table.enter_scope()
        
        # Define Params in Inner Scope
        if ctx.paramList():
            for i, param in enumerate(ctx.paramList().param()):
                p_name = param.ID().getText()
                p_type = param_types[i]
                self.symbol_table.define(p_name, p_type, "param")
                
        self.visit(ctx.block())
        self.symbol_table.exit_scope()

    def visitBlockStat(self, ctx):
        self.symbol_table.enter_scope()
        self.visitChildren(ctx)
        self.symbol_table.exit_scope()

    def visitVarDeclStat(self, ctx):
        self.visit(ctx.varDecl())
        
    def visitVarDecl(self, ctx):
        type_name = ctx.type_().getText()
        var_name = ctx.ID().getText()
        expr_type = self.visit(ctx.expr())
        
        if expr_type != type_name and expr_type != "unknown":
            # Simple coercion check or strict
            if type_name == "float" and expr_type == "int":
                pass # Safe
            else:
                 self.errors.append(f"Type Mismatch: Cannot assign {expr_type} to {type_name} '{var_name}'")
        
        self.symbol_table.define(var_name, type_name, "var")

    def visitAssignStat(self, ctx):
        return self.visit(ctx.assignment())

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        expr_type = self.visit(ctx.expr())
        
        symbol = self.symbol_table.resolve(var_name)
        if not symbol:
             self.errors.append(f"Error: Variable '{var_name}' not declared.")
        else:
            if symbol.type != expr_type and symbol.type != "unknown":
                 if symbol.type == "float" and expr_type == "int":
                     pass 
                 else:
                     self.errors.append(f"Type Mismatch: Cannot assign {expr_type} to {symbol.type} '{var_name}'")
        
        # We don't define here anymore, we only assign. 
        # If implicit declaration is allowed, we'd do it, but User wanted "Undeclared variable" check (Chart 11).
        # So we enforce prior declaration (via varDecl or function arg).

    def visitIdExpr(self, ctx):
        var_name = ctx.ID().getText()
        symbol = self.symbol_table.resolve(var_name)
        if not symbol:
            self.errors.append(f"Error: Variable '{var_name}' not declared.")
            return "unknown"
        return symbol.type

    def visitIntExpr(self, ctx):
        return "int"

    def visitFloatExpr(self, ctx):
        return "float"

    def visitAddSubExpr(self, ctx):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        if left_type == "float" or right_type == "float":
            return "float"
        return "int"

    def visitMulDivExpr(self, ctx):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        # Division often implies float
        if ctx.getChild(1).getText() == '/':
            return "float"
        if left_type == "float" or right_type == "float":
            return "float"
        return "int"
    
    def visitPowerExpr(self, ctx):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        # Power usually returns float or int depending on implementation, 
        # but for type checking we ensure operands are numbers
        if left_type not in ["int", "float"] or right_type not in ["int", "float"]:
             self.errors.append("Error: Power operator requires numeric operands.")
        return "float" # Result is typically float

    def visitRelationalExpr(self, ctx):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        if left_type not in ["int", "float"] or right_type not in ["int", "float"]:
            self.errors.append("Error: Relational operators apply to numbers.")
        return "int" # Representing boolean 0/1

    def visitEqualityExpr(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        return "int" # Boolean

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitFunCallExpr(self, ctx):
        func_name = ctx.ID().getText()
        symbol = self.symbol_table.resolve(func_name)
        
        if not symbol or symbol.kind != "func":
            self.errors.append(f"Error: Function '{func_name}' not declared.")
            return "unknown"
            
        # Check Args
        args = []
        if ctx.argList():
            for expr in ctx.argList().expr():
                args.append(self.visit(expr))
                
        if len(args) != len(symbol.params):
             self.errors.append(f"Error: Argument count mismatch for '{func_name}'. Expected {len(symbol.params)}, got {len(args)}.")
        else:
             # Basic type check
             for i, arg_type in enumerate(args):
                 param_type = symbol.params[i]
                 if arg_type != param_type and arg_type != "unknown":
                      if param_type == "float" and arg_type == "int": continue
                      self.errors.append(f"Type Mismatch in arg {i+1} of '{func_name}': expected {param_type}, got {arg_type}")

        return symbol.type # Return type of function

    def visitReturnStat(self, ctx):
        stmt = ctx.returnStmt()
        if stmt.expr():
            return self.visit(stmt.expr())
        return "void"

    def visitIfStat(self, ctx):
        # ctx is IfStatContext, containing ifStmt
        stmt = ctx.ifStmt()
        self.visit(stmt.expr()) # Check condition
        self.visit(stmt.stat(0)) # Then block
        if stmt.stat(1):
            self.visit(stmt.stat(1)) # Else block

    def visitWhileStat(self, ctx):
        # Special While Scope: Condition and Body share the same scope, 
        # but it acts as a "Local" scope so we can shadow global counter.
        self.symbol_table.enter_scope()
        
        stmt = ctx.whileStmt()
        self.visit(stmt.expr()) # Condition check inside the scope
        self.visit(stmt.stat()) # Body check inside the scope
        
        self.symbol_table.exit_scope()

    def visitPrintStat(self, ctx):
        stmt = ctx.printStmt()
        self.visit(stmt.expr())
