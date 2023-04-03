# 문제 요구사항 #
# 길이가 N인 정수 배열 A와 B
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# B는 재배열하면 안됨
# S의 최솟값을 구할 것
import copy

# 설계 먼저 #
# [가장 큰수] * [가장 작은수] => S를 최소로 만들 수 있지 않을까?
# B의 원소의 크기가 큰 순서대로 인덱스를 나열한다.
    # 가장 큰 값의 인덱스를 찾은 뒤, 해당 인덱스의 값을 -1로 만들고 또 가장 큰값을 찾는 식으로 진행
    # 예를 들면 [1, 5, 3]은 인덱스 1, 2, 0 순으로 크다.
# A를 내림차순 정렬한다.
# 정렬된 A와 인덱스 정렬한 B를 곱해서 S를 구한다.


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def sort_ascending(A):
    for i in range(N-1, 0, -1):
        index_of_max_value = A.index(max(A[:i+1]))
        if i != index_of_max_value:
            A[i], A[index_of_max_value] = A[index_of_max_value], A[i]
    return A


def sort_indices_descending(B):
    # B의 복사본 만들기
    B_copy = copy.deepcopy(B)

    # B의 원소의 크기가 큰 순서대로 인덱스 저장
    B_indices = [0] * N
    for i in range(N):
        index_of_max_value = B_copy.index(max(B_copy))
        B_indices[i] = index_of_max_value
        B_copy[index_of_max_value] = -1
    return B_indices


def dot_product(A, B, N):
    # A를 오름차순 정렬
    A = sort_ascending(A)
    B_indices = sort_indices_descending(B)
    S = 0

    for i in range(N):
        S += (A[i] * B[B_indices[i]])

    print(S)


dot_product(A, B, N)
