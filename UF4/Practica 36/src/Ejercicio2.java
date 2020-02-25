import java.util.Scanner;

public class Ejercicio2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner lector = new Scanner(System.in);  // Definimos variable para lector de teclado
		String nombre = "";
		int numero_uno = 0;
		int numero_dos = 0;
		// a)
		System.out.println("¿Cual es tu nombre? ");  // Mostrar mensaje
		nombre = lector.nextLine();  // Asignar valor a variable del buffer de entrada
		System.out.println("¡Hola " + nombre + "!");  // Mostrar mensaje mas resultado
		// b)
		System.out.println("Introduce el primer numero: ");
		numero_uno = lector.nextInt();
		System.out.println("Introduce el segundo numero: ");
		numero_dos = lector.nextInt();
		System.out.println("Resultado del producto: " + numero_uno*numero_dos);  // Mostrar mensaje mas resultado
	}

}
