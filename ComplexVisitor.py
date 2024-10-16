# Generated from Complex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ComplexParser import ComplexParser
else:
    from ComplexParser import ComplexParser

# This class defines a complete generic visitor for a parse tree produced by ComplexParser.

class ComplexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ComplexParser#program.
    def visitProgram(self, ctx:ComplexParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#Add.
    def visitAdd(self, ctx:ComplexParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#SingleTerm.
    def visitSingleTerm(self, ctx:ComplexParser.SingleTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#Subtract.
    def visitSubtract(self, ctx:ComplexParser.SubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#term.
    def visitTerm(self, ctx:ComplexParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#Parentheses.
    def visitParentheses(self, ctx:ComplexParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#ComplexExpr.
    def visitComplexExpr(self, ctx:ComplexParser.ComplexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#RealNumber.
    def visitRealNumber(self, ctx:ComplexParser.RealNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#complexNumber.
    def visitComplexNumber(self, ctx:ComplexParser.ComplexNumberContext):
        return self.visitChildren(ctx)



del ComplexParser