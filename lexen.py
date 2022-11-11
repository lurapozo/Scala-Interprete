from lex import *


#Palabras reservadas
reservadas = {
  
}

#Tipos de datos primitivos y variables

datos = [ 
]



#Simbolos de cierre ,  simbolos de putuacion y commilas

simbolo =[
  
]


#Operadores aricmeticos y logicos
operadores = [
  
]



#Funciones
funciones = []

#Clases y nombres de datos primitivos
clases = []

#tokens
tokens = list(reservadas.values()) + datos + operadores + simbolo + relocalizar + clases





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

#Lectura de archivo 
print('Mi primer Lexer')
file = open("source.scala")
archivo = file.read()
file.close()
lexer.input(archivo)
getTokens(lexer)


print('Mi primer Lexer')
while True:
  linea = input(">")
  lexer.input(linea)
  getTokens(lexer)