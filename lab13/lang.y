%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define YYDEBUG 1

int yylex();


%}
%token GO
%token STOP
%token VARIABLE
%token AND
%token IF
%token ELSE
%token FOR
%token WHILE
%token IN
%token INT
%token CHAR
%token STRING
%token INPUT
%token DISPLAY
%token VECTOR
%token RANGE

%token ID
%token INT_CONST
%token STR_CONST

%token ATTRIB
%token EGAL
%token DIFERIT
%token MAI_MIC_SAU_EGAL
%token MAI_MARE_SAU_EGAL
%token MAI_MIC
%token MAI_MARE
%token NOT


%token PLUS
%token MINUS
%token ORI
%token DIV
%token REST

%token PARANTEZA_ROTUNDA_OPEN
%token PARANTEZA_ROTUNDA_CLOSE
%token PARANTEZA_DREAPTA_OPEN
%token PARANTEZA_DREAPTA_CLOSE

%token COMMA
%token COLON
%token SPACE
%token NEWLINE
%token ARROW_UP

%start program

%%
program : GO cmpdstmt STOP
	;

cmpdstmt : stmt NEWLINE [cmpd_stmt]
    ;

stmt : variable_declaration | vector_declaration | ifstmt | forstmt | iostmt | assignstmt 
    ;

variable_declaration : VARIABLE ID ARROW_UP type
    ;

type: INT | CHAR | STRING
    ;

vector_declaration:  VECTOR ID PARANTEZA_DREAPTA_OPEN INT_CONST PARANTEZA_DREAPTA_CLOSE ATTRIB type
    ;

ifstmt: IF condition COLON cmpd_stmt [ ELSE COLON cmpd_stmt]
    ;

condition: expression relation expression
    ;

expression: expression (PLUS | MINUS) term | term 
    ;

term: term (ORI | DIV) factor | factor 
    ;

factor: PARANTEZA_ROTUNDA_OPEN expression PARANTEZA_ROTUNDA_CLOSE | ID | INT_CONST
    ;

relation: MAI_MIC | MAI_MIC_SAU_EGAL | EGAL | MAI_MARE_SAU_EGAL | MAI_MARE | DIFERIT | ATTRIB
    ;

forstmt: FOR ID IN RANGE PARANTEZA_ROTUNDA_OPEN ID COMMA ID PARANTEZA_ROTUNDA_CLOSE COLON
    ;

iostmt: readstmt | writestmt
    ;

readstmt: ID ATTRIB INPUT PARANTEZA_ROTUNDA_OPEN STRING_CONST PARANTEZA_ROTUNDA_CLOSE
    ;

writestmt: DISPLAY PARANTEZA_ROTUNDA_OPEN ID PARANTEZA_ROTUNDA_CLOSE
    ;

assignstmt: ID ATTRIB expression
    ;

%%


int main(int argc, char **argv)
{
   
}