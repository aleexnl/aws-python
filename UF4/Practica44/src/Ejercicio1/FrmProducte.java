package Ejercicio1;

import java.util.Scanner;

public class FrmProducte {

    public static void main(String[] args) {
        int codi;
        String nom;
        String tipus;
        double preu;
        int stock;
        int opcion;
        boolean salir =  false;
        Scanner lector = new Scanner(System.in);
        ArrayProducte lista = new ArrayProducte();


        do { // Bulce infinito hasta que el usuario presione salir
            System.out.println("MENU"); // Opciones de menu
            System.out.println("");
            System.out.println("1.\tAñadir productos.");
            System.out.println("2.\tAumentar precio en 10% productos oficina.");
            System.out.println("3.\tEliminar productos sin stock.");
            System.out.println("4.\tMostrar productos.");
            System.out.println("5.\tSalir.");
            do { // Bucle que se ejecuta hasta que se introduce un numero
                System.out.println("escoge una opción: ");
                while (!lector.hasNextInt()) {
                    System.out.println("ERROR: ¡Introduce un número!");
                    lector.next(); // this is important!
                }
                opcion = lector.nextInt();
            } while (opcion <= 0);
            if (opcion == 1) {
                // Coger codigo de producto desde input (con validación)
                System.out.println("Introduce codigo del producto: ");
                while (!lector.hasNextInt()) {
                    System.out.println("ERROR: ¡Introduce un número!");
                    lector.next(); // this is important!
                }
                codi = lector.nextInt();
                lector.nextLine();
                // Coger nombre de producto desde input
                System.out.println("Introduce nombre del producto: ");
                nom = lector.nextLine();
                nom = nom.toLowerCase(); // convertir texto a minusculas
                if (!lista.buscar(codi, nom)) {//Buscar si existe un producto con ese codigo o nombre
                    continue; //Si existe salta a la proxima iteración del while
                }
                // Coger tipo de producto desde input
                System.out.println("Introduce tipo del producto: ");
                tipus = lector.nextLine();
                tipus = tipus.toLowerCase(); // convertir texto a minusculas
                // Coger precio de producto desde input (con validación)
                System.out.println("Introduce precio del producto: ");
                while (!lector.hasNextDouble()) {
                    System.out.println("ERROR: ¡Introduce un número!");
                    lector.next(); // this is important!
                }
                preu = lector.nextDouble();
                lector.nextLine();
                // Coger stock de producto desde input (con validación)
                System.out.println("Introduce stock del producto: ");
                while (!lector.hasNextInt()) {
                    System.out.println("ERROR: ¡Introduce un número!");
                    lector.next(); // this is important!
                }
                stock = lector.nextInt();
                lector.nextLine();
                lista.agregar(codi, nom, tipus, preu, stock);
            } else if (opcion == 2) {
                lista.obtenir();
            } else if (opcion == 3) {
                lista.eliminar();
            } else if (opcion == 4) {
                lista.grandaria();
            } else if (opcion == 5) {
                System.out.println("INFO: Saliendo del programa...");
                salir = true;
            } else {
                System.out.println("ERROR: Opción no encontrada...");
            }
        } while (!salir);
    }
}
