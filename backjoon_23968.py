# 배열 A의 크기 N, k는 교환 횟수
# 배열의 원소가 두 번째 줄에 주어짐

n, k = map(int, input().split())
a = list(map(int, input().split()))

# 버블 정렬은 앞에서부터 차례로 비교하며 교환이 필요하면 교환
swap_count = 0


def get_smaller_number(num1, num2):
    if num1 < num2:
        return num1
    if num1 > num2:
        return num2


for i in a:
    smaller_num = get_smaller_number(a[i], a[i+1])
    temp = 0
    if a[i] != smaller_num:
        temp = a[i]
        a[i] = smaller_num
        a[i+1] = temp
