def search(n, st):
    if n == M:
        print(st)
        return
    for i in range(N):
        search(n+1, st + str(lst[i]) + ' ')


N, M = map(int, input().split())
lst = [num for num in range(1, N+1)]


search(0, '')
