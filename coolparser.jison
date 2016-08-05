%{
/*javascript declarations*/
%}

/*jison declaration*/

%token INTEGER
%token IDENTIFIER
%token TYPE
%token STRING
%token LBRACE
%token RBRACE
%token LPAREN
%token RPAREN
%token PLUS
%token MINUS
%token DIVIDE
%token TIMES
%token SEMI
%token COMMA
%token COLON
%token LE
%token LT
%token GE
%token GT
%token EQUALS
%token LARROW
%token RARROW
%token TILDE
%token CLASS
%token ELSE
%token FI
%token IF
%token IN
%token INHERITS
%token ISVOID
%token LET
%token LOOP
%token POOL
%token THEN
%token WHILE
%token CASE
%token ESAC
%token NEW
%token OF
%token NOT
%token TRUE
%token FALSE
%token DOT

%left LARROW
%left NOT
%left LT LE EQUALS
%left GT GE
%left PLUS MINUS
%left TIMES DIVIDE
%nonassoc ISVOID
%left TILDE
%left AT
%left DOT

%%
program 
                : class SEMI class_list
                ;    
class_list  
                : class SEMI class_list
                | 
                ;
class       
                : CLASS TYPE LBRACE feature_list RBRACE
                | CLASS TYPE INHERITS TYPE LBRACE feature_list RBRACE
                ;
                
feature_list    
                : feature SEMI feature_list
                |
                ;
feature         
                : IDENTIFIER LPAREN formal_list RPAREN COLON TYPE LBRACE expr RBRACE
                | IDENTIFIER COLON TYPE 
                | IDENTIFIER COLON TYPE LARROW expr
                ;

formal_list     
                : formal formal_list
                | 
                ;
formal
                : IDENTIFIER COLON TYPE
                ;

expr            
                : IDENTIFIER expr_identifier
                | expr DOT IDENTIFIER LPAREN expr_comma RPAREN
                | expr AT TYPE  DOT IDENTIFIER LPAREN expr_comma RPAREN
                | IF expr THEN expr ELSE expr FI
                | WHILE expr LOOP expr POOL 
                | LBRACE expr SEMI expr_list RBRACE
                | declaration
                | CASE expr OF case_list ESAC
                | NEW TYPE
                | ISVOID expr
                | expr PLUS expr
                | expr MINUS expr
                | expr TIMES expr
                | expr DIVIDE expr
                | TILDE expr
                | expr LT expr
                | expr LE expr
                | expr GT expr
                | expr GE expr
                | expr EQUALS expr
                | NOT expr
                | LPAREN expr RPAREN
                | INTEGER
                | STRING
                | TRUE
                | FALSE
                ;

expr_list       
                : expr SEMI expr
                |
                ;

expr_identifier 
                : LARROW expr
                | LPAREN expr_comma RPAREN
                |
                ;

expr_comma
                : expr comma_expr
                |
                ;

comma_expr
                : COMMA expr
                |
                ;
declaration_list 
                : declaration
                | declaration COMMA declaration_list
                |
                ;

declaration     
                : LET IDENTIFIER COLON TYPE assignment
                ;

assignment
                : LARROW expr
                ;
                
case_list 
                : IDENTIFIER COLON TYPE RARROW expr SEMI case_list 
                |
                ;
%%
