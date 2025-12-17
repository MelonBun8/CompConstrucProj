# Generated from CalcScript.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,1,1,1,3,1,24,8,1,1,1,1,1,
        3,1,28,8,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,51,8,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,6,1,6,5,6,61,8,6,10,6,12,6,64,9,6,1,6,1,6,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,3,7,76,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,5,7,93,8,7,10,7,12,7,96,9,7,1,7,0,1,14,8,0,
        2,4,6,8,10,12,14,0,4,1,0,8,9,1,0,10,11,1,0,12,15,1,0,16,17,106,0,
        17,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,38,1,0,0,0,8,43,1,0,0,0,10,
        52,1,0,0,0,12,58,1,0,0,0,14,75,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,
        0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,1,1,0,0,0,21,23,3,
        4,2,0,22,24,5,1,0,0,23,22,1,0,0,0,23,24,1,0,0,0,24,33,1,0,0,0,25,
        27,3,6,3,0,26,28,5,1,0,0,27,26,1,0,0,0,27,28,1,0,0,0,28,33,1,0,0,
        0,29,33,3,8,4,0,30,33,3,10,5,0,31,33,3,12,6,0,32,21,1,0,0,0,32,25,
        1,0,0,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,0,34,
        35,5,22,0,0,35,36,5,2,0,0,36,37,3,14,7,0,37,5,1,0,0,0,38,39,5,21,
        0,0,39,40,5,3,0,0,40,41,3,14,7,0,41,42,5,4,0,0,42,7,1,0,0,0,43,44,
        5,18,0,0,44,45,5,3,0,0,45,46,3,14,7,0,46,47,5,4,0,0,47,50,3,2,1,
        0,48,49,5,19,0,0,49,51,3,2,1,0,50,48,1,0,0,0,50,51,1,0,0,0,51,9,
        1,0,0,0,52,53,5,20,0,0,53,54,5,3,0,0,54,55,3,14,7,0,55,56,5,4,0,
        0,56,57,3,2,1,0,57,11,1,0,0,0,58,62,5,5,0,0,59,61,3,2,1,0,60,59,
        1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,
        64,62,1,0,0,0,65,66,5,6,0,0,66,13,1,0,0,0,67,68,6,7,-1,0,68,76,5,
        22,0,0,69,76,5,23,0,0,70,76,5,24,0,0,71,72,5,3,0,0,72,73,3,14,7,
        0,73,74,5,4,0,0,74,76,1,0,0,0,75,67,1,0,0,0,75,69,1,0,0,0,75,70,
        1,0,0,0,75,71,1,0,0,0,76,94,1,0,0,0,77,78,10,9,0,0,78,79,5,7,0,0,
        79,93,3,14,7,10,80,81,10,8,0,0,81,82,7,0,0,0,82,93,3,14,7,9,83,84,
        10,7,0,0,84,85,7,1,0,0,85,93,3,14,7,8,86,87,10,6,0,0,87,88,7,2,0,
        0,88,93,3,14,7,7,89,90,10,5,0,0,90,91,7,3,0,0,91,93,3,14,7,6,92,
        77,1,0,0,0,92,80,1,0,0,0,92,83,1,0,0,0,92,86,1,0,0,0,92,89,1,0,0,
        0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,15,1,0,0,0,96,94,
        1,0,0,0,9,19,23,27,32,50,62,75,92,94
    ]

