# Generated from CalcScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalcScriptParser import CalcScriptParser
else:
    from CalcScriptParser import CalcScriptParser

# This class defines a complete listener for a parse tree produced by CalcScriptParser.
class CalcScriptListener(ParseTreeListener):

    # Enter a parse tree produced by CalcScriptParser#prog.
    def enterProg(self, ctx:CalcScriptParser.ProgContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#prog.
    def exitProg(self, ctx:CalcScriptParser.ProgContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#AssignStat.
    def enterAssignStat(self, ctx:CalcScriptParser.AssignStatContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#AssignStat.
    def exitAssignStat(self, ctx:CalcScriptParser.AssignStatContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#PrintStat.
    def enterPrintStat(self, ctx:CalcScriptParser.PrintStatContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#PrintStat.
    def exitPrintStat(self, ctx:CalcScriptParser.PrintStatContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#IfStat.
    def enterIfStat(self, ctx:CalcScriptParser.IfStatContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#IfStat.
    def exitIfStat(self, ctx:CalcScriptParser.IfStatContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#WhileStat.
    def enterWhileStat(self, ctx:CalcScriptParser.WhileStatContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#WhileStat.
    def exitWhileStat(self, ctx:CalcScriptParser.WhileStatContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#BlockStat.
    def enterBlockStat(self, ctx:CalcScriptParser.BlockStatContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#BlockStat.
    def exitBlockStat(self, ctx:CalcScriptParser.BlockStatContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#assignment.
    def enterAssignment(self, ctx:CalcScriptParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#assignment.
    def exitAssignment(self, ctx:CalcScriptParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#printStmt.
    def enterPrintStmt(self, ctx:CalcScriptParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#printStmt.
    def exitPrintStmt(self, ctx:CalcScriptParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#ifStmt.
    def enterIfStmt(self, ctx:CalcScriptParser.IfStmtContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#ifStmt.
    def exitIfStmt(self, ctx:CalcScriptParser.IfStmtContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#whileStmt.
    def enterWhileStmt(self, ctx:CalcScriptParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#whileStmt.
    def exitWhileStmt(self, ctx:CalcScriptParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#block.
    def enterBlock(self, ctx:CalcScriptParser.BlockContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#block.
    def exitBlock(self, ctx:CalcScriptParser.BlockContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#PowerExpr.
    def enterPowerExpr(self, ctx:CalcScriptParser.PowerExprContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#PowerExpr.
    def exitPowerExpr(self, ctx:CalcScriptParser.PowerExprContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#FloatExpr.
    def enterFloatExpr(self, ctx:CalcScriptParser.FloatExprContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#FloatExpr.
    def exitFloatExpr(self, ctx:CalcScriptParser.FloatExprContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:CalcScriptParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:CalcScriptParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#EqualityExpr.
    def enterEqualityExpr(self, ctx:CalcScriptParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#EqualityExpr.
    def exitEqualityExpr(self, ctx:CalcScriptParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#IdExpr.
    def enterIdExpr(self, ctx:CalcScriptParser.IdExprContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#IdExpr.
    def exitIdExpr(self, ctx:CalcScriptParser.IdExprContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#IntExpr.
    def enterIntExpr(self, ctx:CalcScriptParser.IntExprContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#IntExpr.
    def exitIntExpr(self, ctx:CalcScriptParser.IntExprContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#RelationalExpr.
    def enterRelationalExpr(self, ctx:CalcScriptParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#RelationalExpr.
    def exitRelationalExpr(self, ctx:CalcScriptParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#ParenExpr.
    def enterParenExpr(self, ctx:CalcScriptParser.ParenExprContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#ParenExpr.
    def exitParenExpr(self, ctx:CalcScriptParser.ParenExprContext):
        pass


    # Enter a parse tree produced by CalcScriptParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:CalcScriptParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by CalcScriptParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:CalcScriptParser.AddSubExprContext):
        pass



del CalcScriptParser