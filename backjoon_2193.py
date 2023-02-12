p = [0, 1, 1]

def pinary(n):
    global p
    for i in range(3, n+1):
        p.append(p[i - 1] + p[i - 2])
    print(p[n])


n = int(input())
pinary(n)

