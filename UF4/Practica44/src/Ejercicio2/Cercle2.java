package Ejercicio2;

public class Cercle2 extends Figura2 {

    double radi;

    Cercle2(double radi){
        super();
        this.radi = radi;
    };

    @Override
    void calcularArea() {
        this.area = Math.PI * (radi*radi);
    }
}
