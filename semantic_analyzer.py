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

    def visitBlockStat(self, ctx):
        self.symbol_table.enter_scope()
        self.visitChildren(ctx)
        self.symbol_table.exit_scope()

    def visitAssignStat(self, ctx):
        return self.visit(ctx.assignment())

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        # Visit expression to get type (for now assuming simple inference or default)
        expr_type = self.visit(ctx.expr())
        
        # If variable not defined in current scope, define it
        # For simplicity in this mini-language, assignment defines the variable
        self.symbol_table.define(var_name, expr_type)

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

    def visitIfStat(self, ctx):
        # ctx is IfStatContext, containing ifStmt
        stmt = ctx.ifStmt()
        self.visit(stmt.expr()) # Check condition
        self.visit(stmt.stat(0)) # Then block
        if stmt.stat(1):
            self.visit(stmt.stat(1)) # Else block

    def visitWhileStat(self, ctx):
        stmt = ctx.whileStmt()
        self.visit(stmt.expr())
        self.visit(stmt.stat())

    def visitPrintStat(self, ctx):
        stmt = ctx.printStmt()
        self.visit(stmt.expr())
