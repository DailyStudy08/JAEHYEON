N = int(input())

lst = list(map(int, input().split()))

ans = [min(lst), max(lst)]
print(*ans)
    