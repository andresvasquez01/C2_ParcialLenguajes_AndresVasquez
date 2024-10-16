
# Proyecto de Lenguajes de Programación - Segundo Corte

Este proyecto contiene tres gramáticas diseñadas en ANTLR para realizar operaciones con números complejos, aplicar funciones como `MAP` y `FILTER`, y calcular la transformada de Fourier discreta.

## Estructura del Proyecto

- **Gramáticas:**
  - `Complex.g4`: Gramática para realizar operaciones con números complejos.
  - `MapFilter.g4`: Gramática que implementa las funciones `MAP` y `FILTER` sobre objetos iterables.
  - `Fourier.g4`: Gramática para calcular la Transformada de Fourier.

- **Archivos generados por ANTLR:**
  - `ComplexLexer.py`, `ComplexParser.py`, `ComplexVisitor.py`: Archivos generados para la gramática `Complex.g4`.
  - `MapFilterLexer.py`, `MapFilterParser.py`, `MapFilterVisitor.py`: Archivos generados para la gramática `MapFilter.g4`.
  - `FourierLexer.py`, `FourierParser.py`, `FourierVisitor.py`: Archivos generados para la gramática `Fourier.g4`.

- **Visitantes personalizados:**
  - `visitor.py`: Implementa el visitor para la gramática de números complejos (`Complex.g4`).
  - `visitorFourier.py`: Implementa el visitor para la gramática de la Transformada de Fourier (`Fourier.g4`).

## Instalación

### Requisitos previos

1. **ANTLR 4.13.2**:
   - Descarga el JAR de ANTLR:
     ```bash
     curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
     ```

   - Exporta la variable de entorno:
     ```bash
     export CLASSPATH=".:/ruta/al/directorio/antlr-4.13.2-complete.jar:$CLASSPATH"
     ```

2. **Python 3**:
   - Instala el runtime de ANTLR para Python:
     ```bash
     pip install antlr4-python3-runtime==4.13.2
     ```

### Generar Archivos desde las Gramáticas

Para generar los archivos de lexer y parser correspondientes a cada gramática:

1. **Complex.g4** (números complejos):
   ```bash
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor Complex.g4
   ```

2. **MapFilter.g4** (funciones `MAP` y `FILTER`):
   ```bash
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor MapFilter.g4
   ```

3. **Fourier.g4** (Transformada de Fourier):
   ```bash
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor Fourier.g4
   ```

## Ejecución

### Operaciones con Números Complejos

El archivo `visitor.py` contiene la implementación del visitor para la gramática `Complex.g4`. Para ejecutar operaciones con números complejos:

```bash
python3 visitor.py
```

Esto procesará una expresión como `(2 + 7i) + (3 - 4i)` y devolverá el resultado de la operación.

### Transformada de Fourier

El archivo `visitorFourier.py` contiene la implementación del visitor para la gramática `Fourier.g4`. Para calcular la Transformada de Fourier de una serie:

```bash
python3 visitorFourier.py
```

Esto procesará una entrada como `fourier([1, 2, 3, 4], 4)` y devolverá la transformada de Fourier discreta de la serie.

### Funciones `MAP` y `FILTER`

Si estás trabajando con `MapFilter.g4`, asegúrate de tener implementado el visitante respectivo para ejecutar las funciones `MAP` y `FILTER`.

## Notas adicionales

- Asegúrate de que todos los archivos generados por ANTLR se encuentran en el mismo directorio que los scripts Python (`visitor.py` y `visitorFourier.py`).
- Si deseas probar con diferentes entradas, puedes modificar directamente las cadenas de entrada en los archivos `visitor.py` y `visitorFourier.py`.


## Autor

Andrés Vásquez
