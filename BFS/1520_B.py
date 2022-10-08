from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)


# def dfs(r, c, h):
#     global cnt
#     if r == M - 1 and c == N - 1:
#         cnt += 1
#         visited[r][c] = 0
#         return
#
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#     for d in range(4):
#         nr = r + dr[d]
#         nc = c + dc[d]
#         if nr >= M or nr < 0 or nc >= N or nc < 0:
#             continue
#
#         if not visited[nr][nc] and lst[nr][nc] < h:
#             visited[nr][nc] = 1
#             dfs(nr, nc, lst[nr][nc])



# def bfs():
#     global cnt
#     Q = deque([(0, 0, lst[0][0])])
#     while Q:
#         r, c, h = Q.popleft()
#         visited[nr][nc] = 1
#         if r == M - 1 and c == N - 1:
#
#             cnt += 1
#
#         dr = [-1, 1, 0, 0]
#         dc = [0, 0, -1, 1]
#         for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]
#             if nr >= M or nr < 0 or nc >= N or nc < 0:
#                 continue
#
#             if not visited[nr][nc] and lst[nr][nc] < h:
#                 Q.append((nr, nc, lst[nr][nc]))


def dfs(r, c):
    if r == M - 1 and c == N - 1:
        return 1

    if visited[r][c] == -1:
        visited[r][c] = 0

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < M and 0 <= nc < N :
                if lst[r][c] > lst[nr][nc]:
                    visited[r][c] += dfs(nr, nc)

    return visited[r][c]


M, N = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
visited = [[-1] * N for _ in range(N)]
cnt = 0

# bfs()
# dfs(0, 0, lst[0][0])
ans = dfs(0, 0)
print(ans)