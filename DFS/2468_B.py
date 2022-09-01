'''
1. 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에잠긴다
2. 각 원소는 해당 지점의 높이
3. 물에 잠기지 않는 영역 : 물에 잠기지 않는 지점들이 상하좌우로 인접 이고 그 크기가 최대인 영역
4.


'''
import sys
sys.setrecursionlimit(10000)
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

def search(r, c, height):
    visited[r][c] = True
    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    for d in range(4):
        new_r = r + dr[d]
        new_c = c + dc[d]

        if N > new_r >= 0 and N > new_c >= 0 and not visited[new_r][new_c] and arr[new_r][new_c] > height:
            search(new_r, new_c, height)

    return 1

num_lst = []
for row in range(N):
    for col in range(N):
        num = arr[row][col]
        if num not in num_lst:
            num_lst.append(num)


cnt = 0
for height in num_lst:
    visited = [[False]* N for _ in range(N)]
    temp = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] > height and not visited[row][col]:
                temp += search(row, col, height)
    if temp > cnt:
        cnt = temp
if cnt:
    print(cnt)
else:
    print(1)

