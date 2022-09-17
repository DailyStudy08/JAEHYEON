def search(w, target, degree):
    global result
    if w == target:
        return 1

    for node in adj_lst[w]:
        if not visited[node]:
            visited[node] = 1
            if search(node, target, degree + 1):
                result = degree + 1
    return 0


# n : 전체 사람의 수
n = int(input())
# t_parent, t_child : 촌수를 계산해야하는 서로 다른 두 사람의 번호
t_parent, t_child = map(int, input().split())
# 관계의 개수
m = int(input())
adj_lst = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
result = -1
for _ in range(m):
    parent, child = map(int, input().split())
    adj_lst[parent].append(child)
    adj_lst[child].append(parent)

search(t_child, t_parent, 0)
print(result)


