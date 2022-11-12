from lex import *


#Palabras reservadas
reservadas = {
  
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
  r'\d*\.\d+?'

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
  r'"(.*|\s)*"'
  t.value = t.value
  return t

def t_CHAR(t):
  r'\'.\''
  t.value = t.value
  return t

def t_VARIABLE(t):
  r'[a-zA-Z][a-zA-Z0-9]*(_)?[a-zA-Z0-9]*'
  t.type = reservadas.get(t.value, 'VARIABLE')# Check palabras reservadas
  t.type = clases.get(t.value, 'VARIABLE')  # Check nombres de clases
  return t


#Simbolos de cierre,  simbolos de putuacion y comillas. Realizado por: Ramos Pozo

simbolo =[ 
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


#Funciones
funciones = []



#tokens
tokens = list(reservadas.values()) + datos + operadores + simbolo + funciones + list(clases.values())





#Nueva linea , comentarios y errores
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_COMMENT(t):
  r'//.*'
  pass

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)



#Constuxion del lex
lexer = lex()

def getTokens(lexer):
  for tok in lexer:
    print(tok)
'''
#Lectura de archivo 
print('Mi primer Lexer')
file = open("source.scala")
archivo = file.read()
file.close()
lexer.input(archivo)
getTokens(lexer)
'''


print('Mi primer Lexer')
while True:
  linea = input(">")
  lexer.input(linea)
  getTokens(lexer)
