package Ejercicio1;

import java.util.Scanner;

public class Producte {
    int codi;
    String nom;
    String tipus;
    double preu;
    int stock;
    Scanner lector = new Scanner(System.in);
    public Producte(int codi, String nom, String tipus, double preu, int stock) { // Constructor para el objeto Producto
        this.codi = codi;
        this.nom = nom;
        this.tipus = tipus;
        this.preu = preu;
        this.stock = stock;
    }

    public void getProducte() { // Mostrar toda la info del producto con formato
        System.out.println("Codi: " + this.codi);
        System.out.println("Nom: " + this.nom);
        System.out.println("Tipus: " + this.tipus);
        System.out.println("Preu: " + this.preu + " $");
        System.out.println("Stock: " + this.stock + " Unidad(es)");
    }

    public int getStock() {
        return stock;
    }

    public int getCodi() {
        return codi;
    }

    public String getNom() {
        return nom;
    }

    public String getTipus() {
        return tipus;
    }

    public void setPreu(double preu) {
        this.preu = preu;
    }

    public double getPreu() {
        return preu;
    }
}
