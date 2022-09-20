def search(v, visited, adj_lst, cnt_lst):
    cnt_lst[v] = 1
    visited[v] = 1
    Q = [adj_lst[v]]  # [[3,2]]
    # n = 1
    while Q:
        w = Q.pop(0)
        for node in w:
            if not visited[node]:
                Q.append(adj_lst[node])
                visited[node] = 1
                for i in range(len(adj_lst)):
                    if node in adj_lst[i]:
                        cnt_lst[node] = cnt_lst[i] + 1
                        break

    return cnt_lst

def solution(n, edge):
    answer = 0

    adj_lst = [[] for _ in range(n + 1)]
    visited = [0] * (n+1)
    cnt_lst = [0] * (n + 1)
    for node in edge:
        a = node[0]
        b = node[1]
        adj_lst[a].append(b)
        adj_lst[b].append(a)

    cnt = search(1, visited, adj_lst, cnt_lst)


    max_num = max(cnt)
    answer = cnt.count(max_num)
    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])