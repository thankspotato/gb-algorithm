# input settings
n = int(input())
target = int(input())

# init values
snail_matrix = [[0] * n for _ in range(n)]
value = n * n
row, column = 1, 1  # 유의: 행렬이므로 row = 가로축, column = 세로축
target_row, target_column = 0, 0


def move_like_a_snail(n, row, column):
    global value, target_row, target_column
    move_down = n-1
    move_right = n-1
    move_up = n-1
    move_left = n-1

    if n == 1:
        snail_matrix[column-1][row-1] = value
        return
    if n > 1:
        # 규칙: 하->우->상->좌 로 n-1씩 움직임
        # 하: column 그대로, row 1씩 증가 (1, 0)
        # 우: row 그대로, column 1씩 증가 (0, 1)
        # 상: column 그대로, row 1씩 감소 (-1, 0)
        # 좌: row 그대로, column 1씩 감소 (0, -1)
        while move_left > 0:
            snail_matrix[column-1][row-1] = value
            if value == target:
                target_row = row
                target_column = column
            value -= 1
            if move_down > 0:
                column += 1
                move_down -= 1
            elif move_right > 0:
                row += 1
                move_right -= 1
            elif move_up > 0:
                column -= 1
                move_up -= 1
            elif move_left > 0:
                row -= 1
                move_left -= 1
        move_like_a_snail(n - 2, row + 1, column + 1)


def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=" ")
        print()


# 재귀호출로 바꾸기
if n > 0:
    move_like_a_snail(n, row, column)

print_arr(snail_matrix)
print(target_column, target_row)
