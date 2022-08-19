import numpy as np
import time
start_time = time.time()
def sort():
    global index
    index = list(range(N))
    list1 = [min(A1//a[j],C1//c[j]) for j in range(N)]
    ratio = [f[j]*list1[j] for j in range(N)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    return index
def Try(k):
    global A,C,max_value,f1
    coe = min(C//c[index[k]],A//a[index[k]])    
    for j in range(coe,-1,-1):
        if j >= m[index[k]]:
            i = j
        else:
            i =0
        X[k] = i
        C -= i*c[index[k]]
        A -= i*a[index[k]]
        f1 = f1 + i*f[index[k]]
        if k == N-1 :
            solution()               
        else:           
            g1 = f1 + min(C//c[index[k+1]],A//a[index[k+1]])*f[index[k+1]]
            if g1 >= max_value: 
                Try(k+1)
        C += i*c[index[k]]
        A += i*a[index[k]]
        f1 = f1 - i*f[index[k]]
    
def solution():
    global f1
    global max_value ,start_time
    
    if f1 > max_value:
        max_value = f1
        for i in range(N):
            x_best[i][1]= X[i]
        print("update best :", max_value, "," , "time = ", time.time()-start_time , "s")
    

f1 = 0
N = 4    
A1 = 150
C1 =250   
c = [10,12,15,10]
a = [4,2,7,5]
f = [5,6,4,8]
m = [10,12,6,4]   
A = 150
C = 250 

max_value = 0
X =  [0]*N

sort()
x_best = [[i+1, 0] for i in index ]
Try(0)
print('The maximum value of items that can be carried:', max_value)
print('The solution in which the items should be taken:', x_best)




