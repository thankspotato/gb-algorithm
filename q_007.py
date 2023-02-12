def loop(start, end, add):
    if start >= end:
        return
    print(start)
    loop(start + add, end, add)


inputs = input()
[m, n, p] = map(int, inputs.split())
loop(m, n, p)
