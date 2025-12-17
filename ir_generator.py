# Phase 4: Intermediate Code Generation - Three-Address Code
from CalcScriptVisitor import CalcScriptVisitor

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

    def visitAssignment(self, ctx):
        result = ctx.ID().getText()
        expr_result = self.visit(ctx.expr())
        self.emit('=', expr_result, None, result)

    def visitPrintStat(self, ctx):
        result = self.visit(ctx.printStmt().expr())
        self.emit('PRINT', result, None, None)

    def visitIntExpr(self, ctx):
        return ctx.INT().getText()

    def visitFloatExpr(self, ctx):
        return ctx.FLOAT().getText()

    def visitIdExpr(self, ctx):
        return ctx.ID().getText()

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
        expr = self.visit(if_stmt.expr())
        label_else = self.new_label()
        label_end = self.new_label()

        self.emit('IF_FALSE', expr, None, label_else) # Jump to else if expr is false
        self.visit(if_stmt.stat(0)) # Then block
        self.emit('GOTO', None, None, label_end)
        
        self.emit('LABEL', None, None, label_else)
        if if_stmt.stat(1): # Check if else block exists
            self.visit(if_stmt.stat(1))
        
        self.emit('LABEL', None, None, label_end)

    def visitWhileStat(self, ctx):
        while_stmt = ctx.whileStmt()
        label_start = self.new_label()
        label_end = self.new_label()

        self.emit('LABEL', None, None, label_start)
        expr = self.visit(while_stmt.expr())
        self.emit('IF_FALSE', expr, None, label_end)
        
        self.visit(while_stmt.stat())
        self.emit('GOTO', None, None, label_start)
        self.emit('LABEL', None, None, label_end)

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
