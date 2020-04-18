package Ejercicio2;

public abstract class Figura2 {

    String color;
    double area;


    public Figura2() {

    }

    void setArea (double area) {
        this.area = area;
    }

    void setColor (String color) {
        this.color = color;
    }

    double getArea() {
        return this.area;
    }

    String getColor(){
        return this.color;
    }

    abstract void calcularArea ();

}
