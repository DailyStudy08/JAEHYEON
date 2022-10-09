import copy

operator = ['*', '+', '-']
nums = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

visited = [0] * 3


def make_priority(n, pr, exp_stack):
    global result
    if n == 3:
        tmp = cal(pr, exp_stack)
        if tmp > result:
            result = tmp
        return

    for i in range(3):
        if not visited[i]:
            visited[i] = 1
            make_priority(n + 1, pr + str(i) + ' ', exp_stack)
            visited[i] = 0


def cal(pr, exp_stack):
    priority = list(map(int, pr.split()))
    exp = exp_stack

    for pr in priority:
        op = operator[pr]
        if len(exp) >= 3:
            while op in exp:
                idx = exp.index(op)
                a = exp[idx-1]
                b = exp[idx+1]
                if op == '+':
                    tmp = a + b
                elif op == '-':
                    tmp = a - b
                elif op == '*':
                    tmp = a * b
                exp = exp[:idx-1] + [tmp] + exp[idx+2:]

            if len(exp) == 1:
                return abs(exp[0])

result = -987654321


def solution(expression):
    global result

    exp_stack = []
    tmp = ''
    for idx, e in enumerate(expression):
        if e in nums:
            tmp += e
            if idx == len(expression) - 1:
                exp_stack.append(int(tmp))
        else:
            exp_stack.append(int(tmp))
            exp_stack.append(e)
            tmp = ''

    make_priority(0, '', exp_stack)
    answer = result
    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
