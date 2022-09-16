def search(r, c):
    visited[r][c] = 1
    # 팔방
    # 북서 북 북동 동 남동 남 남서 서
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]

    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]
        if h > nr >= 0 and w > nc >= 0 and not visited[nr][nc] and Map[nr][nc]:
            search(nr, nc)


while True:
    # w : 지도의 너비, h : 지도의 높이
    w, h = map(int, input().split())
    if not w and not h:
        break
    visited = [[0] * w for _ in range(h)]
    Map = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for x in range(h):
        for y in range(w):
            if Map[x][y] and not visited[x][y]:
                search(x, y)
                cnt += 1
    print(cnt)


