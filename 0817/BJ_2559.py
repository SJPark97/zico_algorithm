
N, K = map(int, input().split())

num_list = list(map(int, input().split()))

highest_sum = 0
for i in range(len(num_list)-K+1):
    list_sum = 0
    for j in range(K):
        list_sum += num_list[i+j]
    if highest_sum < list_sum:
        highest_sum = list_sum

print(highest_sum)

