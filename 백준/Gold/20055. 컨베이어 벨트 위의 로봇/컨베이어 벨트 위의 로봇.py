from collections import deque

N, K = map(int, input().split())
velt = list(map(int, input().split()))
queue = deque(velt[::-1])
robot_location = deque([])
cnt = 0

while True:
    cnt += 1
    for _ in range(len(robot_location)):
        i = robot_location.popleft() - 1
        if i > -N:
            if queue[i] > 0 and robot_location.count(i-1) == 0:
                # 해당 위치 -1
                queue[i] -= 1
                if i - 1 > -N:
                    robot_location.append(i-1)
            else:
                robot_location.append(i)
    chk = queue.popleft()
    if chk > 0:
        robot_location.append(-1)
        queue.append(chk - 1)
    else:
        queue.append(chk)
    if queue.count(0) >= K:
        break

print(cnt)