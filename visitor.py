from antlr4 import *
from ComplexLexer import ComplexLexer
from ComplexParser import ComplexParser
from ComplexVisitor import ComplexVisitor

class EvalVisitor(ComplexVisitor):
    def visitAdd(self, ctx):
        left = self.visit(ctx.expr())  # Primer operando (izquierdo)
        right = self.visit(ctx.term())  # Segundo operando (derecho)
        result = left + right  # Realiza la suma de los dos números complejos
        print(f"Suma: {left} + {right} = {result}")
        return result

    def visitSubtract(self, ctx):
        left = self.visit(ctx.expr())  # Primer operando (izquierdo)
        right = self.visit(ctx.term())  # Segundo operando (derecho)
        result = left - right  # Realiza la resta de los dos números complejos
        print(f"Resta: {left} - {right} = {result}")
        return result

    def visitComplexExpr(self, ctx):
        real_part = 0.0
        imaginary_part = 0.0

        # Extraemos los componentes del número complejo si existen
        components = ctx.getText().split('i')[0]  # Obtener el número sin la 'i'

        # Si hay un signo en la mitad, dividimos en real e imaginario
        if '+' in components or '-' in components:
            # Separar en parte real e imaginaria
            parts = components.split('+') if '+' in components else components.split('-')
            real_part = float(parts[0].strip())
            imaginary_part = float(parts[1].strip()) if '+' in components else -float(parts[1].strip())
        else:
            # Si solo hay una parte (real o imaginaria)
            if 'i' in ctx.getText():  # Solo parte imaginaria
                imaginary_part = float(components.strip())
            else:  # Solo parte real
                real_part = float(components.strip())

        print(f"Complejo: {real_part} + {imaginary_part}i")
        return complex(real_part, imaginary_part)

    def visitRealNumber(self, ctx):
        number = float(ctx.getText())
        print(f"Real: {number}")
        return number

    def visitParentheses(self, ctx):
        print("Paréntesis encontrado, visitando expresión dentro del paréntesis.")
        return self.visit(ctx.expr())

    def visitFactor(self, ctx):
        # Si el factor es una expresión entre paréntesis
        if ctx.expr():
            print("Paréntesis encontrado, visitando expresión dentro del paréntesis.")
            return self.visit(ctx.expr())
        
        # Si el factor es un número complejo
        if ctx.complexNumber():
            print("Número complejo encontrado, visitando número complejo.")
            return self.visitComplexExpr(ctx.complexNumber())
        
        # Si el factor es un número real
        if ctx.NUMBER():
            print("Número real encontrado, visitando número real.")
            return self.visitRealNumber(ctx)
        
        # Si llegamos aquí, algo no está bien
        print("Error: Factor no reconocido en el contexto")
        raise ValueError("Factor no reconocido en el contexto")

    def visitTerm(self, ctx):
        return self.visit(ctx.factor())

    def visitProgram(self, ctx):
        print("Visitando el programa")
        return self.visit(ctx.expr())

# Prueba el visitor
def main():
    input_stream = InputStream("(2 + 7i) + (3 - 4i)")
    lexer = ComplexLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ComplexParser(stream)
    tree = parser.program()

    # Imprime el árbol de sintaxis generado
    print(tree.toStringTree(recog=parser))

    visitor = EvalVisitor()
    result = visitor.visit(tree)  # Visitar el árbol de sintaxis
    print("Resultado final:", result)

if __name__ == "__main__":
    main()
