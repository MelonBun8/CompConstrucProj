grammar CalcScript;

/*
 * Parser Rules
 */

prog: stat+ ;

stat: assignment ';'?      # AssignStat
    | printStmt ';'?       # PrintStat
    | ifStmt               # IfStat
    | whileStmt            # WhileStat
    | block                # BlockStat
    ;

assignment: ID '=' expr ;

printStmt: 'print' '(' expr ')' ;

ifStmt: 'if' '(' expr ')' stat ('else' stat)? ;

whileStmt: 'while' '(' expr ')' stat ;

block: '{' stat* '}' ;

expr: expr ('^') expr                 # PowerExpr
    | expr ('*'|'/') expr             # MulDivExpr
    | expr ('+'|'-') expr             # AddSubExpr
    | expr ('>'|'<'|'>='|'<=') expr   # RelationalExpr
    | expr ('=='|'!=') expr           # EqualityExpr
    | ID                              # IdExpr
    | INT                             # IntExpr
    | FLOAT                           # FloatExpr
    | '(' expr ')'                    # ParenExpr
    ;

/*
 * Lexer Rules
 */

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
