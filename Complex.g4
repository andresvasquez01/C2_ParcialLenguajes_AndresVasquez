grammar Complex;

program: expr EOF;

expr: expr '+' term   # Add
    | expr '-' term   # Subtract
    | term            # SingleTerm
    ;

term: factor;

factor: '(' expr ')'   # Parentheses
      | complexNumber  # ComplexExpr
      | NUMBER         # RealNumber
      ;

complexNumber: NUMBER? ('+'|'-')? NUMBER 'i';  // Definición de número complejo

NUMBER: [0-9]+ ('.' [0-9]+)?;  // Números enteros o decimales

WS: [ \t\r\n]+ -> skip;  // Ignorar espacios en blanco
