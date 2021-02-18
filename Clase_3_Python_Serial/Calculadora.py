#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# Definicion de Funciones suma-resta-producto-division
def suma(op1,op2):
    return (op1+op2)
def resta(op3,op4):
    return(op3-op4)
def producto(op5,op6):
    return(op5*op6)
def division(op7,op8):
    return(op7/op8)
# Funcion de ingreso 
def ing():
    a =float(input('Ingrese primer numero'))
    b =float(input('Ingrese segundo numero'))
    return(a,b)
#Ingreso de las dimensiones de las matrices
def ingmxn():
    print('Ingresa el orden de su Matriz 1:Filas y Columnas')
    filas1,columnas1 = int(input()),int(input())
    print('Ingresa el orden de su Matriz 2:Filas y Columnas')
    filas2,columnas2 = int(input()),int(input())
    return(filas1,columnas1,filas2,columnas2)
#Producto de Matrices
def matriz():
    filas1,columnas1,filas2,columnas2 =ingmxn() 
    while(columnas1!=filas2):
        print('El numero de columnas de su Matriz1 debe ser iguala al numero de filas de su Matriz2')
        filas1,columnas1,filas2,columnas2 =ingmxn()
        
    if(columnas1==filas2):
        matriz1 = np.zeros((filas1,columnas1))
        matriz2 = np.zeros((filas2,columnas2))
        print ('Ingrese su Matriz 1')
        for i in range(filas1):
            for j in range(columnas1):
                matriz1[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))
        print ('Ingrese su Matriz 2')
        for i in range(filas2):
            for j in range(columnas2):
                matriz2[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))

    print (np.dot(matriz1,matriz2))
    
    return()


# In[5]:


def calculadora():
    print('Elija una opcion')
    print('1-Suma ')
    print('2-Resta')
    print('3-Multiplicacion')
    print('4-Division')
    print('5-Iterator')
    print('6-Producto de MAtrices')
    s='si'
    while('si' in s):
        x =input('Eliga la operacion que desea realizar')
        y=int(x)
        if(y==1):
            a,b=ing()
            resultado=suma(a,b)
            print(resultado)
            
        elif(y==2):
            a,b=ing()
            resultado=resta(a,b)
            print(resultado)
        elif(y==3):
            a,b=ing()
            resultado=producto(a,b)
            print(resultado)
        elif(y==4):
            a,b=ing()
            resultado=division(a,b)
            print(resultado)
        elif(y==5):
            a,b=ing()
            c=input('Elija operacion')
            y=float(0)
            d=int(b)
            if('a'in c):
                for i in range(d):
                    y=suma(y,a)
                print(y)
            elif('b'in c):
                for i in range(d):
                    y=resta(y,a)
                print(y)
            elif('c'in c):
                y=1
                for i in range(d):
                    y=producto(y,a)
                print(y)
        elif(y==6):
            matriz()
        
        
        s=input('Si desea relaizar otra operacion escriba -si- en caso contrario -no-')
    


# In[ ]:




