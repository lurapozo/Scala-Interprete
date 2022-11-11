import scala.io.StdIn.readLine
//Lenguaje usado: Scala 2.13
object lexer {

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
  }
}
