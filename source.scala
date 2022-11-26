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

    
    val opt = readLine().toInt

    opt match{
      case 1 => value = value.toInt
      case 2 =>  value = value.toLong
      case 3 =>  value = value.toFloat
      case 4 =>  value = value.toDouble
    }

    val tupla: (String , Double) = ("Hola" , 5.5)

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
    //var arreglo2 = arreglo.reverse
    while (i<3) {
      println("Arreglo creado en posicion "+ i + " = " + arreglo2(i))
      i = i + 1
    }
  }
  //Algoritmo realizado por Pisco Jordan
  def funcionPisco() {
    val lista:List[String] = List("primero","segundo","tercero")
    val otraLista = List(1,2,3)
    println("Imprimiendo lista")
    for (i <- lista) {
      println(i)
    }
    print("Ingrese 1 numero: ")
    var primero = readLine().toInt
    print("Ingrese otro numero: ")
    var segundo = readLine().toInt
    var suma = primero + segundo
    var multi = primero * segundo
    var divi = primero / segundo
    var resta = primero - segundo
    if(primero == segundo){
      println("Los numeros ingresados son iguales!")
    }
    else if(primero > segundo){
      println("El primer numero es mayor que el segundo!")
    }
    else if(primero < segundo){
      println("El primer numero es menor que el segundo!")
    }

    if (suma % 2 != 0){
      println("La suma de ambos valores da un valor impar")
    }
    else {
      println("La suma de ambos valores da un valor par")
    }

  }

  def main(args: Array[String]) = {
    val lista = Array(1.2, 1.0)
    val largo = 100l
    val flotate = 1.2f
    val doble = 1.2
    val entero = 1
    val caracter = 'd'

    val tupla = ingreseConstante("pi")
    
    //println(tupla._1 + " " + tupla._2)
    funcionDeArreglos()
    funcionPisco()
  }
}