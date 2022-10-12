import sys
input = sys.stdin.readline


def search(check_to_chicken_shop):
    global ans
    total_distance = 0
    for house in house_lst:
        r, c = house
        min_distance = 987654321
        for shop in check_to_chicken_shop:
            shop_r, shop_c = shop
            distance = abs(r - shop_r) + abs(c - shop_c)
            if distance < min_distance:
                min_distance = distance
        total_distance += min_distance

    if ans > total_distance:
        ans = total_distance


def set_chicken(n, order):
    if n == M:
        order_to_check = list(map(int, order.split()))
        tmp_chicken_shop = []
        for orders in order_to_check:
            tmp_chicken_shop.append(chicken_shop[orders])
        search(tmp_chicken_shop)
        return

    for i in range(len(chicken_shop)):
        if not check_chicken_shop[i]:
            check_chicken_shop[i] = 1
            set_chicken(n + 1, order + str(i) + ' ')
            check_chicken_shop[i] = 0


# N : 배열의 크기, M : 치킨 집의 최대 개수
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]


ans = 987654321
# 0 : 빈 칸, 1 : 집, 2: 치킨집
chicken_shop = []
house_lst = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            chicken_shop.append((i, j))
        if lst[i][j] == 1:
            house_lst.append((i, j))

check_chicken_shop = [0] * (len(chicken_shop))
set_chicken(0, '')

print(ans)