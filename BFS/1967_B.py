import sys
from collections import deque


def search(n):
    visited = [0] * (N + 1)
    D = [0] * (N + 1)
    Q = deque([(n, 0)])
    while Q:
        node, w = Q.popleft()
        visited[node] = 1
        for f in adj_lst[node]:
            new_node, weight = f
            new_weight = w + weight
            if D[new_node] < new_weight and not visited[new_node]:
                Q.append((new_node, new_weight))
                D[new_node] = new_weight

    return max(D)
# n : 노드의 개수(1부터)
N = int(sys.stdin.readline())
adj_lst = [[] for _ in range(N + 1)]

for _ in range(N-1):
    p, c, w = map(int, sys.stdin.readline().split())
    adj_lst[p].append((c, w))
    adj_lst[c].append((p, w))


ans = -987654321
for num in range(1, (N + 1)):
    cal = search(num)
    if cal > ans:
        ans = cal

print(ans)