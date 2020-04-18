package Ejercicio3;

import java.util.ArrayList;
import java.util.Scanner;

public class Persona3Menu3 {
    ArrayList<Persona3> llistaPersones;
    Scanner sc = new Scanner(System.in);
    boolean sortir;
    boolean sortir1;
    int intOpcio;
    double opció;
    float floatOpcio;
    String strOpcio;
    char charOpcio;


    Persona3Menu3() {
        llistaPersones = new ArrayList<Persona3>();
        sortir = false;
        sortir1 = false;
    }


    public void menu() {
        do{
        System.out.println("Introdueix una opció: "
                + "\n\t1. Afegir una persona" + "\n\t2.Mostrar la llista de persones "
                + "\n\t3.Eliminar una persona introduïda" + "\n\t4. Sortir");

            if (sc.hasNextInt()) {
                intOpcio = sc.nextInt();
                executeOpcio(intOpcio);

            } else {
                System.out.println("Introdueix un valor o format correcte...");
                sc.nextLine();
            }

        } while (sortir == false);

    }

    public void executeOpcio(int intOpcio) {
        switch (intOpcio) {
            case 1:
                primeraOpcio();
                break;
            case 2:
                segonaOpcio();
                break;
            case 3:
                terceraOpcio();
                break;
            case 4:
                System.out.println("Bye, bye, baby...");
                sortir = true;
        }
    }

    public void primeraOpcio() {
        Persona3 p = new Persona3();

        System.out.println("Dona'm el DNI");
        do {
            if (sc.hasNextLine()) {
                strOpcio = sc.nextLine();
                p.setDNI(strOpcio);
                sortir = true;
            } else {
                System.out.println("Introdueix un valor o format correcte...");
                sc.nextLine();
            }

        } while (sortir1 == false);

        sortir1 = false;

        System.out.println("Dona'm l'edat");
        do {
            if (sc.hasNextInt()) {
                opció = sc.nextInt();
                p.setEdat(opció);
                sortir = true;
            } else {
                System.out.println("Introdueix un valor o format correcte...");
                sc.nextLine();
            }

        } while (sortir1 == false);

        sortir1 = false;

        System.out.println("Dona'm l'alçada");
        do {
            if (sc.hasNextInt()) {
                floatOpcio = sc.nextInt();
                p.setAltura(floatOpcio);
                sortir = true;
            } else {
                System.out.println("Introdueix un valor o format correcte...");
                sc.nextLine();
            }

        } while (sortir1 == false);

        sortir1 = false;

        System.out.println("Dona'm el sexe [h/d]");
        do {
            if (sc.hasNextLine()) {
                charOpcio = sc.next().charAt(0);
                if (charOpcio == 'h' || charOpcio == 'd') {
                    p.setSexe(charOpcio);
                    sc.nextLine();
                    sortir = true;
                } else {
                    charOpcio = ' ';
                    sc.nextLine();
                }
            } else {
                System.out.println("Introdueix un valor o format correcte...");
                sc.nextLine();
            }

        } while (sortir1 == false);

        sortir1 = false;

        System.out.println("Està casat/da? [s/n]");
        do {
            if (sc.hasNextLine()) {
                charOpcio = sc.next().charAt(0);
                if (charOpcio == 's') {
                    p.setCasat(true);
                    sc.nextLine();
                    sortir = true;
                } else if (charOpcio == 'n') {
                    p.setCasat(false);
                    sc.nextLine();
                    sortir = true;
                } else {
                    charOpcio = ' ';
                    sc.nextLine();
                }
            } else {
                System.out.println("Introdueix un valor o format correcte...");
                sc.nextLine();
            }

        } while (sortir1 == false);

        llistaPersones.add(p);
    }

    public void segonaOpcio() {
        System.out.println("Aquestes son les persones afegides fins ara:");
        for (Persona3 item : llistaPersones
        ) {
            int numeral = 1;
            System.out.println(Integer.toString(numeral) + "a" + " persona:");
            item.getAllInfo();
        }

    }

    public void terceraOpcio() {
        System.out.println("Introdueix el DNI complet que identifica la persona que vols eliminar: ");
        do {
            if (sc.hasNextLine()) {
                strOpcio = sc.next();
                sc.nextLine();
                for (Persona3 persona: llistaPersones
                     ) {
                    if (persona.getDNI().equalsIgnoreCase(strOpcio)){
                        llistaPersones.remove(persona);
                    }
                    else {
                        System.out.println("No s'ha trobat a una persona amb aquest DNI...");
                    }
                }
                sortir = true;

            } else {
                System.out.println("Introdueix un valor o format correcte...");
                sc.nextLine();
            }

        } while (sortir == false);

    }
}


