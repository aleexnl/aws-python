package Ejercicio2;

import java.util.ArrayList;

public class FrmFigures {


    public static void main(String[] args) {
        ArrayList<Figura2> llistaFigures = new ArrayList<>(10);
        llistaFigures.ensureCapacity(10);
        int numQuadrats = 0;
        int numTriangles = 0;
        int numCercles = 0;
        double arees = 0;

        Cercle2 cercle1 = new Cercle2(17);
        Cercle2 cercle2 = new Cercle2(15.3);
        Quadrat2 quadrat1 = new Quadrat2(3);
        Quadrat2 quadrat2 = new Quadrat2(7);
        Quadrat2 quadrat3 = new Quadrat2(5);
        Triangle2 triangle1 = new Triangle2(2, 3);

        llistaFigures.add(cercle1);
        llistaFigures.add(cercle2);
        llistaFigures.add(quadrat1);
        llistaFigures.add(quadrat2);
        llistaFigures.add(quadrat3);
        llistaFigures.add(triangle1);

        for (Figura2 item: llistaFigures
             ) {
                item.calcularArea();
                arees += item.getArea();
        }

        System.out.println("El total d'àrees és " +  Double.toString(arees));

        for (Figura2 item: llistaFigures
             ) {
                if (item instanceof Cercle2) {
                    numCercles += 1;
                }

                else if (item instanceof Quadrat2){
                    numQuadrats += 1;
                }

                else if (item instanceof Triangle2) {
                    numTriangles += 1;
                }

                else {
                    System.out.println("Yo, there ain't no known figures here.");
                }
        }

        System.out.println("Nombre de cercles, quadrats i triangles: " + Integer.toString(numCercles)
                + " " + Integer.toString(numQuadrats) + " " + Integer.toString(numTriangles));



    }
}
