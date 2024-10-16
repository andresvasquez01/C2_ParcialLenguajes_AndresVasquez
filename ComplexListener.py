# Generated from Complex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ComplexParser import ComplexParser
else:
    from ComplexParser import ComplexParser

# This class defines a complete listener for a parse tree produced by ComplexParser.
class ComplexListener(ParseTreeListener):

    # Enter a parse tree produced by ComplexParser#program.
    def enterProgram(self, ctx:ComplexParser.ProgramContext):
        pass

    # Exit a parse tree produced by ComplexParser#program.
    def exitProgram(self, ctx:ComplexParser.ProgramContext):
        pass


    # Enter a parse tree produced by ComplexParser#Add.
    def enterAdd(self, ctx:ComplexParser.AddContext):
        pass

    # Exit a parse tree produced by ComplexParser#Add.
    def exitAdd(self, ctx:ComplexParser.AddContext):
        pass


    # Enter a parse tree produced by ComplexParser#SingleTerm.
    def enterSingleTerm(self, ctx:ComplexParser.SingleTermContext):
        pass

    # Exit a parse tree produced by ComplexParser#SingleTerm.
    def exitSingleTerm(self, ctx:ComplexParser.SingleTermContext):
        pass


    # Enter a parse tree produced by ComplexParser#Subtract.
    def enterSubtract(self, ctx:ComplexParser.SubtractContext):
        pass

    # Exit a parse tree produced by ComplexParser#Subtract.
    def exitSubtract(self, ctx:ComplexParser.SubtractContext):
        pass


    # Enter a parse tree produced by ComplexParser#term.
    def enterTerm(self, ctx:ComplexParser.TermContext):
        pass

    # Exit a parse tree produced by ComplexParser#term.
    def exitTerm(self, ctx:ComplexParser.TermContext):
        pass


    # Enter a parse tree produced by ComplexParser#Parentheses.
    def enterParentheses(self, ctx:ComplexParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by ComplexParser#Parentheses.
    def exitParentheses(self, ctx:ComplexParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by ComplexParser#ComplexExpr.
    def enterComplexExpr(self, ctx:ComplexParser.ComplexExprContext):
        pass

    # Exit a parse tree produced by ComplexParser#ComplexExpr.
    def exitComplexExpr(self, ctx:ComplexParser.ComplexExprContext):
        pass


    # Enter a parse tree produced by ComplexParser#RealNumber.
    def enterRealNumber(self, ctx:ComplexParser.RealNumberContext):
        pass

    # Exit a parse tree produced by ComplexParser#RealNumber.
    def exitRealNumber(self, ctx:ComplexParser.RealNumberContext):
        pass


    # Enter a parse tree produced by ComplexParser#complexNumber.
    def enterComplexNumber(self, ctx:ComplexParser.ComplexNumberContext):
        pass

    # Exit a parse tree produced by ComplexParser#complexNumber.
    def exitComplexNumber(self, ctx:ComplexParser.ComplexNumberContext):
        pass



del ComplexParser