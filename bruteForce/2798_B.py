
N, M = list(map(int, input().split()))
C = list(map(int, input().split()))

def black_jack(N,M,C):
    max = -9876543210

    for i in range(len(C)):
        for j in range(i+1,len(C)):
            for k in range(j+1,len(C)):
                sum = C[i] + C[j] + C[k]
                if sum > max and sum <= M:
                    max = sum
    print(max)

black_jack(N,M,C)