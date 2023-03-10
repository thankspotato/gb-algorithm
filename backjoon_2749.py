# 피사노 주기 : 피보나치 수를 k로 나눈 나머지는 항상 주기를 갖게 된다.
# 주기의 길이가 p일 때, n번째 피보나치 수를 m으로 나눈 나머지는 n % p번째 피보나치 수를 m으로 나눈 나머지와 같다.
# m이 10^k일 때, k > 2라면 주기는 항상 15 * 10^(k-1)


n = int(input('숫자 n 입력: '))
m = 1000000
p = m / 10 * 15
fibo = [0, 1]

for i in range(2, int(p)):
    fibo.append(fibo[i-1]+fibo[i-2])
    fibo[i] %= m  # %=: 왼쪽 변수를 오른쪽 변수로 나눈 후 그 결과를 왼쪽 변수에 할당

print(fibo[int(n % p)])

