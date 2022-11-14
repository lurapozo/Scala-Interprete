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



  def main(args: Array[String]) = {

    print("Ingrese un numero: ")
    val primero = readLine().toInt
    print("Ingrese otro numero: ")


    val segundo = readLine().toInt
    var suma = primero + segundo
    var resta = primero - segundo
    val lista = Array(1.2, 1.0)
    val largo = 100l
    val flotate = 1.2f
    val doble = 1.2
    val entero = 1
    val caracter = 'd'


    if (resta == 0) {
      println()
      println("Los dos numeros que ingreso son iguales")
    } else {
      println() 
      println("Los dos numeros que ingreso son diferentes")
    }

    val tupla: (String , Double) = ingreseConstante("pi")
    
    println(tupla._1 + " " + tupla._2)
  }
}
