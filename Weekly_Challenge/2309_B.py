
# def check_real(N):

#     if N == 7 and total == 100 and len(real) == 7:
#         real.sort()
#         for r in real:
#             print(r)
#             return
#     elif total != 100 and len(real) == 7:
#         real = []
#     else:
#         return check_real(N+1)


lst = []
for _ in range(9):
    case = int(input())
    lst.append(case)
S = sorted(lst)

# S = [7, 8, 10, 13, 15, 19, 20, 23, 25]
total = sum(S)
for i in range(8):
    for j in range(i+1, 9):
        add = S[i] + S[j]
        if total - add == 100:
            S1 = S[i]
            S2 = S[j]
        
S.remove(S1)
S.remove(S2)


for s in S:
    print(s)
