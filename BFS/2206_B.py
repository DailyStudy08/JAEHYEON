from collections import deque
import sys
input = sys.stdin.readline


def search():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for wal in wall:
        tmp_lst = lst
        if wal:
            w_r, w_c = wal
            tmp_lst[w_r][w_c] = 0
        Q = deque([(0, 0)])
        tmp_lst[0][0] = 1
        visited = [[0] * M for _ in range(N)]
        while Q:
            r, c = Q.popleft()
            visited[r][c] = 1
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if N > nr >= 0 and M > nc >= 0 and tmp_lst[nr][nc] == 0 and not visited[nr][nc]:
                    tmp_lst[nr][nc] = tmp_lst[r][c] + 1
                    Q.append((nr, nc))

        cnt_lst.append(tmp_lst[N-1][M-1])


def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    Q = deque([(0, 0, False)])
    visited[0][0][0] = 1
    while Q:
        r, c, is_break = Q.popleft()

        if r == N - 1 and c == M - 1:
            return visited[r][c][is_break]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr >= N or nr < 0 or nc >= M or nc < 0:
                continue

            if visited[nr][nc][is_break]:
                continue

            if lst[nr][nc] == 0:
                visited[nr][nc][is_break] = visited[r][c][is_break] + 1
                Q.append((nr, nc, is_break))

            if not is_break and lst[nr][nc] == 1:
                visited[nr][nc][1] = visited[r][c][is_break] + 1
                Q.append((nr, nc, True))

    # 마지막 점에 방문하지 못 했을 경우
    return -1


N, M = map(int, input().split())
lst = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs())

# print(visited)
