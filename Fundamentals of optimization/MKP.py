N = 10
Q = 20
w = [19, 16, 18, 7, 13, 15, 12, 11, 12, 2]

def select(bins,load,w):
    for b in bins:
        if load[b] + w <= Q:
            return b
    return 0
def greedyMKP():
    bins = []
    load = [0]*N
    binofitem = [[] for i in range(N)]
    for i in range(N):
        b = select(bins, load, w[i])
        if b == 0:
            b = len(bins) + 1
            bins.append(b)
            load[b] = 0
        binofitem[b].append(i+1)
        
        load[b] = load[b] + w[i]
    binofitem.pop(0)
    binofitem.pop(-1)
    return binofitem
print(greedyMKP())