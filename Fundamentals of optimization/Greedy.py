import numpy as np
import time
def sort():
    global index
    index = list(range(N))
    list1 = [min(A//a[j],C//c[j]) for j in range(N)]
    ratio = [f[j]*list1[j] for j in range(N)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    return index
def Greedy_produce_planing(N,A,C,a,c,f,m):
    global max_value
    global x_best
    max_value = 0
    x_best = dict()
    for i in index:
        x_best[i+1] = 0
    for i in index:
        if a[i] <= A and c[i] <=C :
            if min(A//a[i],C//c[i]) >= m[i]:
                x_best[i+1] = min(A//a[i],C//c[i])

                max_value += f[i] * x_best[i+1]
                C -= c[i]*x_best[i+1]
                A -= a[i]*x_best[i+1]            
        else :
            break
    
    return max_value,x_best
N = 4
A = 150
C = 250
c = [10,12,15,10]
a = [4,2,7,5]
f = [5,6,4,8]
m = [10,12,6,25]
start_time = time.time()
sort()
Greedy_produce_planing(N, A, C, a, c, f, m)

print('The maximum value of items that can be carried:', max_value)
print('The solution in which the items should be taken:', x_best)
print("time:", time.time() - start_time)

        
            