def chk(nums):
    while True:
        if nums[-2] < nums[-1]:
            return nums
        nums.append(nums[-2] - nums[-1])


n = int(input())
answer = []
if n == 1:
    print(4)
    print(*[1, 1, 0, 1])
else:
    for num in range(int(n * 0.61), int(n * 0.7) + 1):
        chk_nums = chk([n, num])
        if len(answer) < len(chk_nums):
            answer = chk_nums[:]
    print(len(answer))
    print(*answer)