%{
#include <stdio.h>
#include <string.h>

int nrLines = 0;


%}

%option noyywrap
%option caseless

intNr 0|[+-]*[1-9][0-9]*
stringConst [a-zA-Z]*
id [a-zA-Z]+[a-zA-Z0-9]*

%%
"go" {printf("Reserved word: %s\n", yytext); return GO;}
"stop" {printf("Reserved word: %s\n", yytext); return STOP;}
"int" {printf("Reserved word: %s\n", yytext); return INT;}
"char" {printf("Reserved word: %s\n", yytext); return CHAR;}
"string" {printf("Reserved word: %s\n", yytext); return STRING;}
"for" {printf("Reserved word: %s\n", yytext); return FOR;}
"if" {printf("Reserved word: %s\n", yytext); return IF;}
"else" {printf("Reserved word: %s\n", yytext); return ELSE;}
"in" {printf("Reserved word: %s\n", yytext); return IN;}
"and" {printf("Reserved word: %s\n", yytext); return AND;}
"variable" {printf("Reserved word: %s\n", yytext); return VARIABLE;}
"input" {printf("Reserved word: %s\n", yytext); return INPUT;}
"range" {printf("Reserved word: %s\n", yytext); return RANGE;}
"display" {printf("Reserved word: %s\n", yytext); return DISPLAY;}
"vector" {printf("Reserved word: %s\n", yytext); return VECTOR;}

{id} {printf( "Identifier: %s\n", yytext); return ID;}

{stringConst} {printf( "Constant: %s\n", yytext ); return STRING_CONST;}

{intNr} {printf( "Constant: %s\n", yytext ); return INT_CONST;}

":" {printf( "Separator: %s\n", yytext ); return COLON;}
"(" {printf( "Separator: %s\n", yytext ); return PARANTEZA_ROTUNDA_OPEN;}
")" {printf( "Separator: %s\n", yytext ); return PARANTEZA_ROTUNDA_CLOSE;}
"[" {printf( "Separator: %s\n", yytext ); return PARANTEZA_DREAPTA_OPEN;}
"]" {printf( "Separator: %s\n", yytext ); return PARANTEZA_DREAPTA_CLOSE;}
"#" {printf( "Separator: %s\n", yytext ); return HASHTAG;}
"," {printf( "Separator: %s\n", yytext ); return COMMA;}
"\"" {printf( "Separator: %s\n", yytext ); return GHILIMEA;}



"+"|"-"|"*"|"/"|"<"|"$"|">"|"<="|">="|"=:="|"==>"|"<=>"|"=="|"^" {printf( "Operator: %s\n", yytext ); addToPIFNotSymbols(yytext);}

[\n]+ {nrLines++;}

[ ]+ {}

. printf("Error on line %d\n", nrLines + 1);

%%
int main(int argc, char** argv) {
    yyin = stdin;
    yylex();
}