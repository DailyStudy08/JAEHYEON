sum = 1
for _ in range(3):
    n = int(input())
    sum *= n

s_dict = {}
for i in range(0,10):
    s_dict.setdefault(i,0)

for s in str(sum):
    if int(s) in list(s_dict.keys()):
        s_dict[int(s)] += 1

for j in list(s_dict.values()):
    print(j)