for test_case in range(1, 11):
    print(f'#{test_case}', end = ' ')
    count = int(input())
    box_list = list(map(int, input().split()))
    while count > 0:
        for i in range(len(box_list) - 1, 0, -1):       #정렬
            for j in range(0, i):
                if box_list[j] > box_list[j + 1]:
                    box_list[j], box_list[j + 1] = box_list[j + 1], box_list[j]
        if box_list[-1] - box_list[0] <= 1:
            break
        box_list[0] += 1
        box_list[-1] -= 1
        count -= 1
    if box_list[0] < box_list[1]:
        box_min = box_list[0]
    else:
        box_min = box_list[1]
    if box_list[-1] > box_list[-2]:
        box_max = box_list[-1]
    else:
        box_max = box_list[-2]
    answer = box_max - box_min
    print(answer)