'''
1. 배열에 자연수 x 를 삽입
2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거

> 프로그램은 비어있는 배열에서 최초 시작

1. x 가 자연수 : 배열에 x 라는 값을 추가하는 연산
2. x 가 0 : 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우

출력 :
입력에서 0 이 주어진 회수만큼 답을 출력
만약 배열이 비어있는 경우 가장 큰 값을 출력하라고 하는 경우 0 을 출력
'''


def enq(key):
    global last
    last += 1
    heap[last] = key
    C = last
    P = C // 2

    while P and heap[C] > heap[P]:
        heap[C], heap[P] = heap[P], heap[C]


def deq():           # 배열에서 가장 큰 값을 출력
    global last, P
    tmp = heap[P]
    last -= 1
    C_left = P * 2
    C_right = (P * 2) + 1
    if heap[C_left] or heap[C_right]:
        if heap[C_left] > heap[C_right]:
            heap[P] = heap[C_left]
            heap[C_left] = 0
        else:
            heap[P] = heap[C_right]
            heap[C_right] = 0
    else:
        heap[P] = 0

    return tmp


last = 0
P = 1
heap = [0] * 100000

N = int(input())        # 연산의 개수
for _ in range(N):
    x = int(input())    # 연산에 대한 정보를 나타내는 정수 x
    if x:               # key 가 0이 아닐 경우
        enq(x)
    else:               # key 가 0 일 경우
        if heap[P]:
            print(deq())
        else:
            print(0)



