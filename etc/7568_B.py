
'''
(몸무게 , 키)
(x, p)
(y, q)

x > y and p > q : 덩치가 크다
'''

N = int(input())

info_lst = [input().split() for _ in range(N)]

cnt_lst = []

L = len(info_lst)


for i in range(L):
    cnt = 0
    for j in range(L):
        if i == j:
            continue
        if info_lst[i][0] > info_lst[j][0] and info_lst[i][1] > info_lst[j][1]:
            cnt += 1
    cnt_lst.append(cnt)

for c in range(L):
    cnt_lst[c] += 1

min_num = min(cnt_lst)
max_num = max(cnt_lst)
min_idx = cnt_lst.index(min_num)
max_idx = cnt_lst.index(max_num)

cnt_lst[min_idx] = N
cnt_lst[max_idx] = 1

print(cnt_lst)


print(*cnt_lst)
