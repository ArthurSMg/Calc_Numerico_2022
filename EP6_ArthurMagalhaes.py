import numpy as np


#Primeiro teste do EP6

#Input
Np=int(input()); # Numero de zeros (=grau N) do polinomio de Legendre P_n(x)
TD=float(input()); # Temperatura de Debye T_D (Em Kelvin)
Ntemp=int(input()); # O Numero N_temp de temperaturas T (C_v(T_j)/k_B)
vTemp=np.zeros(Ntemp);
for ii in range(Ntemp):
     vTemp[ii]=float(input());



#Para encontrar os zeros e os pesos de P_n(u) devemos utilizar a função "np.polynomial.legendre.leggauss(Np)"
## Note que legval usa uma normalizacao diferente! ## https://mathworld.wolfram.com/LegendrePolynomial.html


def x1(vTemp):  #Encontrando os valores de x1(T)   #x1 terá dimcao de vTemp
    x1list = []
    for ii in range(len(vTemp)):
        x1list.append(TD/vTemp[ii])

    return x1list

#Agora vamos escrever uma funcao para retornar a primeira parte do calculo de C_v/k_B = 9*(T/T_D)**3 * I(T)

def eq1(vTemp):   #Eq 1 tera dimensoes de vTemp 
    l1 = np.ones(len(vTemp))
    lTD = l1*TD
    leq1 = 9*(vTemp/lTD)**3
    return leq1

#Agora vamos tentar fazer a aproximacao da integral para um grau N


zN,wN = np.polynomial.legendre.leggauss(Np)  #pegando os zeros e pesos para o caso x entre -1 e 1

def aproxfinal(x1list,zN): #Aqui eu tenho que fazer o f para cada valor de xk e x1
    xk = []
    lf = []
    la = []
    u = 0 
    i=0
    while i< len(x1list):
        for k in zN:
            la.append(1/2*(x1list[i]*k+x1list[i]))
        xk.append(la)
        la = []
        i = i+1

    while u<len(xk):
        for kk in xk[u]:
            la.append((kk**4*np.e**kk)/(np.e**kk-1)**2)
        lf.append(la)
        la = []
        u = u+1
    return lf



def aproxI(wN,lf):
    s = []
    soma = np.zeros(len(lf))
    #zeros = []
    u = 0
    
    while u < len(lf):
        for aux in range(len(wN)):
            s.append(lf[u][aux]*wN[aux])
            soma[u] = sum(s)
        s = []
        u = u+1 
    return soma

def cvkb(leq1,soma):
    l2 = np.ones(len(x1list))*2
    lmudvar = x1list/l2   #Valores de mudanca de variavel
    I = []
    cv = []

    for i in range(len(lmudvar)):
        I.append(soma[i]*lmudvar[i])
    for k in range(len(I)):
        cv.append(leq1[k]*I[k])
    
    return cv


## zona para os calculos


x1list = x1(vTemp)
leq1 = eq1(vTemp)
#lmudvar = mudvar(x1list)

lf = aproxfinal(x1list, zN)
soma = aproxI(wN,lf)
cv = cvkb(leq1,soma)



#Output

for ii in range(Ntemp) :
     print("{:10.6e}".format(cv[ii]));
