package Ejercicio3;

public class Persona3 {
    String nom;
    String DNI;
    double edat;
    float altura;
    char sexe;
    boolean casat;

    Persona3(){}
    Persona3(String nom, String DNI, double edat, float altura, char sexe, boolean casat){
        this.nom = nom;
        this.DNI = DNI;
        this.edat = edat;
        this.altura = altura;
        this.sexe = sexe;
        this.casat = casat;
    }

    Persona3(String nom, String DNI, double edat, float altura, char sexe){
        this.nom = nom;
        this.DNI = DNI;
        this.edat = edat;
        this.altura = altura;
        this.sexe = sexe;
        this.casat = false;
    }

    void setNom(String nom){
        this.nom = nom;
    }

    void setDNI(String DNI){
        this.DNI = DNI;
    }

    void setEdat(double edat){
        this.edat = edat;
    }

    void setAltura(float altura){
        this.altura = altura;
    }

    void setSexe(char sexe){
        this.sexe = sexe;
    }

    void setCasat(boolean casat) {
        this.casat = casat;
    }

    String getDNI(){
        return this.DNI;
    }

    double getEdat(){
        return this.edat;
    }

    float getAltura() {
        return this.altura;
    }

    boolean getCasat(){
        return this.casat;
    }

    void getAllInfo(){
        System.out.println(getDNI());
        System.out.println(Double.toString(getEdat()));
        System.out.println(Float.toString(getAltura()));
        System.out.println(Boolean.toString(getCasat()));
    }

}
