/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package javaapplication1;
import java.rmi.*;
import java.rmi.registry.*;
/**
 *
 * @author laboratorio
 */

public class Server {

    private static final String HOST_URL = "rmi://localhost/Ordenador";

    public Server() {
        try {
            LocateRegistry.createRegistry(Registry.REGISTRY_PORT);
            IOrdenador ordenador = new Ordenador();
            Naming.bind(HOST_URL, ordenador);
            System.out.println("Servidor online esperando clientes...");
        } catch (Exception e) {
            System.out.println("Erro: " + e);
        }
    }

    public static void main(String[] args) {
        new Server();
    }
}