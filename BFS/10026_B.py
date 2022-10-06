from collections import deque

def bfs(r, c, P, color):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    Q = deque([(r, c)])
    while Q:
        r, c = Q.popleft()
        visited[r][c] = 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr >= N or nr < 0 or nc >= N or nc < 0:
                continue
            
            if visited[nr][nc]:
                continue

            if P:
                if color == 'R' or color == 'G':
                    if lst[nr][nc] == 'R' or lst[nr][nc] == 'G':
                        Q.append((nr, nc))
                else:
                    if lst[nr][nc] == 'B':
                        Q.append((nr, nc))
            else:
                if lst[nr][nc] == color:
                    Q.append((nr, nc))


N = int(input())

lst = [[] for _ in range(N)]
for i in range(N):
    for s in input():
        lst[i].append(s)

cnt_1 = 0
cnt_2 = 0

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, True, lst[i][j])
            cnt_1 += 1

for i in range(N):
    for j in range(N):
        visited[i][j] = 0

# visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, False, lst[i][j])
            cnt_2 += 1

print(cnt_2, cnt_1)