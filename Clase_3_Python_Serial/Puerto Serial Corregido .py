#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import serial
import sys
import Calculadora
import Grafico


# In[2]:


## Genera la trama a enviar
def generar(a=''):
    print('La cantidad de caracteres de ',a,'es menor a 16 por lo que se envia una trama corta')
    b = len(a)
    c = 0xA0
    cabezera= b | c
    mutable_bytes = bytearray()
    mutable_bytes.append(cabezera)
    mutable_bytes.append(0)
    mutable_bytes.append(0)
    mutable_bytes.append(0)
    mutable_bytes.append(0)
    a_bytes = bytearray(a, "ascii")
    for i in range(len(a)):
        mutable_bytes.append(a_bytes[i])
    mutable_bytes.append(cabezera)
    #print(len(mutable_bytes))
    print('Trama a enviar',mutable_bytes)
    for j in range(len(mutable_bytes)) :
        k= bin(mutable_bytes[j])
        print(k)
    return(mutable_bytes)


# In[6]:


ser = serial.serial_for_url('loop://', timeout=1)
ser.isOpen()
ser.timeout=None
ser.flushInput()
ser.flushOutput()

punto=input('Eliga que ejercicio quiere ejecutar a-b-c')
##############################################
if(punto=='a'):
    dato= input('Ingrese 1-2-exit')
    while(dato !='1' and dato !='2' and dato !='exit'):
            print('Opcion no valida')
            dato=input('Ingrese 1-2-exit')

    out=''
    ser.write(dato.encode())
    while ser.inWaiting() > 0 :
        out+=ser.read(1).decode()
    print(out)

    if(out=="exit"):
        ser.close()
        print('Puerto Serial cerrado')                  
                       
    if(out=="1"):
        Calculadora.calculadora()
        
    if(out=="2"):
        Grafico.graficar()
########################################
elif(punto=='b'):
    dato= input('Ingrese Calculadora-Graficar-exit')
    while(dato !='Calculadora' and dato !='Graficar' and dato !='exit'):
        print('Comando invalido')
        dato=input('Ingrese Calculadora-Graficar-exit')
    
    out=''
    ser.write(dato.encode())
    while ser.inWaiting() > 0 :
        out+=ser.read(1).decode()
    print(out)

    if(out=="exit"):
        ser.close()
        print('Puerto Serial cerrado')                  
                       
    if(out=="Calculadora"):
        Calculadora.calculadora()
        
    if(out=="Graficar"):
        Grafico.graficar()
#########################################################    
elif(punto=='c'): 
    dato= input('Ingrese Calculadora-Graficar-exit')
    while(dato !='Calculadora' and dato !='Graficar' and dato !='exit'):
        print('Comando invalido')
        dato=input('Ingrese Calculadora-Graficar-exit')
        
    mutable_bytes = generar(dato)
    ser.write(mutable_bytes)
    out=bytearray()
    while ser.inWaiting() > 0 :
        out+=ser.read(1)
    print('Trama recibida: ',out)
    
    
    ### En esta parte se lee el tamaño de la trama que se encuentra en los bits menos significatiovs DE LA CABEZERA
    a=int(out[0])
    c= 0b01011111
    d = a & c
    
    ### De acuerdo al tamaño leido se procede a leer el dato
    text=bytearray()
    for i in range(5,5+d):
        text.append(out[i])
    
    print(text)
    
    
    text1 =text.decode('utf-8')
    print(text1)
    #print(type(text1))
    if(text1=='exit'):
        ser.close()
        print('Puerto Serial cerrado')
    if(text1=='Graficar'):
        Grafico.graficar()
    if(text1=='Calculadora'):
        Calculadora.calculadora()


# In[ ]:




