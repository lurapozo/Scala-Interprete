from ply.yacc import *
from ply.lex import *
from lexen import tokens

#Crear las siguientes reglas

def p_inicio(p):
  ''' inicio : OBJECT VARIABLE LLAVE_I cuerpo LLAVE_D
  | IMPORT io inicio'''

def p_io(p):
  ''' io : VARIABLE PUNTO VARIABLE PUNTO VARIABLE PUNTO READLINE'''
# Cuerpo
def p_cuerpo(p):
  '''cuerpo : funcion
  | funcall
  | impresion
  | entrada
  | asignacion
  | while
  | for
  | match
  | if
  | funcion cuerpo
  | asignacion cuerpo
  | while cuerpo
  | for cuerpo
  | if cuerpo
  | match cuerpo'''

# Contenido de Funciones y de estructuras de control
def p_contenido(p):
  '''contenido : asignacion
  | reasignacion
  | funcall
  | impresion
  | entrada
  | while
  | for
  | match
  | if
  | aritmetica
  | asignacion contenido
  | reasignacion contenido
  | funcall contenido
  | impresion contenido
  | entrada contenido
  | while contenido
  | for contenido
  | if contenido
  | match contenido
  | aritmetica contenido'''

# Contendio para estrcutra match de una lienea 
def p_contenidoLine(p):
  '''contenidoLine : asignacion
  | reasignacion
  | funcall
  | impresion
  | entrada'''

