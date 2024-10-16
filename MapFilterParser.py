# Generated from MapFilter.g4 by ANTLR 4.13.2
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
        4,1,10,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,3,0,17,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,5,5,41,8,5,10,5,12,5,
        44,9,5,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,44,0,16,1,0,
        0,0,2,18,1,0,0,0,4,25,1,0,0,0,6,32,1,0,0,0,8,34,1,0,0,0,10,36,1,
        0,0,0,12,47,1,0,0,0,14,17,3,2,1,0,15,17,3,4,2,0,16,14,1,0,0,0,16,
        15,1,0,0,0,17,1,1,0,0,0,18,19,5,1,0,0,19,20,5,2,0,0,20,21,3,6,3,
        0,21,22,5,3,0,0,22,23,3,10,5,0,23,24,5,4,0,0,24,3,1,0,0,0,25,26,
        5,5,0,0,26,27,5,2,0,0,27,28,3,8,4,0,28,29,5,3,0,0,29,30,3,10,5,0,
        30,31,5,4,0,0,31,5,1,0,0,0,32,33,5,8,0,0,33,7,1,0,0,0,34,35,5,8,
        0,0,35,9,1,0,0,0,36,37,5,6,0,0,37,42,3,12,6,0,38,39,5,3,0,0,39,41,
        3,12,6,0,40,38,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,
        43,45,1,0,0,0,44,42,1,0,0,0,45,46,5,7,0,0,46,11,1,0,0,0,47,48,5,
        9,0,0,48,13,1,0,0,0,2,16,42
    ]

class MapFilterParser ( Parser ):

    grammarFileName = "MapFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MAP'", "'('", "','", "')'", "'FILTER'", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_mapExpr = 1
    RULE_filterExpr = 2
    RULE_function = 3
    RULE_condition = 4
    RULE_iterable = 5
    RULE_element = 6

    ruleNames =  [ "program", "mapExpr", "filterExpr", "function", "condition", 
                   "iterable", "element" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    IDENTIFIER=8
    NUMBER=9
    WS=10

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

        def mapExpr(self):
            return self.getTypedRuleContext(MapFilterParser.MapExprContext,0)


        def filterExpr(self):
            return self.getTypedRuleContext(MapFilterParser.FilterExprContext,0)


        def getRuleIndex(self):
            return MapFilterParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MapFilterParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.mapExpr()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.filterExpr()
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


    class MapExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(MapFilterParser.FunctionContext,0)


        def iterable(self):
            return self.getTypedRuleContext(MapFilterParser.IterableContext,0)


        def getRuleIndex(self):
            return MapFilterParser.RULE_mapExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapExpr" ):
                listener.enterMapExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapExpr" ):
                listener.exitMapExpr(self)




    def mapExpr(self):

        localctx = MapFilterParser.MapExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mapExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(MapFilterParser.T__0)
            self.state = 19
            self.match(MapFilterParser.T__1)
            self.state = 20
            self.function()
            self.state = 21
            self.match(MapFilterParser.T__2)
            self.state = 22
            self.iterable()
            self.state = 23
            self.match(MapFilterParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MapFilterParser.ConditionContext,0)


        def iterable(self):
            return self.getTypedRuleContext(MapFilterParser.IterableContext,0)


        def getRuleIndex(self):
            return MapFilterParser.RULE_filterExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterExpr" ):
                listener.enterFilterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterExpr" ):
                listener.exitFilterExpr(self)




    def filterExpr(self):

        localctx = MapFilterParser.FilterExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_filterExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(MapFilterParser.T__4)
            self.state = 26
            self.match(MapFilterParser.T__1)
            self.state = 27
            self.condition()
            self.state = 28
            self.match(MapFilterParser.T__2)
            self.state = 29
            self.iterable()
            self.state = 30
            self.match(MapFilterParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapFilterParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MapFilterParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = MapFilterParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MapFilterParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MapFilterParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MapFilterParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = MapFilterParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MapFilterParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapFilterParser.ElementContext)
            else:
                return self.getTypedRuleContext(MapFilterParser.ElementContext,i)


        def getRuleIndex(self):
            return MapFilterParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)




    def iterable(self):

        localctx = MapFilterParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_iterable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(MapFilterParser.T__5)
            self.state = 37
            self.element()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 38
                self.match(MapFilterParser.T__2)
                self.state = 39
                self.element()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(MapFilterParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MapFilterParser.NUMBER, 0)

        def getRuleIndex(self):
            return MapFilterParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = MapFilterParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(MapFilterParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





