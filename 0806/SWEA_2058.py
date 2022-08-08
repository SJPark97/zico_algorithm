N = int(input())
result = 0
while N > 0:
    result += N % 10
    N = N // 10
print(result)


print(sum(list(map(int, list(input())))))

N = input()
result = 0
for number in N:
    result += int(number)
print(result)
