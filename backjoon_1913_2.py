def printarr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=" ")
        print()


n = int(input())
m = int(input())

num = n * n
snail = [[0 for _ in range(n)] for _ in range(n)]

# 좌표 초기화
# 유의할 점: 행렬이므로 x가 세로축, y가 가로축
x, y = 1, 1
answer_x, answer_y = 0, 0


def snail_(n):
    global x, y, num, answer_x, answer_y
    # 움직일 횟수 초기화
    go_down = n-1
    go_right = n-1
    go_up = n-1
    go_left = n-1

    while go_left > 0:
        snail[y-1][x-1] = num
        if num == m:
            answer_x = x
            answer_y = y
        num = num - 1
        if go_down > 0:
            y += 1
            go_down -= 1
        elif go_right > 0:
            x += 1
            go_right -= 1
        elif go_up > 0:
            y -= 1
            go_up -= 1
        elif go_left > 0:
            x -= 1
            go_left -= 1
    x += 1
    y += 1


while n > 0:
    snail_(n)
    n -= 2

snail[y-2][x-2] = 1

printarr(snail)
print(answer_y, answer_x)  # 행렬 좌표를 표시해야하므로