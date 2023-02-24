def solution(book_time):
    times = []
    for start, end in book_time:
        st = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:]) + 10
        times.append((st, end))
    times.sort(key=lambda x: (x[0], x[1]))
    room = []
    for st, end in times:
        for i in range(len(room)):
            room_st, room_end = room[i]
            if st >= room_end:
                print(end, room_end)
                room[i] = (st, end)
                break
        else:
            room.append((st, end))
    return len(room)


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))