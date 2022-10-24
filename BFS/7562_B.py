def bfs(r, c):
    global ans

    # 8방향을 움직일 수 있음
    dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    dc = [-2, -1, 1, 2, 2, 1, -1, -2]

    Q = [(r,c)]
    while Q:
        w = Q.pop(0)
        r, c = w

        if r == mr and c == mc:
            cnt = visited[r][c]
            if cnt < ans:
                ans = cnt
            pass

        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr >= N or nr < 0 or nc >= N or nc < 0:
                continue

            new_pos = (nr, nc)
            if not visited[nr][nc]:
                Q.append(new_pos)
                visited[nr][nc] = visited[r][c] + 1

T = int(input())
for _ in range(T):
    # N : 한 변의 길이(정사각형)
    N = int(input())
    # 현재 위치
    r, c = map(int, input().split())
    # 이동하고자 하는 위치
    mr, mc = map(int, input().split())
    # 방문한 좌표
    v = [(r,c)]
    visited = [[0]*N for _ in range(N)]
    ans = 987654321
    # search(0, r, c)
    bfs(r,c)
    print(ans)


