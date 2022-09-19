import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
up = 1
up_list = [1]
down = 1
down_list = [1]
for i in range(n - 1):
    if nums[i] < nums[i + 1]:
        up += 1
        down_list.append(down)
        down = 1
    elif nums[i] > nums[i + 1]:
        down += 1
        up_list.append(up)
        up = 1
    else:
        up += 1
        down += 1
        up_list.append(up)
        down_list.append(down)
up_list.append(up)
down_list.append(down)
print(max(max(up_list), max(down_list)))
