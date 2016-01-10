#!/usr/bin/python

import argparse
import logging
import ply.lex as lex

MAX_INTEGER = 2**31 - 1

#reserved keywords in cool
reserved = {
    'class' : 'CLASS',
    'else' : 'ELSE',
    'fi' : 'FI',
    'if' : 'IF',
    'in' : 'IN',
    'inherits' : 'INHERITS',
    'isvoid' : 'ISVOID',
    'let' : 'LET',
    'loop' : 'LOOP',
    'pool' : 'POOL',
    'then' : 'THEN',
    'while' : 'WHILE',
    'case' : 'CASE',
    'esac' : 'ESAC',
    'new' : 'NEW',
    'of' : 'OF',
    'not' : 'NOT',
    'true' : 'TRUE',
    'false' : 'FALSE'
    }

#tokens to be generated by lexer in cool 
tokens = [
    'INTEGER',
    'IDENTIFIER',
    'TYPE',
    'STRING',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'TIMES',
    'SEMI',
    'COMMA',
    'COLON',
    'LE',
    'LT',
    'GE',
    'GT',
    'EQUALS',
    'LARROW',
    'RARROW',
    'TILDE',
    'DOT',
    'AT',
    'COMMENT'
    ] + list(reserved.values())

#tokens for which values should be printed
tokens_to_print = {
    'INTEGER' : '', 
    'STRING' : '',
    'IDENTIFIER' : '', 
    'TYPE' : ''
}
    

t_ignore = ' \t\f\r\v'

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_PLUS = r'\+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_TIMES = r'\*'
t_SEMI = r';'
t_COLON = r':'
t_COMMA = ','
t_LE = r'<='
t_LT = r'<'
t_GE = r'>='
t_GT = r'>'
t_EQUALS = r'='
t_LARROW = r'<-'
t_RARROW = r'=>'
t_TILDE = r'~'
t_DOT = '\.'
t_AT = '@'

def t_STRING(t):
    r'"(\\"|[\\\t\\\n]|.)*?"'
    t.value = t.value[1:]
    t.value = t.value[:-1]
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-z][a-zA-z0-9_]*|self'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_TYPE(t):
    r'SELF_TYPE|[A-Z][a-zA-Z0-9]*'
    return t

def t_COMMENT(t):
     r'(--.*)|(\(\*(.|\n)*?\*\))'
     t.lexer.lineno += t.value.count('\n')
     #return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

def init_logger():
    logging.basicConfig(
        level = logging.DEBUG,
        filename = "lexlog.txt",
        filemode = "w",
        format = "%(filename)10s:%(lineno)4d:%(message)s"
        )

def print_tokens(lex):
    for tok in iter(lex.token, None):
        print tok.lineno
        print tok.type.lower()
        if tok.type in tokens_to_print:
            print tok.value  

def parse_file(filename, lex):
    with open(filename, 'r') as inp:
        lex.input(inp.read())
        print_tokens(lex)

def get_tokens_from_cin(lex):
    while True:
        inp = raw_input()
        if inp.strip() == 'quit':
            break
        else:
            inp += '\n'
            lex.input(inp)
            print_tokens(lex)
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help = 'file from which to read')
    return parser.parse_args()

def main():
    init_logger()
    log = logging.getLogger() 
    lex.lex(debug=True, debuglog=log)
    args = get_args()
    if args.file:
        parse_file(args.file, lex)
    else:
        get_tokens_from_cin(lex)

if __name__ == '__main__':
    main()

