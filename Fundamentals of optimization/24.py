import numpy as np
N = 10
A = np.random.randint(100, size=(N,N))
for i in range(N):
    for j in range(N):
        if i == j :
            A[i,j] = 999

def Greedy():
    Last = 0
    C = [i for a in range(1,N)]
    S = [0]
    while len(C)!=0:
        x = [A[Last][i] for a in C]
        y = [A[last][i] for a in C]
        j = y.index(min(x))+1
        S.append(J)
        last = j
        C.remove(j)
    return S
print(Greedy())