from operator import is_


def dfs(r, c):
    
    
    if lst[r][c] == 3:
        return 1
    lst[r][c] = -1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if N > nr >= 0 and N > nc >= 0 and lst[nr][nc] != 1 and lst[nr][nc] != -1:
            if dfs(nr, nc) == 1:
                return 1

    return 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().strip())) for _ in range(N)]
    is_coor = False
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 2:
                row = i
                col = j
                is_coor = True
                break
        if is_coor:
            break


    ans = dfs(row, col)
    print(f'#{tc} {ans}')