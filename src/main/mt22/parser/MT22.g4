grammar MT22;

@lexer::header {
from lexererr import *;

}

options{
	language=Python3;
}

program: declarationlist EOF;






//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Parser PART
declaration: (vardecl|funcdecl) ;
declarationlist: declaration declarationlisttail|declaration;
declarationlisttail: declaration declarationlisttail|;
//List of var and func declaration
// vardecllist: vardecl vardecllisttail| vardecl;
// vardecllisttail: vardecl vardecllisttail| ;
// funcdeclist: funcdecl funcdeclisttail| funcdecl;
// funcdeclisttail: funcdecl funcdeclisttail|;

// mainfunc: MAIN COLON FUNCTION  (atomicType|voidType|arrayType|autoType) LPAREN RPAREN funcbody ;
boolean: TRUE|FALSE ;
arraylit: LCURLY (exprlist) RCURLY;
comment: COMMENTCPP| COMMENTC;

//Types and values
atomicType: BOOLEAN|INTEGER|FLOAT|STRING;
dimension: INTLIT dimensiontail| INTLIT;
dimensiontail: COMMA INTLIT dimensiontail| ;
arrayType: ARRAY LSQBRACKET dimension RSQBRRACKET OF atomicType ;
voidType: VOID ;
autoType: AUTO;

//Declarations
idlist:ID idtail|ID ;
idtail: COMMA ID idtail| ; 
vardecl : idlist COLON (atomicType|autoType|dimension|arrayType) SEMI |vardeclnosemi SEMI;
vardeclnosemi: ID COLON (atomicType|autoType|dimension|arrayType) ASSIGN expr | ID COMMA vardeclnosemi COMMA expr;
vardecllist: vardecl vardecllisttail| vardecl;
vardecllisttail: vardecl vardecllisttail|;
para: ('inherit'|) ('out'|) ID COLON (atomicType|autoType|dimension|arrayType) ;
paralist: para paratail| para;
paratail: COMMA para paratail|;
funcdecl: funcpropo funcbody ;
funcpropo: ID COLON FUNCTION (atomicType|voidType|arrayType|autoType) 
	LPAREN (paralist|) RPAREN ((INHERIT ID)|) ;
funcbody:blockstmt;
callexpr: ID'('(exprlist|)')' ;



//index operators
idxOp: ID LSQBRACKET exprlist RSQBRRACKET;

//Expressions (Checking the unary again)
expr: expr1 STRCONCAT expr1 | expr1;
expr1: expr2 (EQ|NOTEQ|SMALLER|GREATER|GREATEREQ|SMALLEREQ) expr2| expr2 ;
expr2: expr2 (AND|OR) expr3| expr3;
expr3: expr3 (PLUS|MINUS) expr4| expr4; 
expr4: expr4 (MUL|DIVIDE|MODULO) expr5| expr5; 
expr5: (NOT) expr5| expr6;
expr6: (MINUS) expr6| expr7; 
expr7: idxOp | expr8; 
expr8: ID|numOperand|booleanOperand|stringOperand|relationalOperand|callexpr|subexpr|arraylit;
//List of operands
exprlist: expr exprlisttail| expr;
exprlisttail: COMMA expr exprlisttail|;
subexpr: '('expr')' ;
numOperand: INTLIT|FLOATLIT ;
booleanOperand: boolean;
stringOperand: STRLIT;
relationalOperand: INTLIT|boolean;


//Statements
stmt:assignstmt|ifstmt|forstmt|whilestmt|do_whilestmt|breakstmt
	|continuestmt|returnstmt|callstmt|blockstmt;
stmtlist: stmt stmtlisttail| stmt;
stmtlisttail: stmt stmtlisttail| ;
lhs: ID|idxOp;
assignstmt: lhs ASSIGN expr SEMI ;
ifstmt: IF LPAREN expr RPAREN stmt ((ELSE stmt)|) ;
forstmt: 'for' LPAREN lhs ASSIGN expr COMMA expr COMMA expr RPAREN
    stmt  ;//different from Parser
whilestmt: WHILE LPAREN expr RPAREN stmt;
do_whilestmt: DO blockstmt WHILE LPAREN expr RPAREN SEMI;
breakstmt: BREAK SEMI;
continuestmt: CONTINUE SEMI;
returnstmt: RETURN (expr|) SEMI;
callstmt: ID LPAREN (exprlist|) RPAREN SEMI;
blockstmt: LCURLY (blockcontentlist|) RCURLY;
blockcontent: (stmt|vardecl);
blockcontentlist: blockcontent blockcontentlisttail| blockcontent;
blockcontentlisttail: blockcontent blockcontentlisttail|;





//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Lexer PART
WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines, return, backspace, and form feed
LCOMMENTC: '/*';
RCOMMENTC: '*/';
COMMENTCPPSYM: '//';
//Comments
COMMENTC : '/*' .*? '*/' -> skip;
COMMENTCPP : '//' (~[\r\f\n])* -> skip;
//Keywords
AUTO: 'auto';
INTEGER: 'integer';
VOID: 'void';
ARRAY:'array';
BREAK: 'break';
FLOAT: 'float';
RETURN: 'return';
OUT: 'out';
BOOLEAN: 'boolean';
FOR: 'for';
STRING: 'string';
CONTINUE: 'continue';
DO: 'do';
// MAIN: 'main';
FUNCTION: 'function';
OF: 'of';
ELSE: 'else';
IF: 'if';
WHILE: 'while';
INHERIT: 'inherit';
TRUE: 'true';
FALSE: 'false';
//Operators
PLUS: '+';
NOT: '!';
NOTEQ: '!=';
MINUS: '-';
MUL:'*';
AND: '&&';
SMALLER: '<';
OR: '||';
SMALLEREQ: '<=';
DIVIDE: '/';
EQ: '==';
GREATER: '>';
MODULO: '%';
GREATEREQ: '>=';
STRCONCAT: '::';
//Seperators
DOT: '.';
COLON: ':';
COMMA : ',' ;
SEMI : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;
ASSIGN: '=';
LSQBRACKET: '[';
RSQBRRACKET: ']';
//Literals
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
INTLIT : [0]|[1-9]+[0-9_]* {self.text = self.text.replace("_", "")} ;
FLOATLIT: (INTPART|) (DECIMAL|EXP|DECIMAL EXP?) {self.text = self.text.replace("_", "")} ;
fragment DECIMAL: '.' [0-9]*;
fragment EXP: ('e'|'E') (MINUS|PLUS)? [0-9]+;
fragment INTPART: [0]|[1-9]+[0-9_]*  ;
STRLIT: '"'StrChar?'"' {self.text = self.text[1:-1]};
fragment StrChar:(~["\r\n] | EscSe)+;
fragment EscSe:'\\' [btnfr"'\\];
//Identifiers
UNCLOSE_STRING: ["](~[\\'"\b\f\r\n\t]|EscSe)*EOF?{
    y = str(self.text)
    raise UncloseString(y[1:])
};
ILLEGAL_ESCAPE: ["](~[\\'"\b\f\r\n\t]|EscSe)*('\\'(~[bfrnt'"\\])){
    y = str(self.text)
    raise IllegalEscape(y[1:])
};
ERROR_CHAR: . {
    raise ErrorToken(self.text)
};