class CalcScriptParser ( Parser ):

    grammarFileName = "CalcScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'('", "')'", "'{'", "'}'", 
                     "'^'", "'*'", "'/'", "'+'", "'-'", "'>'", "'<'", "'>='", 
                     "'<='", "'=='", "'!='", "'if'", "'else'", "'while'", 
                     "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IF", "ELSE", "WHILE", "PRINT", 
                      "ID", "INT", "FLOAT", "WS", "COMMENT", "BLOCK_COMMENT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_assignment = 2
    RULE_printStmt = 3
    RULE_ifStmt = 4
    RULE_whileStmt = 5
    RULE_block = 6
    RULE_expr = 7

    ruleNames =  [ "prog", "stat", "assignment", "printStmt", "ifStmt", 
                   "whileStmt", "block", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    IF=18
    ELSE=19
    WHILE=20
    PRINT=21
    ID=22
    INT=23
    FLOAT=24
    WS=25
    COMMENT=26
    BLOCK_COMMENT=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcScriptParser.StatContext)
            else:
                return self.getTypedRuleContext(CalcScriptParser.StatContext,i)


        def getRuleIndex(self):
            return CalcScriptParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CalcScriptParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.stat()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7602208) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcScriptParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(CalcScriptParser.AssignmentContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStat" ):
                return visitor.visitAssignStat(self)
            else:
                return visitor.visitChildren(self)


    class BlockStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(CalcScriptParser.BlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStat" ):
                return visitor.visitBlockStat(self)
            else:
                return visitor.visitChildren(self)


    class PrintStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printStmt(self):
            return self.getTypedRuleContext(CalcScriptParser.PrintStmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)


    class IfStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStmt(self):
            return self.getTypedRuleContext(CalcScriptParser.IfStmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whileStmt(self):
            return self.getTypedRuleContext(CalcScriptParser.WhileStmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStat" ):
                return visitor.visitWhileStat(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = CalcScriptParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = CalcScriptParser.AssignStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.assignment()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 22
                    self.match(CalcScriptParser.T__0)


                pass
            elif token in [21]:
                localctx = CalcScriptParser.PrintStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.printStmt()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 26
                    self.match(CalcScriptParser.T__0)


                pass
            elif token in [18]:
                localctx = CalcScriptParser.IfStatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.ifStmt()
                pass
            elif token in [20]:
                localctx = CalcScriptParser.WhileStatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.whileStmt()
                pass
            elif token in [5]:
                localctx = CalcScriptParser.BlockStatContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalcScriptParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return CalcScriptParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = CalcScriptParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(CalcScriptParser.ID)
            self.state = 35
            self.match(CalcScriptParser.T__1)
            self.state = 36
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(CalcScriptParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return CalcScriptParser.RULE_printStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = CalcScriptParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(CalcScriptParser.PRINT)
            self.state = 39
            self.match(CalcScriptParser.T__2)
            self.state = 40
            self.expr(0)
            self.state = 41
            self.match(CalcScriptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CalcScriptParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcScriptParser.ExprContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcScriptParser.StatContext)
            else:
                return self.getTypedRuleContext(CalcScriptParser.StatContext,i)


        def ELSE(self):
            return self.getToken(CalcScriptParser.ELSE, 0)

        def getRuleIndex(self):
            return CalcScriptParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = CalcScriptParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(CalcScriptParser.IF)
            self.state = 44
            self.match(CalcScriptParser.T__2)
            self.state = 45
            self.expr(0)
            self.state = 46
            self.match(CalcScriptParser.T__3)
            self.state = 47
            self.stat()
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 48
                self.match(CalcScriptParser.ELSE)
                self.state = 49
                self.stat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CalcScriptParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcScriptParser.ExprContext,0)


        def stat(self):
            return self.getTypedRuleContext(CalcScriptParser.StatContext,0)


        def getRuleIndex(self):
            return CalcScriptParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = CalcScriptParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(CalcScriptParser.WHILE)
            self.state = 53
            self.match(CalcScriptParser.T__2)
            self.state = 54
            self.expr(0)
            self.state = 55
            self.match(CalcScriptParser.T__3)
            self.state = 56
            self.stat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcScriptParser.StatContext)
            else:
                return self.getTypedRuleContext(CalcScriptParser.StatContext,i)


        def getRuleIndex(self):
            return CalcScriptParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = CalcScriptParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(CalcScriptParser.T__4)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7602208) != 0):
                self.state = 59
                self.stat()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(CalcScriptParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcScriptParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PowerExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerExpr" ):
                return visitor.visitPowerExpr(self)
            else:
                return visitor.visitChildren(self)


    class FloatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(CalcScriptParser.FLOAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalcScriptParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalcScriptParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcScriptParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcScriptParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = CalcScriptParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 68
                self.match(CalcScriptParser.ID)
                pass
            elif token in [23]:
                localctx = CalcScriptParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 69
                self.match(CalcScriptParser.INT)
                pass
            elif token in [24]:
                localctx = CalcScriptParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70
                self.match(CalcScriptParser.FLOAT)
                pass
            elif token in [3]:
                localctx = CalcScriptParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(CalcScriptParser.T__2)
                self.state = 72
                self.expr(0)
                self.state = 73
                self.match(CalcScriptParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 92
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = CalcScriptParser.PowerExprContext(self, CalcScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")

                        self.state = 78
                        self.match(CalcScriptParser.T__6)
                        self.state = 79
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = CalcScriptParser.MulDivExprContext(self, CalcScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 81
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 82
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = CalcScriptParser.AddSubExprContext(self, CalcScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 84
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 85
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = CalcScriptParser.RelationalExprContext(self, CalcScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 87
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 88
                        self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = CalcScriptParser.EqualityExprContext(self, CalcScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 90
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 91
                        self.expr(6)
                        pass

             
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         




