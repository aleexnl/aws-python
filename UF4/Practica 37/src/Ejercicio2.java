import java.util.Scanner;

public class Ejercicio2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] alumnes = new String[10]; // Definimos un array con 10 posiciones.
		Scanner lector = new Scanner(System.in); // Definimos un scanner.
		int contador_elementos = 0;
		String alumno;
		
		System.out.println("Introduce 10 nombres: ");
		while (contador_elementos < 10) { // Este while irá iterando hasta que se hayan introducido 10 elementos.
			System.out.println("Nombre numero " + (contador_elementos + 1) + ": ");
			alumno = lector.nextLine();
			// Esto se supone que comprueba si lo introducido existe pero por cosas de la vida no va.
//			for (int i = 0; i < alumnes.length; i++) { // Este for itera con cada posición de la lista y la muestra.
//				  if (alumno == alumnes[i]) {
//					  System.out.println(alumno + "ya existe en la lista");
//				  };
//				};
			alumnes[contador_elementos] = alumno;
			contador_elementos ++;
		};
		
		System.out.println("Alumnos: ");
		for (int i = 0; i < alumnes.length; i++) { // Este for itera con cada posición de la lista y la muestra.
			  System.out.println(alumnes[i]);
			};
	}

}
