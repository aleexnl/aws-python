package Ejercicio1;

import java.util.ArrayList;

public class ArrayProducte{
    int contadorProductos = 1; // Contador de productos
    ArrayList<Producte> llistaProductes = new ArrayList<Producte>();

    public void agregar(int codi, String nom, String tipus, double preu, int stock) { // Agregar producto al array
        llistaProductes.add(new Producte(codi, nom, tipus, preu, stock));
    }

    public void grandaria() { // Muestra todos los productos del  Array con contador
        contadorProductos = 1;
        for (Producte producto : llistaProductes) {
            System.out.println("Producto Nº: " + contadorProductos);
            producto.getProducte();
            contadorProductos++;
        }
    }
    public boolean buscar(int codi, String nom) { // Comprueba si hay productos con ese codigo o nombre
        for (Producte producto : llistaProductes) {
            if (codi == producto.getCodi()) {
                System.out.println("ERROR: Ya existe un producto con ese codigo");
                return false;
            }
            if (nom.equals(producto.getNom())) {
                System.out.println("ERROR: Ya existe un producto con ese nombre");
                return false;
            }
        }
        return true; // Si ninguno esta repetido devuelve true y continua
    }

    public void eliminar() {// Itera por la lista y si hay un elemento sin stock lo elimina
        llistaProductes.removeIf(producto -> producto.getStock() == 0);
    }

    public void obtenir() { // Augmenta un 10% el precio si el tipo es igual al de oficina
        for (Producte producto : llistaProductes) {
            if (producto.getTipus().equals("oficina")) {
                producto.setPreu(producto.getPreu() * 1.10);
            }
        }
    }
}
