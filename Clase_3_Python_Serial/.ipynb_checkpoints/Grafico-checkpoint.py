#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as pl
import random
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


def obt(t_joinvect = [0]):
    if(len(t_joinvect)==1):
        j=tuple(t_joinvect)
        v=j[0]
        
    else:
        v=tuple(t_joinvect)
       
    return(v)


# In[3]:


def ingreso():
    join2=[]
    join1=[]
    w=[]
    joinvect=[]
    for i in range(5):
        join = input('Ingrese distribucion del Grafico Numero (%d): ' % (i))
        x=join.split("-")
        join1.append(x)
        #print(join1)
    for j in range(5):
        join2=join1[j]
        b=[int(x) for x in join2]
        w.extend(b)
        joinvect.append(b)
   
    #print (w)

    return(joinvect,w)


# In[4]:


def figPlot(x=[0], y=[0], row=0, col=0, t_joinvect=[0], numplot=0, show=False, typeGraf=[0], xlim=[0], ylim=[0], xlabel=[0],ylabel=[0]):
    if(show):
        pl.figure(num=1,figsize=[10,10])
        for i in range(5):
            t = obt(t_joinvect[i])
            if(typeGraf[i]=='stem'):
                pl.subplot(row,col,t)
                pl.stem(x[i],y[i],markerfmt='C1o')
               #pl.plot(x[i],y[i])
                pl.ylabel(xlabel[i])
                pl.xlabel(ylabel[i])
                pl.xlim(xlim[i])
                pl.ylim(ylim[i])
                
            else:
                pl.subplot(row,col,t)
                pl.plot(x[i],y[i])
                pl.ylabel(xlabel[i])
                pl.xlabel(ylabel[i])
                pl.xlim(xlim[i])
                pl.ylim(ylim[i])
                
        
        pl.show()


# In[5]:


def graficar():
    ###################fUNCIONES X Y##############
    print('Valores a Graficar (5 graficos)')
    x= np.random.randint(0,10,size=[5,5])
    print('Valores de x'+'\n',x)
    y= np.random.randint(0,10,size=[5,5])
    print('Valores de y'+'\n',y)
    #x = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
    #y = np.array([[1,2,3,6],[1,2,3,2],[1,2,3,1],[1,2,3,0],[1,2,3,4]])
    
    #######INGRESA LAS FILAS Y COLUMNAS##
    row=int(input('Ingrese cantidad de filas'))
    col=int(input('Ingrese cantidad de columnas'))
    
    
    ##INGRESA JOINVECT Y SE VERIFICA SI LA DISTRIBUCION ES CORRECTA
    print('Ingrese la distribucion en este formato X-X')
    t_joinvect,prueba = ingreso()
    while(len(prueba)!=len(set(prueba)) or max(prueba)>row*col):
        print('Distribucion incorrecta los graficos se solapan o estan fuera del limite')
        t_joinvect,prueba = ingreso()
    print(t_joinvect)
    #t_joinvect =[[1,3],[4],[5],[6],[7,9]]
    
    
    ## INGRESA EL TIPO DE GRAFICO
    TdeGraf=[]
    for i in range(5):
        num =input('Ingrese Tipo de Grafico (stem o plot) del Grafico Numero (%d): ' % (i))
        TdeGraf.append(num)
    print(TdeGraf)
    #TdeGraf=np.array(['stem','stem','plot','plot','plot'])
    
    
    
    ## INGRESA LOS XLIM YLIM
    xlim =[]
    ylim = []
    for i in range(5):
        print('Ingrese limite inferior y superio del eje X del Grafico Numero(%d): ' % (i))
        numx = [int(input('Ingrese limite inferior de x (%d):'% (i))),int(input('Ingrese limite superior de x (%d):' % (i)))]
        print('Ingrese limite inferior y superio del eje Y del Grafico Numero(%d):' % (i))
        numy = [int(input('Ingrese limite inferior de y (%d):' % (i))),int(input('Ingrese limite superior de y (%d):'% (i)))]
        xlim.append(numx)
        ylim.append(numy)
    print('xlim: ',xlim)
    print('ylim: ',ylim)
    #xlim =np.array([[0,4],[0,4],[0,5],[0,6],[0,5]])
    #ylim =np.array([[1,6],[1,4],[0,5],[0,6],[0,5]])
    
    
    
    ## SE INGRESA LOS XLABEL YLABEL
    xlabel =[]
    ylabel = []
    for i in range(5):
        j=input('Ingrese Nombre del EjeX del Grafico Numero (%d): ' % (i))
        p=input('Ingrese Nombre del EjeY del Grafico Numero (%d): ' % (i))
        xlabel.append(j)
        ylabel.append(p)
    print('xlabel: ',xlabel)
    print('xlabel: ',ylabel)
    
    
    numplot = int(input('Ingrese numplot'))

    ## SE INGRESA SHOW
    show1 = (input('Ingrese show (true o false)'))
    if show1 == "true":
        show = True
        print(show)
    elif show1 == "false":
        show = False
        print(show)
        
    figPlot(x,y,row,col,t_joinvect,1,show,TdeGraf,xlim,ylim,ylabel,xlabel )

 
      


# In[ ]:





# In[ ]:




