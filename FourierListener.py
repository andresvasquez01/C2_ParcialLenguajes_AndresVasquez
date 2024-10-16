# Generated from Fourier.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FourierParser import FourierParser
else:
    from FourierParser import FourierParser

# This class defines a complete listener for a parse tree produced by FourierParser.
class FourierListener(ParseTreeListener):

    # Enter a parse tree produced by FourierParser#program.
    def enterProgram(self, ctx:FourierParser.ProgramContext):
        pass

    # Exit a parse tree produced by FourierParser#program.
    def exitProgram(self, ctx:FourierParser.ProgramContext):
        pass


    # Enter a parse tree produced by FourierParser#FourierTransform.
    def enterFourierTransform(self, ctx:FourierParser.FourierTransformContext):
        pass

    # Exit a parse tree produced by FourierParser#FourierTransform.
    def exitFourierTransform(self, ctx:FourierParser.FourierTransformContext):
        pass


    # Enter a parse tree produced by FourierParser#ArrayExpr.
    def enterArrayExpr(self, ctx:FourierParser.ArrayExprContext):
        pass

    # Exit a parse tree produced by FourierParser#ArrayExpr.
    def exitArrayExpr(self, ctx:FourierParser.ArrayExprContext):
        pass


    # Enter a parse tree produced by FourierParser#elements.
    def enterElements(self, ctx:FourierParser.ElementsContext):
        pass

    # Exit a parse tree produced by FourierParser#elements.
    def exitElements(self, ctx:FourierParser.ElementsContext):
        pass



del FourierParser