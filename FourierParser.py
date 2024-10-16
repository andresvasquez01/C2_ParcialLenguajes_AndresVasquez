# Generated from Fourier.g4 by ANTLR 4.13.2
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
        4,1,7,30,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,25,8,3,10,3,12,3,28,
        9,3,1,3,0,0,4,0,2,4,6,0,0,26,0,8,1,0,0,0,2,11,1,0,0,0,4,17,1,0,0,
        0,6,21,1,0,0,0,8,9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,5,1,0,
        0,12,13,3,4,2,0,13,14,5,2,0,0,14,15,5,6,0,0,15,16,5,3,0,0,16,3,1,
        0,0,0,17,18,5,4,0,0,18,19,3,6,3,0,19,20,5,5,0,0,20,5,1,0,0,0,21,
        26,5,6,0,0,22,23,5,2,0,0,23,25,5,6,0,0,24,22,1,0,0,0,25,28,1,0,0,
        0,26,24,1,0,0,0,26,27,1,0,0,0,27,7,1,0,0,0,28,26,1,0,0,0,1,26
    ]

class FourierParser ( Parser ):

    grammarFileName = "Fourier.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'fourier('", "','", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_array = 2
    RULE_elements = 3

    ruleNames =  [ "program", "expr", "array", "elements" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(FourierParser.ExprContext,0)


        def EOF(self):
            return self.getToken(FourierParser.EOF, 0)

        def getRuleIndex(self):
            return FourierParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = FourierParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr()
            self.state = 9
            self.match(FourierParser.EOF)
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
            return FourierParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FourierTransformContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(FourierParser.ArrayContext,0)

        def NUMBER(self):
            return self.getToken(FourierParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFourierTransform" ):
                listener.enterFourierTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFourierTransform" ):
                listener.exitFourierTransform(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFourierTransform" ):
                return visitor.visitFourierTransform(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = FourierParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            localctx = FourierParser.FourierTransformContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(FourierParser.T__0)
            self.state = 12
            self.array()
            self.state = 13
            self.match(FourierParser.T__1)
            self.state = 14
            self.match(FourierParser.NUMBER)
            self.state = 15
            self.match(FourierParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FourierParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayExprContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FourierParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def elements(self):
            return self.getTypedRuleContext(FourierParser.ElementsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayExpr" ):
                listener.enterArrayExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayExpr" ):
                listener.exitArrayExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)



    def array(self):

        localctx = FourierParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array)
        try:
            localctx = FourierParser.ArrayExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(FourierParser.T__3)
            self.state = 18
            self.elements()
            self.state = 19
            self.match(FourierParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(FourierParser.NUMBER)
            else:
                return self.getToken(FourierParser.NUMBER, i)

        def getRuleIndex(self):
            return FourierParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = FourierParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(FourierParser.NUMBER)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 22
                self.match(FourierParser.T__1)
                self.state = 23
                self.match(FourierParser.NUMBER)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





