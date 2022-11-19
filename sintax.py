from ply.yacc import *
from ply.lex import *
from lexen import tokens

#Crear las siguientes reglas


# Cuerpo
def p_cuerpo(p):
  '''cuerpo : funcion
  | funcionDefecto
  | asignacion
  | while
  | for
  | if
  | funcion cuerpo
  | funcionDefecto cuerpo
  | asignacion cuerpo
  | while cuerpo
  | for cuerpo
  | if cuerpo'''

# Contenido de Funciones y de estructuras de control
def p_contenido(p):
  '''contenido : asignacion
  | impresion
  | entrada
  | while
  | for
  | if
  | aritmetica
  | asignacion contenido
  | impresion contenido
  | entrada contenido
  | while contenido
  | for contenido
  | if contenido
  | aritmetica contenido'''

# Asignacion realizada por: Ramos Pozo
def p_asignacion(p):
  '''asignacion : VAR VARIABLE IGUAL VARIABLE
  | VAL VARIABLE IGUAL VARIABLE
  | VAR VARIABLE IGUAL aritmetica
  | VAL VARIABLE IGUAL aritmetica
  | asignacionLong
  | asignacionInt
  | asignacionFloat
  | asignacionDouble
  | asignacionString
  | asignacionChar
  | asignacionBoolean
  | array
  | list'''

def p_asignacionLong(p):
  '''asignacionLong : VAR VARIABLE IGUAL LONG
  | VAR VARIABLE DOBLE_PUNTO LONGCLASS IGUAL LONG
  | VAL VARIABLE IGUAL LONG
  | VAL VARIABLE DOBLE_PUNTO LONGCLASS IGUAL LONG
  | VAR VARIABLE DOBLE_PUNTO LONGCLASS IGUAL VARIABLE
  | VAL VARIABLE DOBLE_PUNTO LONGCLASS IGUAL VARIABLE'''
  
def p_asignacionInt(p):
  '''asignacionInt : VAR VARIABLE IGUAL INT
  | VAR VARIABLE DOBLE_PUNTO INTCLASS IGUAL INT
  | VAL VARIABLE IGUAL INT
  | VAL VARIABLE DOBLE_PUNTO INTCLASS IGUAL INT
  | VAR VARIABLE DOBLE_PUNTO INTCLASS IGUAL VARIABLE
  | VAL VARIABLE DOBLE_PUNTO INTCLASS IGUAL VARIABLE'''

def p_asignacionFloat(p):
  '''asignacionFloat : VAR VARIABLE IGUAL FLOAT
  | VAR VARIABLE DOBLE_PUNTO FLOATCLASS IGUAL FLOAT
  | VAL VARIABLE IGUAL FLOAT
  | VAL VARIABLE DOBLE_PUNTO FLOATCLASS IGUAL FLOAT
  | VAR VARIABLE DOBLE_PUNTO FLOATCLASS IGUAL VARIABLE
  | VAL VARIABLE DOBLE_PUNTO FLOATCLASS IGUAL VARIABLE'''

def p_asignacionDouble(p):
  '''asignacionDouble : VAR VARIABLE IGUAL DOUBLE
  | VAR VARIABLE DOBLE_PUNTO DOUBLECLASS IGUAL DOUBLE
  | VAL VARIABLE IGUAL DOUBLE
  | VAL VARIABLE DOBLE_PUNTO DOUBLECLASS IGUAL DOUBLE
  | VAR VARIABLE DOBLE_PUNTO DOUBLECLASS IGUAL VARIABLE
  | VAL VARIABLE DOBLE_PUNTO DOUBLECLASS IGUAL VARIABLE'''

def p_asignacionString(p):
  '''asignacionString : VAR VARIABLE IGUAL STRING
  | VAR VARIABLE DOBLE_PUNTO STRINGCLASS IGUAL STRING
  | VAL VARIABLE IGUAL STRING
  | VAL VARIABLE DOBLE_PUNTO STRINGCLASS IGUAL STRING
  | VAR VARIABLE DOBLE_PUNTO STRINGCLASS IGUAL VARIABLE
  | VAL VARIABLE DOBLE_PUNTO STRINGCLASS IGUAL VARIABLE'''

def p_asignacionChar(p):
  '''asignacionChar : VAR VARIABLE IGUAL CHAR
  | VAR VARIABLE DOBLE_PUNTO CHARCLASS IGUAL CHAR
  | VAL VARIABLE IGUAL CHAR
  | VAL VARIABLE DOBLE_PUNTO CHARCLASS IGUAL CHAR
  | VAR VARIABLE DOBLE_PUNTO CHARCLASS IGUAL VARIABLE
  | VAL VARIABLE DOBLE_PUNTO CHARCLASS IGUAL VARIABLE'''

def p_asignacionBoolean(p):
  '''asignacionBoolean : VAR VARIABLE IGUAL booleanos
  | VAR VARIABLE DOBLE_PUNTO BOOLCLASS IGUAL booleanos
  | VAL VARIABLE IGUAL booleanos
  | VAL VARIABLE DOBLE_PUNTO BOOLCLASS IGUAL booleanos
  | VAR VARIABLE DOBLE_PUNTO BOOLCLASS IGUAL VARIABLE
  | VAL VARIABLE DOBLE_PUNTO BOOLCLASS IGUAL VARIABLE'''

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


