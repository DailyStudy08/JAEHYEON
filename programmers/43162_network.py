# def solution(n, computers):
#     answer = 0
#     visited = [0] * n
#
#
#     def bfs():
#
#         for com in computers:
#             Q = com
#             visited[0] = 1
#             cnt = 0
#             while Q:
#                 w = Q.pop(0)
#                 for idx, node in enumerate(w):
#                     print('w :', w, 'idx :', idx, 'node :',node)
#                     if not visited[idx] and node:
#                         visited[idx] = 1
#                         Q.append(idx)
#
#             return cnt
#
#     answer = bfs()
#     return answer

def bfs(n, lst):
    answer = 0
    visited = [0] * n
    for i in range(n):
        Q = [lst[i]]
        cnt = 0
        while Q:
            w = Q.pop(0)
            for node in w:
                for adj_node in lst[node]:
                    if not visited[adj_node]:
                        visited[adj_node] = 1
                        cnt += 1
                        Q.append([adj_node])

        if cnt > 0:
            answer += 1

    return answer


def solution(n, computers):
    adj_lst = [[] for _ in range(n)]

    for i in range(len(adj_lst)):
        adj_lst[i].append(i)

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i != j and computers[i][j] == 1:
                adj_lst[i].append(j)

    answer = bfs(n, adj_lst)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print()
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))