def search(r, c):
    lst[r][c] = 1

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    Q = [(r, c)]
    cnt = 1
    while Q:
        r, c = Q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if M > nr >= 0 and N > nc >= 0 and not lst[nr][nc]:
                Q.append((nr, nc))
                lst[nr][nc] = 1
                cnt += 1
    return cnt


M, N, K = map(int, input().split())

lst = [[0] * N for _ in range(M)]

cnt = 0
ans_lst = []
for _ in range(K):
    l_x, l_y, r_x, r_y = map(int, input().split())
    r_x -= 1
    r_y -= 1

    for row in range(M):
        for col in range(N):
            if l_y <= row <= r_y and l_x <= col <= r_x:
                lst[row][col] = 1

tmp_cnt = []
m_cnt = 0
for row in range(M):
    for col in range(N):
        if not lst[row][col]:
            tmp = search(row, col)
            if tmp:
                tmp_cnt.append(tmp)
                m_cnt += 1
print(m_cnt)
print(*sorted(tmp_cnt))