# Funcion sin retorno por Juan Pisco
def p_funcion(p):
  'funcion : DEF VARIABLE PAR_I parametro PAR_D IGUAL LLAVE_I contenido LLAVE_D'

# Funcion con valores por defecto realizada por: Ramos Pozo
def p_funcionDefecto(p):
  '''funcionDefecto : DEF VARIABLE parametroDefecto IGUAL LLAVE_I contenido LLAVE_D
  '''

def p_parametroDefecto(p):
  '''parametroDefecto : PAR_I parametro IGUAL valor PAR_D
  | PAR_I parametro IGUAL valor PAR_D parametroDefecto'''


def p_parametro(p):
  '''parametro : declaracion
  | declaracion COMA parametro'''

def p_declaracion(p):
  '''declaracion : VARIABLE DOBLE_PUNTO tipo'''

# Impresion realziada por: Ramos Pozo
def p_impresion(p):
  '''impresion : PRINTLN PAR_I valorI PAR_D
  | PRINT PAR_I valorI PAR_D'''

def p_valorI(p):
  '''valorI : valor MAS valorI
  | valor'''


# Entrada de datos realizada por: Ramos Pozo
def p_entrada(p):
  '''entrada : READLINE PAR_I PAR_D'''


# Estructura de Datos
#Array realizado por: Ramos Pozo
def p_array(p):
  '''array : VAR VARIABLE IGUAL ARRAYCLASS PAR_I valores PAR_D
  | VAR VARIABLE DOBLE_PUNTO ARRAYCLASS CORCHETE_I tipo CORCHETE_D IGUAL ARRAYCLASS PAR_I valores PAR_D
  | VAR VARIABLE DOBLE_PUNTO ARRAYCLASS CORCHETE_I tipo CORCHETE_D IGUAL ARRAYCLASS CORCHETE_I tipo CORCHETE_D PAR_I INT PAR_D'''

# List por Juan Pisco
def p_list(p):
  '''list : VAL VARIABLE IGUAL LISTCLASS PAR_I valores PAR_D
  | VAL VARIABLE DOBLE_PUNTO LISTCLASS CORCHETE_I tipo CORCHETE_D IGUAL LISTCLASS PAR_I valores PAR_D'''



def p_valores(p):
  '''valores : valor
  | valor COMA valores'''


# Estructuras de Control
# While realizada por: Ramos Pozo
def p_while(p):
  '''while : WHILE PAR_I condicional PAR_D LLAVE_I contenido LLAVE_D'''

# For por Juan Pisco
def p_for(p):
  '''for : FOR PAR_I VAR VARIABLE ITERATOR VARIABLE PAR_D LLAVE_I contenido LLAVE_D
  | FOR PAR_I VARIABLE ITERATOR VARIABLE PAR_D LLAVE_I contenido LLAVE_D
  | FOR PAR_I VARIABLE ITERATOR INT TO INT PAR_D LLAVE_I contenido LLAVE_D
  | FOR PAR_I VARIABLE ITERATOR INT UNTIL INT PAR_D LLAVE_I contenido LLAVE_D
  | FOR PAR_I VAR VARIABLE ITERATOR INT TO INT PAR_D LLAVE_I contenido LLAVE_D
  | FOR PAR_I VAR VARIABLE ITERATOR INT UNTIL INT PAR_D LLAVE_I contenido LLAVE_D'''
#Condicion if por Juan Pisco
def p_if(p):
  '''if : IF PAR_I condicional PAR_D LLAVE_I contenido LLAVE_D
  | if elseif
  | if else
  '''

def p_elseif(p):
  '''elseif : ELSE IF PAR_I condicional PAR_D LLAVE_I contenido LLAVE_D'''

def p_else(p):
  '''else : ELSE LLAVE_I contenido LLAVE_D
  | elseif else'''

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
  | aritmetica comparacion aritmetica
  | aritmetica comparacion numeros
  | numeros comparacion aritmetica
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

# Expresiones aritmeticas por Juan Pisco
def p_aritmetica(p):
  '''aritmetica : numeros aritmeticos numeros
  | VARIABLE aritmeticos numeros
  | numeros aritmeticos VARIABLE
  | VARIABLE aritmeticos VARIABLE
  | aritmetica aritmeticos numeros
  | aritmetica aritmeticos VARIABLE'''

def p_aritmeticos(p):
  '''aritmeticos : MENOS
  | MAS
  | MULTIPLICACION
  | DIVISION
  | MOD'''

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

probar = '''
def funcion( i:Int = 8) = {
  while(true){
      if(i != 1) {
        println("Hola")
      } else if(i<2) {
        println("F")
      } else {
        readLine()
      }
    readLine() 
    readLine()
  }
  for (var x <- c) {
    println(1)
  } 
  var i:Int = 1
}'''

validaRegla(probar)
while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)
