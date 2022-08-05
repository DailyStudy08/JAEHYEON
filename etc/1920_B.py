# N = int(input())
# visit = [False] * (N + 1)

# nums = list(map(int, input().split()))
# # visit[el] = True
# for num in nums:
#     visit[num] = True

# # M
# M = int(input())
# # 있는지 확인
# bools = list(map(int, input().split()))
# for _bool in bools:
#     try:
#         visit[_bool]
#         print(1)
#     except:
#         print(0)

N = int(input())
nums = list(map(int, input().split()))
visit = {}

for num in nums:
    visit[num] = True

M = int(input())
bools = list(map(int, input().split()))

for b in bools:
    if visit.get(b):
        print(1)
    else:
        print(0)