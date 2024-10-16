# Generated from Complex.g4 by ANTLR 4.13.2
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
        4,1,7,47,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,36,8,3,1,4,3,4,39,8,4,1,4,3,4,42,
        8,4,1,4,1,4,1,4,1,4,0,1,2,5,0,2,4,6,8,0,1,1,0,1,2,47,0,10,1,0,0,
        0,2,13,1,0,0,0,4,27,1,0,0,0,6,35,1,0,0,0,8,38,1,0,0,0,10,11,3,2,
        1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,6,1,-1,0,14,15,3,4,2,0,15,24,
        1,0,0,0,16,17,10,3,0,0,17,18,5,1,0,0,18,23,3,4,2,0,19,20,10,2,0,
        0,20,21,5,2,0,0,21,23,3,4,2,0,22,16,1,0,0,0,22,19,1,0,0,0,23,26,
        1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,1,0,0,0,26,24,1,0,0,0,27,
        28,3,6,3,0,28,5,1,0,0,0,29,30,5,3,0,0,30,31,3,2,1,0,31,32,5,4,0,
        0,32,36,1,0,0,0,33,36,3,8,4,0,34,36,5,6,0,0,35,29,1,0,0,0,35,33,
        1,0,0,0,35,34,1,0,0,0,36,7,1,0,0,0,37,39,5,6,0,0,38,37,1,0,0,0,38,
        39,1,0,0,0,39,41,1,0,0,0,40,42,7,0,0,0,41,40,1,0,0,0,41,42,1,0,0,
        0,42,43,1,0,0,0,43,44,5,6,0,0,44,45,5,5,0,0,45,9,1,0,0,0,5,22,24,
        35,38,41
    ]

class ComplexParser ( Parser ):

    grammarFileName = "Complex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'('", "')'", "'i'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3
    RULE_complexNumber = 4

    ruleNames =  [ "program", "expr", "term", "factor", "complexNumber" ]

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
            return self.getTypedRuleContext(ComplexParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ComplexParser.EOF, 0)

        def getRuleIndex(self):
            return ComplexParser.RULE_program

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

        localctx = ComplexParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expr(0)
            self.state = 11
            self.match(ComplexParser.EOF)
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
            return ComplexParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ComplexParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(ComplexParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SingleTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ComplexParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleTerm" ):
                listener.enterSingleTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleTerm" ):
                listener.exitSingleTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleTerm" ):
                return visitor.visitSingleTerm(self)
            else:
                return visitor.visitChildren(self)


    class SubtractContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ComplexParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(ComplexParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtract" ):
                listener.enterSubtract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtract" ):
                listener.exitSubtract(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtract" ):
                return visitor.visitSubtract(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ComplexParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ComplexParser.SingleTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 14
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 22
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = ComplexParser.AddContext(self, ComplexParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 17
                        self.match(ComplexParser.T__0)
                        self.state = 18
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = ComplexParser.SubtractContext(self, ComplexParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 20
                        self.match(ComplexParser.T__1)
                        self.state = 21
                        self.term()
                        pass

             
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(ComplexParser.FactorContext,0)


        def getRuleIndex(self):
            return ComplexParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = ComplexParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.factor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplexParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RealNumberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(ComplexParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealNumber" ):
                listener.enterRealNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealNumber" ):
                listener.exitRealNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealNumber" ):
                return visitor.visitRealNumber(self)
            else:
                return visitor.visitChildren(self)


    class ComplexExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def complexNumber(self):
            return self.getTypedRuleContext(ComplexParser.ComplexNumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexExpr" ):
                listener.enterComplexExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexExpr" ):
                listener.exitComplexExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexExpr" ):
                return visitor.visitComplexExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesesContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ComplexParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentheses" ):
                return visitor.visitParentheses(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = ComplexParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ComplexParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(ComplexParser.T__2)
                self.state = 30
                self.expr(0)
                self.state = 31
                self.match(ComplexParser.T__3)
                pass

            elif la_ == 2:
                localctx = ComplexParser.ComplexExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.complexNumber()
                pass

            elif la_ == 3:
                localctx = ComplexParser.RealNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.match(ComplexParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplexNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ComplexParser.NUMBER)
            else:
                return self.getToken(ComplexParser.NUMBER, i)

        def getRuleIndex(self):
            return ComplexParser.RULE_complexNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexNumber" ):
                listener.enterComplexNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexNumber" ):
                listener.exitComplexNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexNumber" ):
                return visitor.visitComplexNumber(self)
            else:
                return visitor.visitChildren(self)




    def complexNumber(self):

        localctx = ComplexParser.ComplexNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_complexNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 37
                self.match(ComplexParser.NUMBER)


            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 40
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 43
            self.match(ComplexParser.NUMBER)
            self.state = 44
            self.match(ComplexParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




