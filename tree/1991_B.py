N = int(input())        # 노드의 개수(정점)
tree = [0] * (N + 1)
ch1 = [0] * (N + 1)
ch2 = [0] * (N + 1)

for _ in range(N):
    # 'A' : 루트 노드, '.' : 자식 노드가 없는 경우
    node, left, right = input().split()
    V = ord(node) - 64
    tree[V] = node
    if left != '.':
        ch1[V] = left
    if right != '.':
        ch2[V] = right


def preorder(n):        # 전위 순회
    if tree[n]:
        print(tree[n], end='')
        if ch1[n]:
            preorder(ord(ch1[n]) - 64)
        if ch2[n]:
            preorder(ord(ch2[n]) - 64)


def inorder(n):         # 중위 순회
    if tree[n]:
        if ch1[n]:
            inorder(ord(ch1[n]) - 64)
        print(tree[n], end='')
        if ch2[n]:
            inorder(ord(ch2[n]) - 64)


def postorder(n):       # 후위 순회
    if tree[n]:
        if ch1[n]:
            postorder(ord(ch1[n]) - 64)
        if ch2[n]:
            postorder(ord(ch2[n]) - 64)
        print(tree[n], end='')


preorder(1)
print()
inorder(1)
print()
postorder(1)
print()