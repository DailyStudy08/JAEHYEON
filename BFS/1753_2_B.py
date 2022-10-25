import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = sys.maxsize
D = [INF] * (V + 1)
heap = []
adj_lst = [[] for _ in range(V + 1)]


def dijkstra(start):
    D[start] = 0
    heapq.heappush(heap, (0, K))

    while heap:
        w, v = heapq.heappop(heap)

        if D[v] < w:
            continue

        for weight, node in adj_lst[v]:
            new_weight = w + weight
            if D[node] > new_weight:
                D[node] = new_weight
                heapq.heappush(heap, (new_weight, node))


for _ in range(E):
    u, v, w = map(int, input().split())
    adj_lst[u].append((w, v))

dijkstra(K)


for i in range(1, V + 1):
    print("INF" if D[i] == INF else D[i])