import sys
import heapq


def dijkstra(V):
    heap = []
    heapq.heappush(heap, [V, 0])
    D[V] = 0

    while heap:
        node, w = heapq.heappop(heap)
        if D[node] < w:
            continue
        for new_node, weight in adj_L[node]:
            new_weight = w + weight
            if new_weight < D[new_node]:
                D[new_node] = new_weight
                heapq.heappush(heap, [new_node, new_weight])


# N : 도시의 개수
N = int(sys.stdin.readline())
# M : 버스의 개수
M = int(sys.stdin.readline())
adj_L = [[] for _ in range(N + 1)]  # 기존 adj_M 을 이용하게되면 (1 -> 2, 10), (1 -> 2, 20) 이 들어오게되면 이후 값이 더 크지만 큰 값으로 할당됨
for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    adj_L[start].append([end, weight])

S, E = map(int, sys.stdin.readline().split())
INF = sys.maxsize   # 이거 이렇게 쓰니깐 맞네; 0xffffff 안 되네; 이게 이유가 최대 가중치가 100,000 인데 도시의 개수가 최대 1000개니깐 1억까지도 나올 수 있음 근데 0xffffff = 167만 정도니깐  삑나ㄷ는듯
D = [INF] * (N + 1)

dijkstra(S)
print(D[E])
