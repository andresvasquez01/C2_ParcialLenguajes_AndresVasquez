grammar MapFilter;

program: mapExpr | filterExpr;

mapExpr: 'MAP' '(' function ',' iterable ')';
filterExpr: 'FILTER' '(' condition ',' iterable ')';

function: IDENTIFIER;
condition: IDENTIFIER;

iterable:
	'[' element (',' element)* ']'; // Simple list of elements

element: NUMBER;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;

WS: [ 	]+ -> skip;
