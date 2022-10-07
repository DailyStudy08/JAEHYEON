'''
1 : 익은 토마토
0 : 익지 않은 토마토
-1 : 토마토가 없는 칸

저장될 때부터 모든 토마토가 익어있는 상태면 0
토마토가 모두 익지 못하는 상황이면 -1
토마토가 모두 익을 때 까지의 최소 날짜 출력
'''

from collections import deque

def bfs(coor):
    cnt = 0
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    Q = [coor]
    tmp = []
    while Q:
        for q in Q.pop(0):
            r, c = q
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if nr >= row or nr < 0 or nc >= col or nc < 0:
                    continue
                if lst[nr][nc] == -1:
                    continue
                if lst[nr][nc] == 0:
                    lst[nr][nc] = 1
                    tmp.append((nr, nc))
        if tmp:
            Q.append(tmp)
            cnt += 1
        tmp = []

    return cnt


col, row = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(row)]

# 저장될 때 부터 모든 토마토가 익어있는 상태이면 0 출력 > 1 만 있을 때
is_all_clear = False
zero_cnt = 0
for i in range(row):
    zero_cnt += lst[i].count(0)
    zero_cnt += lst[i].count(-1)

if zero_cnt > 1:
    is_all_clear = True

if not is_all_clear:
    ans = 0

ans = 0
if is_all_clear:
    coor = []
    for i in range(row):
        for j in range(col):
            if lst[i][j] == 1:
                coor.append((i, j))
    ans += bfs(coor)

    for i in range(row):
        for j in range(col):
            if lst[i][j] == 0:
                ans = -1

print(ans)