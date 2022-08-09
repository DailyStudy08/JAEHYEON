dajango = list(map(int, input().split()))

L = len(dajango)
ans = ''
for d in range(L-1):
    if dajango[0] == 1:
        if dajango[d+1] - dajango[d] != 1:
            ans = 'mixed'
            break
        else:
            ans = 'ascending'
    else:
        if dajango[d] - dajango[d+1] != 1:
            ans = 'mixed'
            break
        else:
            ans = 'descending'

print(ans)