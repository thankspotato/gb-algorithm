import math


def is_prime(n):
    # 주어진 수 n에 대하여 1과 자기자신 외에 약수를 가지고 있지 않은지 판별
    if n == 1:
        return False
    # 제곱근을 기준으로 약수의 쌍이 대칭을 이루므로, 제곱근까지만 반복하며 검증하면 된다
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_prime_list(n):
    for i in n:
        pass


while True:
    n = int(input())
    primes = []
    count = 0
    if n > 0:
        for i in range(n + 1, (2 * n) + 1):
            if is_prime(i):
                primes.append(i)
                count += 1
        print(count)
    else:
        break
