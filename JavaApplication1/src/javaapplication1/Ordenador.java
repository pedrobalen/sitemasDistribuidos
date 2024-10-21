/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package javaapplication1;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.Arrays;
/**
 *
 * @author laboratorio
 */
public class Ordenador extends UnicastRemoteObject implements IOrdenador {
    
    protected Ordenador() throws RemoteException {
        super();
    }

    @Override
    public int[] ordenar(int[] lista) throws RemoteException {
        Arrays.sort(lista);
        return lista;
    }
}