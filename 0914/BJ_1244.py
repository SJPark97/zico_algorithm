n = int(input())
switch = list(map(int, input().split()))
for _ in range(int(input())):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num-1, n, num):
            switch[i] = abs(switch[i]-1)
    else:
        num = num - 1
        switch[num] = abs(switch[num]-1)
        for j in range(1, n//2):
            if num - j < 0 or num + j >= n or switch[num-j] != switch[num+j]:
                break
            switch[num-j] = abs(switch[num-j]-1)
            switch[num+j] = abs(switch[num+j] - 1)
for l in range(0, len(switch), 20):
    p_switch = switch[l:l+20]
    print(*p_switch)