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
  '''tipo : CHARCLASS
  | STRINGCLASS
  | BOOLCLASS
  | INTCLASS
  | LONGCLASS
  | DOUBLECLASS
  | FLOATCLASS'''

def p_valor(p):
  '''valor : STRING
  | CHAR
  | VARIABLE
  | numeros
  | booleanos'''

def p_booleanos(p):
  '''booleanos : TRUE
  | FLASE'''

def p_numeros(p):
  '''numeros : INT
  | LONG
  | FLOAT
  | DOUBLE'''

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

#Condicionales por Juan Pisco
def p_condicional(p):
  '''condicional : valorC logicos condicional
  | valorC'''

def p_valorC(p):
  '''valorC : VARIABLE
  | booleanos
  | relacional
  | NOT VARIABLE
  | NOT booleanos
  | NOT relacional
  '''
def p_logicos(p):
  '''logicos : AND
  | OR
  | NOT'''
#Comparaciones por Juan Pisco
def p_relacional(p):
  '''relacional : numeros comparacion numeros
  | booleanos comparacion booleanos
  | STRING comparacion STRING
  | CHAR comparacion CHAR
  | VARIABLE comparacion numeros
  | numeros comparacion VARIABLE
  | VARIABLE comparacion booleanos
  | booleanos comparacion VARIABLE
  | VARIABLE comparacion STRING
  | STRING comparacion VARIABLE
  | VARIABLE comparacion CHAR
  | CHAR comparacion VARIABLE
  | VARIABLE comparacion VARIABLE'''

def p_comparacion(p):
  '''comparacion : IGUAL_COMPARACION
  | DIFERENTE
  | MAYOR
  | MENOR'''

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
