package Ejercicio2;

public class Triangle2 extends Figura2 {
    int base;
    int altura;

    void setBase(int base){
        this.base = base;
    }

    void setAltura(int altura){
        this.altura = altura;
    }

    int getBase(){
        return this.base;
    }

    int getAltura(){
        return this.altura;
    }

    Triangle2(int base, int altura){
        super();
        this.base = base;
        this.altura = altura;


    }

    @Override
    void calcularArea() {
        this.area = base * altura / 2;

    }


}
