def new(a, b):
    if a >= 1 and a <= 1000 and b >= 1 and b <= 1000:
        return (a + b) * (a - b)
    return False


A, B = map(int, input().split())
new(A, B)
print(new(A, B))
