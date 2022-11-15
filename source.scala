import scala.io.StdIn.readLine
//Lenguaje usado: Scala 2.13
object lexer {

  //Algoritmo Gabriel Maldonado
  def ingreseConstante(constante:String) : (String , Double) = {

    print("Ingrese constante: ")
    var value = readLine().toDouble

    println("Escoja el tipo de numero al que persenese la constante: ")
    println("1.Int ")
    println("2.Long ")
    println("3. Float")
    println("4. Double")
    print("Opcion:  ")
    val opt:Int = readLine().toInt

    opt match{
      case 1 => value.toInt
      case 2 => value.toLong
      case 3 => value.toFloat
      case 4 => value.toDouble
    }

    val tupla: (String , Double) = (constante , value)

    return tupla

  }

  //Algoritmos hecho por Ramos Pozo
  def suma (x: Int = 6)(y: Int = 7): Int = {
    return x + y
  }
  def funcionDeArreglos() = {
    print("Ingrese un numero: ")
    val primero = readLine().toInt
    var sum = suma(primero)()
    println("Numero ingresado + 7 = "  + sum)
    var arreglo:Array[Int] = Array(1,2,3)
    var array:Array[String] = new Array[String](1)
    array(0) = "hola"
    arreglo(1) = 4
    var i = 0
    var arreglo2 = arreglo.reverse
    while (i<3) {
      println("Arreglo creado en posicion "+ i + " = " + arreglo2(i))
      i = i + 1
    }
  }

  def main(args: Array[String]) = {
    val lista = Array(1.2, 1.0)
    val largo = 100l
    val flotate = 1.2f
    val doble = 1.2
    val entero = 1
    val caracter = 'd'

    val tupla: (String , Double) = ingreseConstante("pi")
    
    println(tupla._1 + " " + tupla._2)
    funcionDeArreglos()
  }
}
