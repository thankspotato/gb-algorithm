import math


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def goldbach_partition(n):
    # 두 소수의 차이가 가장 작은 것을 출력해야하므로 역순으로 탐색
    if n < 4 or n > 10000 or n % 2 != 0:
        print('범위 밖!')
    for i in range(int(n / 2), 0, -1):
        if is_prime(i):
            j = n - i
            if is_prime(j):
                return i, j


r = int(input())
for n in range(r):
    n = int(input())
    answer = goldbach_partition(n)
    print(answer[0], answer[1])

