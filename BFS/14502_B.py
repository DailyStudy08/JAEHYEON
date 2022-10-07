import copy
from collections import deque


def bfs():
    tmp_lst = copy.deepcopy(lst)
    Q = deque()
    for i in range(N):
        for j in range(M):
            if tmp_lst[i][j] == 2:
                Q.append((i, j))

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if N > nr >= 0 and M > nc >= 0 and tmp_lst[nr][nc] == 0:
                tmp_lst[nr][nc] = 2
                Q.append((nr, nc))

    global ans
    cnt = 0

    for i in range(N):
        cnt += tmp_lst[i].count(0)
    ans = max(ans, cnt)


def make_wall(cnt):
    global ans
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 0:
                lst[i][j] = 1
                make_wall(cnt + 1)
                lst[i][j] = 0


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

ans = 0
make_wall(0)

print(ans)