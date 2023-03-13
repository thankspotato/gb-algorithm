f_0 = 0
f_1 = 0
czo = [[0, 0] for i in range(41)]
czo[0] = [0, 1]
czo[1] = [1, 0]


def fibonacci(n):
    global f_0
    global f_1
    global czo
    if n == 0:
        f_0 += 1
    if n == 1:
        f_1 += 1
    if n > 1:
        if czo[n - 1] == [0, 0]:
            fibonacci(n-1)
        else:
            czo[n - 1]
        if czo[n - 2] == [0, 0]:
            fibonacci(n-2)
        else:
            czo[n - 2]
            czo[n] = [f_0, f_1]
    return


def fibo_(n):
    # fibo_(0)이 몇 번 들어가는지
    # fibo_(1)이 몇 번 들어가는지

    fibo_(n - 1)
    fibo_(n - 2)



# 테스트 케이스 갯수
T = int(input())
for _ in range(T):
    N = int(input())
    print(fibonacci(N))
    # str(czo[n][0]) + ' ' + str(czo[n][1])
    f_0, f_1 = 0, 0
