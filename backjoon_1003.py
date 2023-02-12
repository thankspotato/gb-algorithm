f_0 = 0
f_1 = 0
czo = []


def fibonacci(n):
    global f_0
    global f_1
    global czo
    if n == 0:
        f_0 += 1
        # return
    if n == 1:
        f_1 += 1
        # return
    if n > 1:
        fibonacci(n-1)
        fibonacci(n-2)
    czo.append([f_0, f_1])
    return str(f_0) + ' ' + str(f_1)


# 테스트 케이스 갯수
T = int(input())
for _ in range(T):
    N = int(input())
    print(fibonacci(N))
    f_0, f_1 = 0, 0
