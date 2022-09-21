import sys

sys.stdin = open('s_input.txt', 'r')


# d : depth, sm: sum
def dfs(d, sm):
    global ans

    # 가지치기 : 현재 depth 에서의 sum 이 ans 보다 크거나 같을 때 > 조건에 부합하지 않음
    if sm >= ans:
        return

    # depth 가 N 까지 왔을 때
    if d == N:
        if sm < ans:
            ans = sm
        return

    for col in range(N):
        # 방문처리 확인은 column 만 하면 됨
        if not visited[col]:
            visited[col] = 1
            # depth += 1, 넘기는 sum 에 현재위치에 해당하는 좌표값 추가
            dfs(d+1, sm+arr[d][col])
            # 위에서 재귀한 함수가 return 됐을 때
            visited[col] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 987654321
    dfs(0, 0)
    print(f'#{tc} {ans}')