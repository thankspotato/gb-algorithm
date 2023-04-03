# 삽입 정렬로
# 오름차순 정렬
# 배열 A에 K 번째 저장되는 수를 구하기


def insertion_sort(N, K, A):
    # 문제가 이해가 잘 안되는데..
    # 교환이 필요한 인덱스에 도달하면 temp에 해당하는 인덱스의 값을 저장하고, 카운트를 올린다. 카운트가 k가 되면 temp에 저장한 값을 출력하겠다
    count = 0
    print('정렬 전 A', A)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if A[j] < A[j-1]:
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
                count += 1
                print('A', A)
            if count == K:
                print(temp)
                return
    if count < K:
        print(-1)
    return


N, K = map(int, input().split())
A = list(map(int, input().split()))


insertion_sort(N, K, A)
