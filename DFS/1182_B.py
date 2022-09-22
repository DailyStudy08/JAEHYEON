
def search2(idx, sm):
    global cnt

    if idx >= N:
        return

    sm += data[idx]

    if sm == S:
        cnt += 1

    search2(idx+1, sm)

    search2(idx+1, sm - data[idx])


def search(n, sm):
    global cnt
    visited[n] = 1

    if sm == S:
        cnt += 1
        # return
    if n == N:
        return

    for i in range(N):
        if not visited[i]:
            search(n+1, sm + data[i])
            visited[i] = 0
            sm -= (data[i])


N, S = map(int, input().split())
data = list(map(int, input().split()))
visited = [0] * N
cnt = 0
# search(0, data[0])
search2(0, 0)
print(cnt)