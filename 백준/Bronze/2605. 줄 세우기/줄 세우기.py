num = int(input())
move = list(map(int, input().split()))
student = list(range(1, num+1))
answer = []
for i in range(num):
    answer.insert(move[i], student[i])
print(*answer[::-1])
