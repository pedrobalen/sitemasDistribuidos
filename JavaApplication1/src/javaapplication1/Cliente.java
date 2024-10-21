/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package javaapplication1;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;
/**
 *
 * @author laboratorio
 */
public class Cliente {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            IOrdenador ordenador = (IOrdenador) registry.lookup("Ordenador");

            Scanner scanner = new Scanner(System.in);
            System.out.println("Digite os numeros a serem ordenados (separados por espaço):");
            String input = scanner.nextLine();
            String[] partes = input.split(" ");
            int[] lista = new int[partes.length];
            for (int i = 0; i < partes.length; i++) {
                lista[i] = Integer.parseInt(partes[i]);
            }

            int[] listaOrdenada = ordenador.ordenar(lista);
            System.out.println("Lista ordenada:");
            for (int num : listaOrdenada) {
                System.out.print(num + " ");
            }
            System.out.println();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
}
