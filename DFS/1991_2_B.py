

N = int(input())

tree = [0] * (N+1)
ch_left = [0] * (N+1)
ch_right = [0] * (N+1)

for _ in range(N):
    parent, child_left, child_right = input().split()
    V = ord(parent) - 64
    # child_left = ord(child_right) - 64
    # child_right = ord(child_right) - 64

    tree[V] = parent
    if child_left.isalpha():
        ch_left[V] = child_left
    if child_right.isalpha():
        ch_right[V] = child_right
        
        
# 1부터 시작
def pre_order(n):
    if tree[n]:
        print(tree[n], end='')
        if ch_left[n]:
            pre_order(ord(ch_left[n])-64)
        if ch_right[n]:
            pre_order(ord(ch_right[n])-64)


def in_order(n):
    if tree[n]:
        if ch_left[n]:
            in_order(ord(ch_left[n])-64)

        print(tree[n], end='')

        if ch_right[n]:
            in_order(ord(ch_right[n])-64)


def post_order(n):
    if tree[n]:
        if ch_left[n]:
            post_order(ord(ch_left[n]) - 64)

        if ch_right[n]:
            post_order(ord(ch_right[n]) - 64)

        print(tree[n], end='')


pre_order(1)
print()
in_order(1)
print()
post_order(1)