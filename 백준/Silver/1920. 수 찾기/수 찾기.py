n = int(input())
li1 = set(map(int, input().split()))
m = int(input())
for num in map(int, input().split()):
    if num in li1:
        print(1)
    else:
        print(0)