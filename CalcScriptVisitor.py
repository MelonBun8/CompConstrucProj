# Generated from CalcScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalcScriptParser import CalcScriptParser
else:
    from CalcScriptParser import CalcScriptParser

# This class defines a complete generic visitor for a parse tree produced by CalcScriptParser.

class CalcScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcScriptParser#prog.
    def visitProg(self, ctx:CalcScriptParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#funcDecl.
    def visitFuncDecl(self, ctx:CalcScriptParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#paramList.
    def visitParamList(self, ctx:CalcScriptParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#param.
    def visitParam(self, ctx:CalcScriptParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#VarDeclStat.
    def visitVarDeclStat(self, ctx:CalcScriptParser.VarDeclStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#AssignStat.
    def visitAssignStat(self, ctx:CalcScriptParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#PrintStat.
    def visitPrintStat(self, ctx:CalcScriptParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#IfStat.
    def visitIfStat(self, ctx:CalcScriptParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#WhileStat.
    def visitWhileStat(self, ctx:CalcScriptParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#ReturnStat.
    def visitReturnStat(self, ctx:CalcScriptParser.ReturnStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#ExprStat.
    def visitExprStat(self, ctx:CalcScriptParser.ExprStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#BlockStat.
    def visitBlockStat(self, ctx:CalcScriptParser.BlockStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#varDecl.
    def visitVarDecl(self, ctx:CalcScriptParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#assignment.
    def visitAssignment(self, ctx:CalcScriptParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#returnStmt.
    def visitReturnStmt(self, ctx:CalcScriptParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#printStmt.
    def visitPrintStmt(self, ctx:CalcScriptParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#ifStmt.
    def visitIfStmt(self, ctx:CalcScriptParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#whileStmt.
    def visitWhileStmt(self, ctx:CalcScriptParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#block.
    def visitBlock(self, ctx:CalcScriptParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#PowerExpr.
    def visitPowerExpr(self, ctx:CalcScriptParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#FloatExpr.
    def visitFloatExpr(self, ctx:CalcScriptParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:CalcScriptParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#EqualityExpr.
    def visitEqualityExpr(self, ctx:CalcScriptParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#IdExpr.
    def visitIdExpr(self, ctx:CalcScriptParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#FunCallExpr.
    def visitFunCallExpr(self, ctx:CalcScriptParser.FunCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#IntExpr.
    def visitIntExpr(self, ctx:CalcScriptParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#RelationalExpr.
    def visitRelationalExpr(self, ctx:CalcScriptParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#ParenExpr.
    def visitParenExpr(self, ctx:CalcScriptParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:CalcScriptParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#argList.
    def visitArgList(self, ctx:CalcScriptParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcScriptParser#type.
    def visitType(self, ctx:CalcScriptParser.TypeContext):
        return self.visitChildren(ctx)



del CalcScriptParser