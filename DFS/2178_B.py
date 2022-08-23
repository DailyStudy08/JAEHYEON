N, M = map(int,input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

'''
(1,1) 에서 출발해서 (N, M) 의 위치로 이동할 때 지나야하는 최소의 칸 수
1 : 이동할 수 있는 칸
0 : 이동할 수 없는 칸
case1 :
(1,1) > (4,6) 의 위치로
'''
# 우하좌상


# 시작점
r, c = (1, 1)


def bfs(r, c):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    queue = []
    queue.append((r,c))
    while queue:
        r, c = queue.pop(0)
        for d in range(4):
            new_r = r + dr[d]
            new_c = c + dc[d]

            if new_r < 0 or new_r >= N or new_c < 0 or new_c >= M:
                continue

            if maze[new_r][new_c] == 0:
                continue

            if maze[new_r][new_c] == 1:
                maze[new_r][new_c] = maze[r][c] + 1
                queue.append((new_r, new_c))

    return maze[N-1][M-1]

print(bfs(0,0))



