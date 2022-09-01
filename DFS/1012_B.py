T = int(input())

def search(r, c):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for d in range(4):
        new_r = r + dr[d]
        new_c = c + dc[d]
        if M > new_r >= 0 and N > new_c >= 0 and not visited[new_r][new_c] and arr[new_r][new_c] == 1:
            visited[new_r][new_c] = 1
            search(new_r, new_c)


for _ in range(T):
    M, N, K = map(int, input().split())
    
    arr = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1

    result = 0
    for row in range(M):
        for col in range(N):
            if arr[row][col] == 1 and not visited[row][col]:
                search(row, col)
                result += 1

    print(result)



