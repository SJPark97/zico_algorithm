numbers = list(map(int, input().split()))
code = 0
for number in numbers:
    code += number**2
print(code % 10)
