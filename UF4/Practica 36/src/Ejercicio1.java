import java.util.Scanner;

public class Ejercicio1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		@SuppressWarnings("resource")
		Scanner lector = new Scanner(System.in);  // Definimos variable para lector de teclado
		System.out.print("Introduce un numero para calcular el cuadrado de este: ");  // Mostramos mensaje
		int numero = lector.nextInt();  // Asignaos el valor introducido por teclado a la variable
		int resultat = numero*numero;  // Hacemos el calculo de el cuadrado y lo guardamos en una variable
		System.out.println("El cuadrado de " + numero + " es: " + resultat);  // Mostramos resultado con numero personalizado
		
	}

}
