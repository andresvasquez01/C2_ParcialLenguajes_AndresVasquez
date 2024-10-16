import cmath
from antlr4 import *
from FourierLexer import FourierLexer
from FourierParser import FourierParser
from FourierVisitor import FourierVisitor

class FourierEvalVisitor(FourierVisitor):
    def visitFourierTransform(self, ctx):
        print("Visitando Fourier Transform")
        array = self.visit(ctx.array())  # Obtener la serie de entrada
        N = int(ctx.NUMBER().getText())  # Obtener el número de puntos
        
        # Calculamos la Transformada de Fourier Discreta
        fourier_result = self.fourier_transform(array, N)
        
        print(f"Transformada de Fourier: {fourier_result}")
        return fourier_result  # Devolver el resultado final

    def visitArrayExpr(self, ctx):
        # Extraer los elementos del array como una lista de números
        elements = [float(num.getText()) for num in ctx.elements().NUMBER()]
        print(f"Array visitado: {elements}")
        return elements

    def fourier_transform(self, array, N):
        result = []
        for k in range(N):
            sum_val = 0
            for n, x_n in enumerate(array):
                angle = -2 * cmath.pi * k * n / N
                sum_val += x_n * cmath.exp(1j * angle)  # Expresión de Fourier
            result.append(sum_val)
        return result

    def visitExpr(self, ctx):
        if ctx.fourier():
            return self.visitFourierTransform(ctx.fourier())
        return None

    def visitProgram(self, ctx):
        return self.visit(ctx.expr())  # Asegurar que devolvemos el resultado de expr

# Prueba el visitor
def main():
    input_stream = InputStream("fourier([1, 2, 3, 4], 4)")
    lexer = FourierLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FourierParser(stream)
    tree = parser.program()

    # Imprime el árbol de sintaxis generado
    print(tree.toStringTree(recog=parser))

    visitor = FourierEvalVisitor()
    result = visitor.visit(tree)  # Visitar el árbol de sintaxis
    
    # Verificación del resultado final
    if result is not None:
        print("Resultado final capturado correctamente:", result)
    else:
        print("Error: El resultado es None.")
    
    # Muestra el resultado final de la transformada
    print("Resultado final:", result)

if __name__ == "__main__":
    main()
