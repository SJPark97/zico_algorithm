n = int(input())
a = n // 5
b = n % 5
answer = -1
if b == 0:
    answer = a
elif b == 1 and a >= 1 or b == 3:
    answer = a + 1
elif b == 2 and a >= 2 or b == 4 and a >= 1:
    answer = a + 2
print(answer)
