# Generated from Fourier.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FourierParser import FourierParser
else:
    from FourierParser import FourierParser

# This class defines a complete generic visitor for a parse tree produced by FourierParser.

class FourierVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FourierParser#program.
    def visitProgram(self, ctx:FourierParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#FourierTransform.
    def visitFourierTransform(self, ctx:FourierParser.FourierTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#ArrayExpr.
    def visitArrayExpr(self, ctx:FourierParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#elements.
    def visitElements(self, ctx:FourierParser.ElementsContext):
        return self.visitChildren(ctx)



del FourierParser