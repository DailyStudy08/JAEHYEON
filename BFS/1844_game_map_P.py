def bfs(n, m, maps):
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    Q = [(0, 0)]
    while Q:
        w = Q.pop(0)
        r = w[0]
        c = w[1]
        for d in range(4):
            new_r = r + dr[d]
            new_c = c + dc[d]

            if new_r >= n or new_r < 0 or new_c >= m or new_c < 0:
                continue

            if maps[new_r][new_c] == 0:
                continue

            if maps[new_r][new_c] == 1:
                maps[new_r][new_c] = maps[r][c] + 1
                Q.append((new_r, new_c))

    return maps[n - 1][m - 1]


def solution(maps):
    n = 0  # row
    m = 0  # col

    # n, m 구하기
    for _ in maps[0]:
        n += 1
    for _ in maps:
        m += 1

    answer = bfs(n, m, maps)
    print(answer)
    return answer if answer > 1 else -1


solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])