'''

각 좌표를 확인하면서 L 이면 방문처리
해당 L 을 기준으로 사방을 돌면서 BFS 처리
마지막으로 끝났을 때 까지의 거리를 구해야함 일단

비교를 해서 어느 좌표에서 시작했을 때의 거리가 더 긴
값이 답
'''

import sys
from collections import deque

input = sys.stdin.readline

def search(r, c, t):
    global ans
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    tmp_max = 0
    Q = deque([(r, c, t)])
    while Q:
        r, c, t = Q.popleft()
        visited[r][c] = 1

        if t > tmp_max:
            tmp_max = t

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if row > nr >= 0 and col > nc >= 0 and not visited[nr][nc] and lst[nr][nc] == 'L':
                Q.append((nr, nc, t + 1))

    return tmp_max


row, col = map(int, input().split())
lst = [list(input().strip()) for _ in range(row)]
ans = -987654321
for r in range(row):
    for c in range(col):
        if lst[r][c] == 'L':
            visited = [[0] * col for _ in range(row)]
            call = search(r, c, 0)
            if call > ans:
                ans = call
print(ans)