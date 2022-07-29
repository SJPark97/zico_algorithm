N = int(input())
list = map(int, input().split())
v = int(input())
print(len([n for n in list if n == v]))