# Asignacion realizada por: Ramos Pozo
def p_asignacion(p):
  '''asignacion : VAR VARIABLE IGUAL VARIABLE
  | VAL VARIABLE IGUAL VARIABLE
  | VAR VARIABLE IGUAL aritmetica
  | VAL VARIABLE IGUAL aritmetica
  | VAR VARIABLE IGUAL returnfun
  | VAL VARIABLE IGUAL returnfun
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

# Reasignacion de valor a variable por Gabriel Maldonado
def p_reasignacion(p):
  '''reasignacion :  VARIABLE IGUAL valor
      | VARIABLE IGUAL returnfun
      | VARIABLE IGUAL aritmetica
      | VARIABLE PAR_I INT PAR_D IGUAL valor'''
# Tipos de Datos realizado por: Ramos Pozo
def p_tipo(p):
  '''tipo : CHARCLASS
  | STRINGCLASS
  | BOOLCLASS
  | INTCLASS
  | LONGCLASS
  | DOUBLECLASS
  | FLOATCLASS
  | ARRAYCLASS CORCHETE_I tipo CORCHETE_D
  | LISTCLASS CORCHETE_I tipo CORCHETE_D'''

def p_valor(p):
  '''valor : STRING
  | CHAR
  | VARIABLE
  | numeros
  | booleanos
  | VARIABLE PAR_I VARIABLE PAR_D
  | VARIABLE PAR_I INT PAR_D'''

def p_booleanos(p):
  '''booleanos : TRUE
  | FLASE'''

def p_numeros(p):
  '''numeros : INT
  | LONG
  | FLOAT
  | DOUBLE'''


# Funciones sin retorno por Juan Pisco
def p_funcion(p):
  '''funcion : DEF VARIABLE parametro IGUAL LLAVE_I contenido LLAVE_D
  | DEF VARIABLE parametro LLAVE_I contenido LLAVE_D'''


# Funciones con valores por defecto realizada por: Ramos Pozo
def p_declaracion(p):
  '''declaracion : VARIABLE DOBLE_PUNTO tipo'''

def p_declaracion_defecto(p):
  '''declaracion :  VARIABLE DOBLE_PUNTO tipo IGUAL valor '''

def p_parametro(p):
  '''parametro : parametros
  | PAR_I PAR_D '''

def p_parametros(p):
  '''parametros : PAR_I declaracion PAR_D 
    | PAR_I declaracion PAR_D parametros'''


#Funcion con retorno realizada por Gabriel Maldonado
def p_funcion_return(p):
  '''funcion : DEF VARIABLE  parametro  dectipo IGUAL LLAVE_I contenido RETURN valor LLAVE_D 
    | DEF VARIABLE  parametro  dectipo IGUAL LLAVE_I contenido RETURN VARIABLE LLAVE_D
    | DEF VARIABLE  parametro  dectipo IGUAL LLAVE_I contenido RETURN returnfun LLAVE_D
    | DEF VARIABLE  parametro  dectipo IGUAL LLAVE_I contenido RETURN aritmetica LLAVE_D'''

def p_funcion_return_vacia(p):
  '''funcion : DEF VARIABLE  parametro  dectipo IGUAL LLAVE_I RETURN valor LLAVE_D 
    | DEF VARIABLE  parametro  dectipo IGUAL LLAVE_I RETURN VARIABLE LLAVE_D
    | DEF VARIABLE  parametro  dectipo IGUAL LLAVE_I RETURN returnfun LLAVE_D
    | DEF VARIABLE  parametro  dectipo IGUAL LLAVE_I RETURN aritmetica LLAVE_D'''

def p_funcion_returnTupla(p):
  '''funcion : DEF VARIABLE  parametro  dectipoTupla IGUAL LLAVE_I contenido RETURN tuple LLAVE_D
      | DEF VARIABLE  parametro  dectipoTupla IGUAL LLAVE_I contenido RETURN VARIABLE LLAVE_D 
      | DEF VARIABLE  parametro  dectipoTupla IGUAL LLAVE_I contenido RETURN returnfun LLAVE_D'''

def p_dectipo(p):
  '''dectipo : DOBLE_PUNTO tipo '''

def p_dectipoTupla(p):
  '''dectipoTupla : DOBLE_PUNTO PAR_I tipos PAR_D'''

def p_tipos(p):
  '''tipos : tipo
    | tipo tiposentry'''

def p_tipoentry(p):
  '''tiposentry : COMA tipo 
  | COMA tipo tiposentry'''


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

#Llamadas a funciones por : Gabriel Maldonado
def p_funcall(p):
  '''funcall : VARIABLE varparen'''

def p_varparen(p):
  ''' varparen : PAR_I valores PAR_D
  | PAR_I PAR_D
  | varparen PAR_I valores PAR_D
  | varparen PAR_I PAR_D'''

def p_returnfun(p):
  ''' returnfun : returnCastable
      | castingcall'''

def p_returnCastable(p):
  '''returnCastable : entrada
      | funcall'''
  
# Funciones casting por : Gabriel Maldonado

def p_castingcall(p):
  '''castingcall : returnCastable PUNTO castingfun
      | VARIABLE PUNTO castingfun'''


def p_castingfun(p):
  '''castingfun : TO_INT
    | TO_DOUBLE
    | TO_FLOAT
    | TO_LONG'''

# Estructura de Datos
#Array realizado por: Ramos Pozo
def p_array(p):
  '''array : VAR VARIABLE IGUAL ARRAYCLASS PAR_I valores PAR_D
  | VAR VARIABLE DOBLE_PUNTO ARRAYCLASS CORCHETE_I tipo CORCHETE_D IGUAL ARRAYCLASS PAR_I valores PAR_D
  | VAR VARIABLE DOBLE_PUNTO ARRAYCLASS CORCHETE_I tipo CORCHETE_D IGUAL NEW ARRAYCLASS CORCHETE_I tipo CORCHETE_D PAR_I INT PAR_D
  | VAL VARIABLE IGUAL ARRAYCLASS PAR_I valores PAR_D
  | VAL VARIABLE DOBLE_PUNTO ARRAYCLASS CORCHETE_I tipo CORCHETE_D IGUAL ARRAYCLASS PAR_I valores PAR_D
  | VAL VARIABLE DOBLE_PUNTO ARRAYCLASS CORCHETE_I tipo CORCHETE_D IGUAL NEW ARRAYCLASS CORCHETE_I tipo CORCHETE_D PAR_I INT PAR_D'''

# List por Juan Pisco
def p_list(p):
  '''list : VAL VARIABLE IGUAL LISTCLASS PAR_I valores PAR_D
  | VAL VARIABLE DOBLE_PUNTO LISTCLASS CORCHETE_I tipo CORCHETE_D IGUAL NEW LISTCLASS PAR_I valores PAR_D
  | VAL VARIABLE DOBLE_PUNTO LISTCLASS CORCHETE_I tipo CORCHETE_D IGUAL LISTCLASS PAR_I valores PAR_D'''


def p_valores(p):
  '''valores : valor
  | valor COMA valores'''

# Tuple por Gabriel Maldonado
def p_tuple(p): 
  '''tuple : PAR_I valores PAR_D'''

def p_asignacion_tuple(p):
  '''asignacion : VAR VARIABLE IGUAL tuple 
      | VAL VARIABLE IGUAL tuple'''

def p_asignacion_tupleDec(p):
  '''asignacion : VAR VARIABLE dectipoTupla IGUAL tuple 
      | VAL VARIABLE dectipoTupla IGUAL tuple'''

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

# Match por Gabriel Maldonado
def p_match(p):
  '''match : VARIABLE MATCH  LLAVE_I cases LLAVE_D'''

def p_cases(p):
  '''cases : casesInt
    | casesLgn
    | casesFlt
    | casesDob
    | casesStr
    | casesChar
    | casesBool'''

def p_caseInt(p):
  '''caseInt : CASE INT FUNCION_FLECHA codeBlock'''

def p_casesInt(p):
  ''' casesInt : caseInt 
      | caseInt casesInt
      | caseInt defcase'''

def p_caseLgn(p):
  '''caseLgn : CASE LONG FUNCION_FLECHA codeBlock'''

def p_casesLgn(p):
  ''' casesLgn : caseLgn 
      | caseLgn casesLgn
      | caseLgn defcase'''

def p_caseFlt(p):
  '''caseFlt : CASE FLOAT FUNCION_FLECHA codeBlock'''

def p_casesFlt(p):
  ''' casesFlt : caseFlt 
      | caseFlt casesFlt
      | caseFlt defcase'''

def p_caseDob(p):
  '''caseDob : CASE DOUBLE FUNCION_FLECHA codeBlock'''

def p_casesDob(p):
  ''' casesDob : caseDob 
      | caseDob casesDob
      | caseDob defcase'''

def p_caseStr(p):
  '''caseStr : CASE STRING FUNCION_FLECHA codeBlock'''

def p_casesStr(p):
  ''' casesStr : caseStr
      | caseStr casesStr
      | caseStr defcase'''

def p_caseChar(p):
  '''caseChar : CASE CHAR FUNCION_FLECHA codeBlock'''

def p_casesChar(p):
  ''' casesChar : caseChar
      | caseChar casesChar
      | caseChar defcase'''

def p_caseBool(p):
  '''caseBool : CASE booleanos FUNCION_FLECHA codeBlock'''

def p_casesBool(p):
  ''' casesBool : caseBool
      | caseBool casesBool
      | caseBool defcase'''


def p_defcase(p):
  '''defcase : CASE SUBGUION FUNCION_FLECHA codeBlock'''

def p_codeBlock(p):
  ''' codeBlock : contenidoLine
      | LLAVE_I contenido LLAVE_D'''

#Condicion if por Juan Pisco
def p_if(p):
  '''if : IF PAR_I condicional PAR_D LLAVE_I contenido LLAVE_D
  | if elseif
  | if else
  '''

def p_elseif(p):
  '''elseif : ELSE IF PAR_I condicional PAR_D LLAVE_I contenido LLAVE_D
  | ELSE IF PAR_I condicional PAR_D LLAVE_I contenido LLAVE_D elseif'''

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


output = ""

def p_error(p):

  global output

  if p:
    print(
      f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    )
    
    output += f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos} \n"

    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
    output += "Error de sintaxis Fin de Linea \n"


# Build the parser
parser = yacc()

def prosesarSintax(data):
  global parser
  global output

  result = parser.parse(data)

  #Output guardado en log.txt
  log = open("log.txt", "a")
  log.write("\nFecha yyyy/mm/dd\n")
  log.write(output)
  log.write('\n--------------------------------------------------\n')
  log.close()
  return output + str(result)



file = open("source.scala")
archivo = file.read()
file.close()
print( parser.parse(archivo))
print('--------------------------------------------------')
