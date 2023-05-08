# 병합 정렬은 분포에 관계없이 시간복잡도가 동일하다는 특징이 있다
import sys

sys.setrecursionlimit(10**6)
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
switch_count = 0


def merge_sort(arr, start, end, k):
    global switch_count
    half_point = int((start + end) / 2)  # 소수점 이하 버림
    merge_sort(arr, start, half_point, k)
    merge_sort(arr, half_point, end, k)
    print(merge(arr, start, end, half_point, k))


def merge(arr, start, end, half_point, k):
    i = start
    j = half_point
    temp = []
    while i <= half_point and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
            switch_count += 1
            if switch_count == k:
                return arr[i]
        else:
            temp.append(arr[j])
            j += 1
            switch_count += 1
            if switch_count == k:
                return arr[j]
    while i <= half_point:
        temp.append(arr[i])
        i += 1
        switch_count += 1
        if switch_count == k:
            return arr[i]
    while j <= end:
        temp.append(arr[j])
        j += 1
        switch_count += 1
        if switch_count == k:
            return arr[j]
    for p in len(arr):
        arr[p] = temp[p]
        switch_count += 1
        if switch_count == k:
            return arr[p]
    return -1


merge_sort(A, 0, N, K)
