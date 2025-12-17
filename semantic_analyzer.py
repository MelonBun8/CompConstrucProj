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
    
    # ... handle other expressions similarly
