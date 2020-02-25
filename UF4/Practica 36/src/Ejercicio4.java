import java.util.Scanner;

public class Ejercicio4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		float qty_money;
		float int_rate;
		int num_year;
		Scanner lector = new Scanner(System.in);  // Definimos variable para lector de teclado


		System.out.println("Introduce cantidad de dinero :");  // Mostrar mensaje
		qty_money = lector.nextFloat();  // Asignar valor a variable del buffer de entrada

		System.out.println("Introduce los intereses :");
		int_rate = lector.nextFloat();

		System.out.println("Introduce los años :");
		num_year = lector.nextInt();

		System.out.println("Diners a pagar: " + qty_money * Math.pow((int_rate/100), num_year)); // Mostrar mensaje mas resultado
	}

}
