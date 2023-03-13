# case1. 가로길이 1을 배치하는 방법
# case2. 가로길이 2를 배치하는 방법 * 2 (2*2로 배치하는 방법과 2*1로 배치하는 방법)


# n번째 직사각형을 채우는 방법: n-1번째 직사각형에서 case1과 case2 더해주기
def tiling(n):
    if n == 0 or n == 1:
        return 1
    a = [0 for _ in range(n + 1)]
    a[0], a[1] = 1, 1
    for i in range(2, n+1):
        a[i] = a[i - 1] + 2 * a[i - 2]
    return a[n]


dp = [0 for i in range(251)]
dp[0], dp[1] = 1, 1


# 재귀함수로
def tiling_dp(n):
    w_1 = 0
    w_2 = 0
    if n <= 1:
        return dp[n]
    if n <= 250:
        if dp[n-1] == 0:
            w_1 = tiling_dp(n-1)
        else:
            w_1 = dp[n-1]
        if dp[n-2] == 0:
            w_2 = tiling_dp(n-2)
        else:
            w_2 = dp[n-2]
        dp[n] = w_1 + 2 * w_2
        return dp[n]


while True:
    try:
        n = int(input())
        print(tiling_dp(n))
    except:
        break



