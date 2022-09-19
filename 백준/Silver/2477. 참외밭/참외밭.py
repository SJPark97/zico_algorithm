k = int(input())
length = [list(map(int, input().split()))[1] for _ in range(6)]
center = length.index(max(length))
front = length[(center + 1) % 6] * length[(center + 2) % 6]
end = length[center - 1] * length[center - 2]
print((front+end)*k)