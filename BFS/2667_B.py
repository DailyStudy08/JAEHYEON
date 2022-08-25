'''
모든 index 를 순회하되
index 의 사방을 확인하면서
1이 있으면 Q 에 삽입 및 cnt += 1
다 돌고 없을 때는 해당 cnt 를 lst 에 append

visited 에 방문하지 않은 index 가 없을 때 bfs 를 멈춤
'''

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = []


def bfs(r, c):
    cnt = 1
    visited[r][c] = True
    Q = [(r, c)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while Q:
        w = Q.pop(0)
        for d in range(4):
            new_r = w[0] + dr[d]
            new_c = w[1] + dc[d]
            if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
                continue

            if arr[new_r][new_c] == 1 and not visited[new_r][new_c]:
                visited[new_r][new_c] = True
                Q.append((new_r, new_c))
                cnt += 1

    return cnt


for row in range(N):
    for col in range(N):
        if arr[row][col] == 1 and not visited[row][col]:
            result.append(bfs(row, col))

print(len(result))
for r in result:
    print(r)
# remove_n = {0}
# result = [i for i in result if i not in remove_n]



# print(len(result))
# if len(result) == 1:
#     if result[0] == 0:
#         print(0)
#     else:
#         print(result[0])
# else:
#     for r in sorted(result):
#         print(r)
