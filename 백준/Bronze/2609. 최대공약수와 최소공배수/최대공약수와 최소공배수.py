def gcd1(a, b):
    if b == 0:
        return a
    return gcd1(b, a % b)


a, b = map(int, input().split())
c = gcd1(a, b)
print(c)
print(a * b // c)
