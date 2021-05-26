# coded by Anton Karpov
import numpy as np 
import matplotlib.pyplot as plt

# Математическое ожидание 
def mathoj (x,N):
    s = 0
    for i in range (N):
        s = s + x[i]
    return s/N 

# Дисперсия
def disp (x, N):
    d = 0
    M = mathoj(x, N)
    for i in range (N):
        d = d + (x[i]-M)*(x[i]-M)
    return d / N

# Серднее
def sredn(x, N):
    return np.sqrt(disp(x, N))

def xi_2(x,N,maximum):
    kol_vo=20
    s=0
    k=maximum/kol_vo
    p=1/kol_vo
    n=np.zeros(kol_vo+1)
    granitsa=np.zeros(kol_vo+1)
    for i in range(1,kol_vo+1):
        granitsa[i]=granitsa[i-1]+k
    for i in range(1,kol_vo+1):
        for j in range(N):
            if (x[j]>=granitsa[i-1] and x[j]<granitsa[i]):
                n[i-1]+=1
    for i in range(kol_vo+1):
        if(n[i]!=0):
            s=s+(n[i]-p*N)**2
    nn=np.zeros(21000)
    j=0
    for i in range(21):
        j+=1
        while j%1000!=0:
            nn[j-1]=n[i]
            j+=1
    m=np.arange(0,21000,1)
    plt.xticks(np.arange(0,21000,2000))
    plt.plot(m,nn)
    plt.show
    return (s/p*N)
                

# Задаем переменные
a =11
b =12
c = 13
m = 20000
N = int(input("введите кол-во чисел:")) 
x1=np.zeros(N)
x1[0]=1400
x1[1]=1600
for i in range (1, N-1):
    x1[i+1] = abs(((a * x1[i] + b *x1[i-1] + c) % m ))
for i in range (N):
    print (x1[i])
maximum=max(x1)
print (' - - - - - - - - - - - ')
print('Математическое ожидание: ', mathoj(x1, N))
print('Дисперсия: ', disp(x1, N))
print('Среднее: ', sredn(x1, N))
print('хи- квадрат оценки равномерности распределения: ', xi_2(x1,N,maximum))