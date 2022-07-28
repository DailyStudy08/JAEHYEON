
N = int(input())

def recur(N):

    if N == 1:
        return N
    elif N == 0:
        return 1
    
    return N * recur(N-1)


print(recur(10))