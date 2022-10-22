from collections import deque

def bfs():
    Q = deque([(0, 0)])
    lst[0][0] = 1
    while Q:
        r, c = Q.popleft()
        if r == N - 1 and c == M - 1:
            return lst[r][c]

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if N > nr >= 0 and M > nc >= 0 and lst[nr][nc]:
                lst[nr][nc] = lst[r][c] + 1
                Q.append((nr, nc))

N, M = map(int, input().split())
lst = [list(map(int, input().strip())) for _ in range(N)]



ans = bfs()
print(ans)