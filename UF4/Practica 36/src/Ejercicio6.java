import java.util.Scanner;

/**
 * 
 */

/**
 * @author aleexnl
 *
 */
public class Ejercicio6 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner lector = new Scanner(System.in);
		int num1;
		int num2;
		int resultat;
		System.out.println("Dame un número");
		num1 = lector.nextInt();
		System.out.println("Dame el segundo número:");
		num2 = lector.nextInt();
		
		System.out.println("Behold! Addition!");
		resultat = num1 + num2;
		System.out.println(resultat);
		
		System.out.println("Be amazed! Substraction!");
		resultat = num1 - num2;
		System.out.println(resultat);
		
		System.out.println("Stare in awe! Multiplication!");
		resultat = num1 * num2;
		System.out.println(resultat);
		
		System.out.println("Marvel yourself! Division!");
		resultat = num1 / num2;
		System.out.println(resultat);
		
		
		
	}

}
