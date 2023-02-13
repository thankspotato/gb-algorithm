p = [0, 1, 1]

def pinary(n):
    global p
    for i in range(3, n+1):
        p.append(p[i - 1] + p[i - 2])
    print(p[n])


def pinary_self(n):
    a = p(n-1)
    b = p(n-2)
    return a + b


n = int(input())
pinary(n)

