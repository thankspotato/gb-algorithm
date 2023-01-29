# 1부터 n까지 홀수와 짝수를 번갈아서 출력
# 샘플: 1, 3, 5, 7 ... 2, 4, 6, 8 ...
# 범위는 입력값으로 주어진다.


def printOdd(n):
    if n > 1:
        printEven(n - 1)
    print(n)
    return


def printEven(n):
    if n > 1:
        printOdd(n - 1)
    print(n)
    return


n = int(input())
if n % 2 == 0:
    printEven(n)
else:
    printOdd(n)
