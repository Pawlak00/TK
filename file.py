import ply.lex as lex;
from ply.lex import Token
import sys

tokens = (  'PLUS',  'MINUS',  'TIMES',  'DIVIDE',  'LPAREN',  'RPAREN' ,  'NUMBER', 'ID','EQ', 'EW_PLUS', 'EW_MINUS', 'EW_TIMES','EW_DIV',
            'EQ_PLUS','EQ_MINUS', 'EQ_TIMES', 'EQ_DIVIDE','LT','GT','EQ_LT', 'EQ_GT', 'NOT_EQ', 'C_EQ', 'RANGE', 'TRANSPOSE')
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_C_EQ = r'=='
t_EQ=r'\='
t_EW_PLUS = r'\.\+'
t_EW_MINUS = r'\.-'
t_EW_TIMES = r'\.\*'
t_EW_DIV = r'\./'
t_EQ_PLUS = r'\+='
t_EQ_MINUS = r'\-='
t_EQ_TIMES = r'\*='
t_EQ_DIVIDE = r'='
t_LT = r'\<'
t_GT = r'\>'
t_EQ_LT = r'\<='
t_EQ_GT = r'\>0'
t_NOT_EQ = r'\!='
t_RANGE = r'::'
t_TRANSPOSE = r'\''
t_STRING = r'"[\s.a-zA-Z_]+"'
literals = [ '+','-','*','/','(',')','=', '[', ']', '{', '}',',',';' ]

reserved = {
    'if'    : 'if',
    'else'  : 'else',
    'while' : 'while',
    'for'   : 'for',
    'break' : 'break',
    'continue'  : 'continue',
    'return' : 'return',
    'eyes'  : 'eyes',
    'zeros' : 'zeros',
    'ones'  : 'ones',
    'print' : 'print'
}
 
tokens = ['PLUS',  'MINUS',  'TIMES',  'DIVIDE', 'LPAREN',  'RPAREN' ,  'NUMBER', 'ID','EQ', 'EW_PLUS', 'EW_MINUS', 'EW_TIMES','EW_DIV', 'EQ_PLUS',
          'EQ_MINUS', 'EQ_TIMES', 'EQ_DIVIDE', 'LT','GT','EQ_LT', 'EQ_GT', 'NOT_EQ', 'C_EQ', 'RANGE', 'TRANSPOSE', 'INT_VAL', 'DOUBLE_VAL', 'STRING'] + list(reserved.values())
 
def t_COMMENT(t):
    r'\#.*'
    pass
 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

r_INT_CONST = r'^[-+]?\d*$'
r_FLOAT_CONST = r'^[-+]?[0-9]+[.]?[0-9]*([eE][-+]?[0-9]+)?$'

def t_DOUBLE_VAL(t):
    '[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
    return t

def t_INT_VAL(t):
    r'[-+]?[0-9]+'
    return t

t_ignore = '\t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t) :
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
fh = open(sys.argv[1], "r");
lexer.input( fh.read() )
for token in lexer:
    print("line %d: %s(%s)" %(token.lineno, token.type, token.value))

