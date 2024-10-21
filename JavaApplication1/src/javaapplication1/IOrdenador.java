    /*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package javaapplication1;

import java.rmi.*;
/**
 *
 * @author laboratorio
 */
interface IOrdenador extends Remote {
    int[] ordenar(int[] lista) throws RemoteException;
}