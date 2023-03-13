p = [0, 1, 1]

def pinary(n):
    global p
    for i in range(3, n+1):
        p.append(p[i - 1] + p[i - 2])
    print(p[n])


# 재귀함수로 구현
def pinary_self(n):

    a = pinary_self(n-1)
    b = pinary_self(n-2)
    return a + b


n = int(input())
pinary_self(n)

