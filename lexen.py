from ply.lex import *

#Palabras reservadas. Realizado por Pisco Jordan
reservadas = {
  "abstract": "ABSTRACT",
  "do": "DO",
  "finally": "FINALLY",
  "import": "IMPORT",
  "null": "NULL",
  "protected": "PROTECTED",
  "throw": "THROW",
  "val": "VAL",
  "case": "CASE",
  "else": "ELSE",
  "for": "FOR",
  "lazy": "LAZY",
  "object": "OBJECT",
  "return": "RETURN",
  "trait": "TRAIT",
  "var": "VAR",
  "catch": "CATCH",
  "extends": "EXTENDS",
  "forSome": "FOR_SOME",
  "macro": "MACRO",
  "override": "OVERRIDE",
  "sealed": "SEALED",
  "try": "TRY",
  "while": "WHILE",
  "class": "CLASS",
  "false": "FLASE",
  "if": "IF",
  "match": "MATCH",
  "package": "PACKAGE",
  "super": "SUPER",
  "true": "TRUE",
  "with": "WITH",
  "def": "DEF",
  "final": "FINAL",
  "implicit": "IMPLICIT",
  "new": "NEW",
  "private": "PRIVATE",
  "this": "THIS",
  "type": "TYPE",
  "yield": "YIELD",
  "to": "TO",
  "until": "UNTIL",
  "startsWith":"STARTSWITH",
  "scala.io.StdIn.readLine": "LIBRERIA_IO",
}

#Funciones. Realizado por: Pisco Jordan
funciones = {
  "readLine": "READLINE",
  "print": "PRINT",
  "println": "PRINTLN",
  "reverse": "REVERSE",
  "toInt": "TO_INT",
  "toDouble": "TO_DOUBLE",
  "toFloat": "TO_FLOAT",
  "toLong": "TO_LONG",
}

#Clases y nombres de datos primitivos. Encargado: Gabriel Maldonado
clases = {
  'Int':'INTCLASS',
  'Long':'LONGCLASS',

  'Double':'DOUBLECLASS',
  'Float':'FLOATCLASS',

  'Char':'CHARCLASS',
  'String':'STRINGCLASS',

  'List':'LISTCLASS',
  'Array':'ARRAYCLASS',

  'Boolean':"BOOLCLASS"
}

#Tipos de datos primitivos y variables. Encargado: Gabriel Maldonado

datos = [
  "INT",
  "LONG",

  "DOUBLE",
  "FLOAT",

  "STRING",
  "CHAR",

  "VARIABLE",
]


def t_FLOAT(t):
  r'\d*\.\d+(f|F)'
  t.value = float(t.value[:-1])
  return t


def t_DOUBLE(t):
  r'\d*\.\d+'

  t.value = float(t.value)
  return t


def t_LONG(t):
  r'\d+(l|L)'
  t.value = int(t.value[:-1])
  return t


def t_INT(t):
  r'\d+'
  t.value = int(t.value)
  return t


def t_STRING(t):
  r'"([^"]*|\s)*"'
  t.value = t.value
  return t


def t_CHAR(t):
  r'\'.\''
  t.value = t.value
  return t


def t_VARIABLE(t):
  r'[a-zA-Z][a-zA-Z0-9]*(_)?[a-zA-Z0-9]*'
  t.type = clases.get(t.value, 'VARIABLE')  # Check nombres de clases
  if t.type != 'VARIABLE':
    return t
  t.type = funciones.get(t.value, 'VARIABLE')  # Check nombres de funciones
  if t.type != 'VARIABLE':
    return t
  t.type = reservadas.get(t.value, 'VARIABLE')  # Check palabras reservadas
  return t


#Simbolos de cierre,  simbolos de putuacion y comillas. Realizado por: Ramos Pozo

simbolo = [
  "PAR_D",
  "PAR_I",
  "CORCHETE_D",
  "CORCHETE_I",
  "LLAVE_D",
  "LLAVE_I",
  "COMA",
  "PUNTO",
  "DOBLE_PUNTO",
  "BACKTICK",
  "FUNCION_FLECHA",
  "ITERATOR",
  "HASHTAG",
  "ARROBA",
  "SUBGUION",
]

t_PAR_D = r'\)'
t_PAR_I = r'\('
t_CORCHETE_D = r'\]'
t_CORCHETE_I = r'\['
t_LLAVE_D = r'\}'
t_LLAVE_I = r'\{'
t_COMA = r','
t_PUNTO = r'\.'
t_DOBLE_PUNTO = r':'
t_BACKTICK = r'`'
t_FUNCION_FLECHA = r'=>'
t_ITERATOR = r'<-'
t_HASHTAG = r'\#'
t_ARROBA = r'@'
t_SUBGUION = r'_'

#Operadores logicos, aritmeticos y relacionaes. Realizado por: Ramos Pozo
operadores = [
  #RELACIONALES
  "IGUAL_COMPARACION",
  "DIFERENTE",
  "MAYOR_IGUAL",
  "MENOR_IGUAL",
  "MAYOR",
  "MENOR",

  #LOGICOS
  "AND",
  "OR",
  "NOT",

  #ARITMETICOS
  "MENOS",
  "MAS",
  "MULTIPLICACION",
  "DIVISION",
  "MOD",
  "IGUAL",
]

#RELACIONALES
t_IGUAL_COMPARACION = r'=='
t_DIFERENTE = r'!='
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_MAYOR = r'>'
t_MENOR = r'<'

#LOGICOS
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

#ARIMETICOS
t_MENOS = r'-'
t_MAS = r'\+'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MOD = r'%'
t_IGUAL = r'='

#tokens
tokens = list(reservadas.values()) + datos + operadores + simbolo + list(
  funciones.values()) + list(clases.values())


#Nueva linea , comentarios y errores
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_COMMENT(t):
  r'//.*'
  pass


output = ""


def t_error(t):
  global output
  print("Illegal character '%s'" % t.value[0])
  lastout = output
  output = lastout + "Illegal character " + t.value[0] + "\n"
  t.lexer.skip(1)

lexer = lex()


def getTokens(lexer):
  global output
  output = ""

  for tok in lexer:
    lastout = output
    output = lastout + str(tok) + "\n"


def prosesarLexico(data):
    global output
    global lexer

    lexer = lex()    
    lexer.input(data)
    getTokens(lexer)
    return output
