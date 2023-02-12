# 원판의 갯수
N = int(input())
# 옮긴 횟수
k = (2 ** N) - 1


def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
        return
    if 1 < n <= 20:
        hanoi(n-1, start, end, mid)
        print(start, end)
        hanoi(n-1, mid, start, end)
        return
    if n > 20:
        return


print(k)
hanoi(N, 1, 2, 3)
