# N개의 서로 다른 양의 정수가 저장된 배열 A
# 선택 정렬로
# A를 오름차순 정렬할 경우
# K 번째 교환되는 수

# 입력
# 첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 10,000), 교환 횟수 K(1 ≤ K ≤ N)가 주어진다
# 둘째 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN

# 출력
# K 번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력
# 교환 횟수가 K 보다 작으면 -1을 출력

def select_sort(N, K, A):
    swap_count = 0

    for i in range(N-1, 0, -1):
        index_of_max_value = A.index(max(A[:i+1]))
        if index_of_max_value != i:
            temp = A[i]
            A[i] = A[index_of_max_value]
            A[index_of_max_value] = temp
            swap_count += 1
        if swap_count == K:
            print(A[index_of_max_value], A[i])
            return

    if swap_count < K:
        print(-1)


N, K = map(int, input().split())
A = list(map(int, input().split()))

select_sort(N, K, A)

