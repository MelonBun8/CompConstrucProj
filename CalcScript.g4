grammar CalcScript;

/*
 * Parser Rules
 */

prog: (funcDecl | stat)+ ;

funcDecl: 'func' ID LPAREN paramList? RPAREN (COLON type)? block ;

paramList: param (',' param)* ;
param: ID ':' type ;

stat: varDecl SEMI?           # VarDeclStat
    | assignment SEMI?      # AssignStat
    | printStmt SEMI?       # PrintStat
    | ifStmt                # IfStat
    | whileStmt             # WhileStat
    | returnStmt SEMI?      # ReturnStat
    | expr SEMI?            # ExprStat  // Allow function calls as statements
    | block                 # BlockStat
    ;

varDecl: type ID ASSIGN expr ;

assignment: ID ASSIGN expr ;

returnStmt: RETURN expr? ;

printStmt: PRINT LPAREN expr RPAREN ;

ifStmt: IF LPAREN expr RPAREN stat (ELSE stat)? ;

whileStmt: WHILE LPAREN expr RPAREN stat ;

block: LBRACE stat* RBRACE ;

expr: expr POWER expr                   # PowerExpr
    | expr (MUL|DIV) expr               # MulDivExpr
    | expr (ADD|SUB) expr               # AddSubExpr
    | expr (GT|LT|GTE|LTE) expr         # RelationalExpr
    | expr (EQ|NEQ) expr                # EqualityExpr
    | ID LPAREN argList? RPAREN         # FunCallExpr
    | ID                                # IdExpr
    | INT                               # IntExpr
    | FLOAT                             # FloatExpr
    | LPAREN expr RPAREN                # ParenExpr
    ;

argList: expr (',' expr)* ;

type: 'int' | 'float' | 'void' ;

/*
 * Lexer Rules
 */

SEMI: ';' ;
COLON: ':' ;
COMMA: ',' ;
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
RETURN: 'return' ;
FUNC: 'func' ;
TYPE_INT: 'int' ;
TYPE_FLOAT: 'float' ;
TYPE_VOID: 'void' ;

ID: [a-zA-Z_] [a-zA-Z_0-9]* ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;
