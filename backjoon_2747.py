n = int(input())
a, b = 0, 1

if n > 45:
    print('범위 초과')
elif n < 2:
    print(n)
else:
    for i in range(2, n+1):
        a, b = b, a + b
    print(b)
