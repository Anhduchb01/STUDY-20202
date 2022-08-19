def Greedy_TSP(distance):
    N = len(distance)
    S = [0]
    last = 0
    C = [i for i in range(1, N)]
    while len(C) != 0:
        x=[distance[last][i] for i in C]
        print(x)
        dis_cop=[distance[last][i] for i in range(1,N)]
        j=dis_cop.index(min(x))+1
        S.append(j)
        last = j
        print(j)
        print(C)
        C.remove(j)

    return S


distance = [[99999, 4, 10, 2, 17],
            [4, 99999, 4, 11, 9],
            [10, 4, 99999, 12, 3],
            [2, 11, 12, 99999, 13],
            [17, 9, 3, 6, 99999]]

print(Greedy_TSP(distance))
