grammar CalcScript;

/*
 * Parser Rules
 */

prog: stat+ ;

stat: assignment SEMI?      # AssignStat
    | printStmt SEMI?       # PrintStat
    | ifStmt                # IfStat
    | whileStmt             # WhileStat
    | block                 # BlockStat
    ;

assignment: ID ASSIGN expr ;

printStmt: PRINT LPAREN expr RPAREN ;

ifStmt: IF LPAREN expr RPAREN stat (ELSE stat)? ;

whileStmt: WHILE LPAREN expr RPAREN stat ;

block: LBRACE stat* RBRACE ;

expr: expr POWER expr                   # PowerExpr
    | expr (MUL|DIV) expr               # MulDivExpr
    | expr (ADD|SUB) expr               # AddSubExpr
    | expr (GT|LT|GTE|LTE) expr         # RelationalExpr
    | expr (EQ|NEQ) expr                # EqualityExpr
    | ID                                # IdExpr
    | INT                               # IntExpr
    | FLOAT                             # FloatExpr
    | LPAREN expr RPAREN                # ParenExpr
    ;

/*
 * Lexer Rules
 */

SEMI: ';' ;
ASSIGN: '=' ;
LPAREN: '(' ;
RPAREN: ')' ;
LBRACE: '{' ;
RBRACE: '}' ;

POWER: '^' ;
MUL: '*' ;
DIV: '/' ;
ADD: '+' ;
SUB: '-' ;

GT: '>' ;
LT: '<' ;
GTE: '>=' ;
LTE: '<=' ;
EQ: '==' ;
NEQ: '!=' ;

IF: 'if' ;
ELSE: 'else' ;
WHILE: 'while' ;
PRINT: 'print' ;

ID: [a-zA-Z_] [a-zA-Z_0-9]* ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;
