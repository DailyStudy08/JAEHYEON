C = int(input())

for _ in range(C):
    T = list(map(int, input().split()))
    N = T[0]
    score_lst = T[1:]

    avg = sum(score_lst) / len(score_lst)
    cnt = 0
    for score in score_lst:
        if score > avg:
            cnt += 1

    result = (cnt / N) * 100

    print(f"{result:.3f}%")