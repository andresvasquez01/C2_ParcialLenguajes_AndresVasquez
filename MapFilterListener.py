# Generated from MapFilter.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MapFilterParser import MapFilterParser
else:
    from MapFilterParser import MapFilterParser

# This class defines a complete listener for a parse tree produced by MapFilterParser.
class MapFilterListener(ParseTreeListener):

    # Enter a parse tree produced by MapFilterParser#program.
    def enterProgram(self, ctx:MapFilterParser.ProgramContext):
        pass

    # Exit a parse tree produced by MapFilterParser#program.
    def exitProgram(self, ctx:MapFilterParser.ProgramContext):
        pass


    # Enter a parse tree produced by MapFilterParser#mapExpr.
    def enterMapExpr(self, ctx:MapFilterParser.MapExprContext):
        pass

    # Exit a parse tree produced by MapFilterParser#mapExpr.
    def exitMapExpr(self, ctx:MapFilterParser.MapExprContext):
        pass


    # Enter a parse tree produced by MapFilterParser#filterExpr.
    def enterFilterExpr(self, ctx:MapFilterParser.FilterExprContext):
        pass

    # Exit a parse tree produced by MapFilterParser#filterExpr.
    def exitFilterExpr(self, ctx:MapFilterParser.FilterExprContext):
        pass


    # Enter a parse tree produced by MapFilterParser#function.
    def enterFunction(self, ctx:MapFilterParser.FunctionContext):
        pass

    # Exit a parse tree produced by MapFilterParser#function.
    def exitFunction(self, ctx:MapFilterParser.FunctionContext):
        pass


    # Enter a parse tree produced by MapFilterParser#condition.
    def enterCondition(self, ctx:MapFilterParser.ConditionContext):
        pass

    # Exit a parse tree produced by MapFilterParser#condition.
    def exitCondition(self, ctx:MapFilterParser.ConditionContext):
        pass


    # Enter a parse tree produced by MapFilterParser#iterable.
    def enterIterable(self, ctx:MapFilterParser.IterableContext):
        pass

    # Exit a parse tree produced by MapFilterParser#iterable.
    def exitIterable(self, ctx:MapFilterParser.IterableContext):
        pass


    # Enter a parse tree produced by MapFilterParser#element.
    def enterElement(self, ctx:MapFilterParser.ElementContext):
        pass

    # Exit a parse tree produced by MapFilterParser#element.
    def exitElement(self, ctx:MapFilterParser.ElementContext):
        pass



del MapFilterParser