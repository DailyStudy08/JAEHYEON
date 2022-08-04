def solve(a: list) -> int :
    sum = 0

    for _a in a:
        sum += _a
    
    return sum

a = list(map(int, input().split()))

solve(a)
