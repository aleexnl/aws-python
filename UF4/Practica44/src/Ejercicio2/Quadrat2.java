package Ejercicio2;

public class Quadrat2 extends Figura2 {
    int costat;

    void setCostat(int costat){
        this.costat = costat;
    }

    int getCostat (){
        return this.costat;
    }

    Quadrat2(int costat){
        super();
        this.costat = costat;
    }

    @Override
    void calcularArea () {
        this.area = costat * costat;
    };
}
