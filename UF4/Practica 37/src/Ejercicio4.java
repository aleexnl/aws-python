
import java.util.Scanner;

public class Ejercicio4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Float[] numeros = new Float[10]; // Definimos un array de floats con 10 posiciones.
		Scanner lector = new Scanner(System.in); // Definimos un scanner.
		int contador_elementos = 0;
		Float numero;
		
		System.out.println("Introduce 10 numeros decimales: ");
		while (contador_elementos < 10) { // Este while irá iterando hasta que se hayan introducido 10 elementos.
			System.out.println("Numero " + (contador_elementos + 1) + ": ");
			numero = lector.nextFloat();
			for (int i = 0; i < numeros.length; i++) { // Este for itera con cada posición de la lista y la muestra.
			  if (numero == numeros[i]) {
				  System.out.println(numero + "ya existe en la lista");
				  while (numero == numeros[i]) {
						System.out.println("Introduce un numero no repetido");
						numero = lector.nextFloat();  
				  }
			  };
			};
			numeros[contador_elementos] = numero;
			contador_elementos ++;
		};
		
		System.out.println("numeros: ");
		for (int i = 0; i < numeros.length; i++) { // Este for itera con cada posición de la lista y la muestra.
			  System.out.println(numeros[i]);
			};
	}

}

