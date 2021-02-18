#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import serial
import sys
import Calculadora
import Grafico


# In[ ]:


## Genera la trama a enviar
def generar(a=''):
    mutable_bytes = bytearray(b'\xB0\x00\x00\x00')
    a_bytes = bytearray(a, "ascii")
    for i in range(len(a)):
        mutable_bytes.append(a_bytes[i])
    mutable_bytes.append(176)
    #print(len(mutable_bytes))
    print('Trama Larga a enviar :',mutable_bytes)
    return(mutable_bytes)


# In[ ]:


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
    
    text=bytearray()
    if(len(out)==9):
        for i in range(4,8):
            text.append(out[i])
    elif(len(out)==13):
        for i in range(4,12):
            text.append(out[i])
    elif(len(out)==16):
        for i in range(4,15):
            text.append(out[i])
    
    #print(text)
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




