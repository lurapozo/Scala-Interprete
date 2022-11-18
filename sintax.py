from ply.yacc import *
from ply.lex import *
from lexen import tokens

#Crear las siguientes reglas


#6 Cuerpo
def p_cuerpo(p):
  '''cuerpo : contenido
  | funcion'''


def p_contenido(p):
  '''contenido : asignacion
  | impresion
  | entrada'''


# Asignacion realizada por: Ramos Pozo
def p_asignacion(p):
  '''asignacion : VAR VARIABLE IGUAL valor
  | VAL VARIABLE IGUAL valor
  | VAL declaracion IGUAL valor
  | VAR declaracion IGUAL valor'''

def p_declaracion(p):
  '''declaracion : VARIABLE DOBLE_PUNTO tipo'''

# Tipos de Datos realizado por: Ramos Pozo
def p_tipo(p):
  '''tipo : INTCLASS
  | LONGCLASS
  | DOUBLECLASS
  | FLOATCLASS
  | CHARCLASS
  | STRINGCLASS
  | BOOLCLASS'''

def p_valor(p):
  '''valor : INT
  | LONG
  | FLOAT
  | DOUBLE
  | STRING
  | CHAR
  | VARIABLE
  | TRUE
  | FLASE'''


# Definicion de funcion
def p_funcion(p):
  'funcion : DEF VARIABLE PAR_I parametro PAR_D IGUAL LLAVE_I contenido LLAVE_D'

def p_parametro(p):
  '''parametro : VARIABLE
  | VARIABLE COMA parametro'''


# Impresion
def p_impresion(p):
  '''impresion : PRINTLN PAR_I valor PAR_D
  | PRINT PAR_I valor PAR_D'''


# Entrada de datos
def p_entrada(p):
  '''entrada : READLINE PAR_I PAR_D'''

# Estructura de Datos


def p_error(p):
  if p:
    print(
      f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    )
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")


# Build the parser
parser = yacc()

def validaRegla(s):
  result = parser.parse(s)
  print(result)


while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)
