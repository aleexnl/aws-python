import java.util.Scanner;;

public class Ejercicio3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int b = 0;
		int h = 0;
		boolean sortir = false;
		Scanner lector = new Scanner(System.in);


		do {
			do {
				System.out.println("Dame b");

				if (lector.hasNextInt()){
					b = lector.nextInt();
					sortir = true;

				} else {
					System.out.println("Error");

				}
			} while (!sortir);
			
			sortir = false;


			do {
				System.out.println("Dame h");

				if (lector.hasNextInt()){
					h = lector.nextInt();
					sortir = true;
				}

				else {
					System.out.println("Error");
				}
			} while(!sortir);



		} while(!sortir);


		System.out.println(perimeter(b, h));
		System.out.println(area(b, h));
		
		
	}

	public static float perimeter(int b, int h) {
		float perimeter = 2 * b + 2 * h;
		return perimeter;

	}

	public static float area(int b, int h) {
		int area = b * h;
		return area;

	}

}
