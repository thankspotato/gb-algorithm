def calc(inputs: list):
    # 반복문의 범위, 더 작은 수를 r에 저장해서 반복 횟수를 최소화한다.
    r = 0
    # Note(오답): 서로소 케이스 누락, 0으로 설정하면 서로소일 때 최대공약수 체크가 안됨
    gcd = 1
    lcm = 0
    n = inputs[0]
    m = inputs[1]
    if n - m > 0:
        r = n
    else:
        r = m
    # Note(오답노트): 범위 설정이 잘못되었다. r-1까지만 반복하는 것이 문제!
    for i in range(2, r + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    lcm = int(n * m / gcd)
    print(gcd)
    print(lcm)


inputs = list(map(int, input().split()))
calc(inputs)
