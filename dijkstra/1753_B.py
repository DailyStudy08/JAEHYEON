from collections import deque
import sys

V, E = map(int, sys.stdin.readline().split())
S = int(sys.stdin.readline())
# adj_M = [[0] * (V+1) for _ in range(V+1)]
adj_L = [[] for _ in range(V+1)]
D = [0xffffff] * (V+1)
D[S] = 0
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    # adj_M[s][e] = w
    adj_L[s].append([e,w])


Q = deque([S])
while Q:
    w = Q.popleft()
    # if not adj_L[w]:
    #     continue
    adj_L[w].sort(key= lambda x: x[1])  # 시간 초과 나서 추가해봄
    for node in adj_L[w]:
        end = node[0]
        weight = node[1]
        distance = D[w] + weight
        if distance < D[end]:
            D[end] = distance
            Q.append(end)

    # 기존 코드 인접행렬 이용하게되면 최대 노드 20000 개이므로 20000^2 배열 생성으로 메모리 초과
    # for i in range(E):
    #     # weight = adj_M[w][i]
    #     weight = adj_L[w]
    #
    #     if weight:
    #         distance = D[w] + weight
    #         if distance < D[i]:
    #             D[i] = distance
    #             Q.append(i)

for i in range(1, len(D)):
    if D[i] != 0xffffff:
        print(D[i])
    else:
        print('INF')
