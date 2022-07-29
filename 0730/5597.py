list = list(range(1, 31))
for _ in range(28):
    student_number = int(input())
    list.remove(student_number)
print(f'{list[0]}\n{list[1]}')
