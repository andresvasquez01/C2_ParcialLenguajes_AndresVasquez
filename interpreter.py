import sys
from antlr4 import *
from MapFilterLexer import MapFilterLexer
from MapFilterParser import MapFilterParser

# Función auxiliar para verificar si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Funciones para MAP
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def double(x):
    return x * 2

def negate(x):
    return -x

def even_to_zero(x):
    return 0 if x % 2 == 0 else x

class MapFilterEvalListener(ParseTreeListener):
    def __init__(self, numeros):
        self.numeros = numeros

    def exitMapFunction(self, ctx):
        function_name = ctx.function().getText()
        print(f"Applying {function_name} to {self.numeros}")

        # Diccionario de funciones disponibles para MAP
        map_functions = {
            "square": square,
            "cube": cube,
            "double": double,
            "negate": negate,
            "even_to_zero": even_to_zero,
            "is_prime": is_prime
        }

        # Obtener la función desde el diccionario y aplicarla
        func = map_functions.get(function_name)
        if func:
            resultado = list(map(func, self.numeros))
            print(f"Result of MAP: {resultado}")
        else:
            print(f"Function {function_name} not supported.")

    def exitFilterFunction(self, ctx):
        condition_name = ctx.condition().getText()
        print(f"Applying {condition_name} filter to {self.numeros}")

        # Diccionario de condiciones disponibles para FILTER
        filter_conditions = {
            "even": lambda x: x % 2 == 0,
            "odd": lambda x: x % 2 != 0,
            "asc": sorted,
            "desc": lambda x: sorted(x, reverse=True)
        }

        # Obtener la condición desde el diccionario y aplicarla
        condition = filter_conditions.get(condition_name)
        if condition:
            # Verificar si es una función de filtro o de ordenación
            if condition_name in ["asc", "desc"]:
                resultado = condition(self.numeros)
            else:
                resultado = list(filter(condition, self.numeros))
            print(f"Result of FILTER: {resultado}")
        else:
            print(f"Condition {condition_name} not supported.")

def main(argv):
    # Recibir los números desde la consola o como argumentos
    if len(argv) > 2:
        numeros = list(map(int, argv[2:]))  # Los números ingresados como argumentos
    else:
        numeros = list(map(int, input("Introduce una lista de números separados por espacio: ").split()))

    input_stream = FileStream(argv[1])
    lexer = MapFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MapFilterParser(stream)
    tree = parser.program()

    listener = MapFilterEvalListener(numeros)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)