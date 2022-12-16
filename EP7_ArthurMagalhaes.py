### CODIGO FINAL ARTHUR MAGALHAES

#INPUTS DADOS PELO PROFESSOR

import numpy as np

m=float(input()); # in kg
l=float(input()); # in m
h=float(input()); # in s
Tf=float(input()); # in s
theta0=float(input()); # in rad
p0=float(input()); # in kg m^2/s

#FUNCAO FINAL

def RK2(m,l,h,Tf,theta0,p0):
    n = 0
    n2 = 0

    Nt=np.size(np.arange(0.0,Tf+h,h))  # numero inteiro com o tamanho dos arrays que serao os vetores 
  
    thetat=np.zeros(Nt)  #vetor theta somente de zeros
    pt=np.zeros(Nt)      # vetor p somente de zeros

    pt[0] = p0
    thetat[0] = theta0
    

    while n<Nt-1: #Aplicando o metodo de Runge-Kutta
        k1pt = -m*10*l*np.sin(thetat[n]) 
        k1theta = pt[n]/(m*l**2)   
    
        pt12 = pt[n] + k1pt * h/2
        theta12 = thetat[n] + k1theta * h/2

        k2pt = -m*10*l*np.sin(theta12)
        k2theta = pt12/(m*l**2)

        pt[n+1] = pt[n] + k2pt * h
        thetat[n+1] = thetat[n] + k2theta*h

        if abs(thetat[n+1]) > np.pi: #Testando para cada passo ver se o theta esta entre -pi e pi
            if theta[n+1] > 0:
                theta[n+1] = theta[n+1] - 2*np.pi
            if theta[n+1] < 0:
                theta[n+1] = theta[n+1] + 2*np.pi
        n += 1

    E = []

    n2 = 0

    while n2<Nt:
        E.append((pt[n2])**2/(2*m*l**2) + m*10*l*(1-np.cos(thetat[n2]))) #Calculando a Energia para verificar se esta praticamente constante

        n2 += 1 

    for ii in range(Nt):
     print("{:10.6e}".format(thetat[ii]))
    for ii in range(Nt):
     print("{:10.6e}".format(pt[ii]))
    


    

    
RK2(m,l,h,Tf,theta0,p0)

