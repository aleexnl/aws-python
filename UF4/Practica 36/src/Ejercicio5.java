import java.util.Scanner;

public class Ejercicio5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		float grados;
		Scanner lector = new Scanner(System.in);  // Definimos variable para lector de teclado
		
		System.out.println("Introduce los grados a convertir :");
		grados = lector.nextFloat();
		
		System.out.println((grados * 5/9) - 32 + " Cº");
		


	}

}
