n = int(input())
fibo = [0, 1]

if n > 90:
    print('범위 초과')
elif n < 2:
    print(n)
else:
    for i in range(2, n+1):
        fibo.append(fibo[i-2] + fibo[i-3])
    print(fibo[n-1])
