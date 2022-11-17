x, y, w, q = map(int, input().split())
print(min(x, y, w - x, q - y))