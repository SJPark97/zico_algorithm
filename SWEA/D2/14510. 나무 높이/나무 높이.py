def sol():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        tree_list = list(map(int, input().split()))
        tree_list.sort()
        high = tree_list.pop()
        cnt2 = 0
        cnt1 = 0
        for i in range(n - 1):
            cnt2 += (high - tree_list[i]) // 2
            cnt1 += (high - tree_list[i]) % 2
        if cnt1 > cnt2:
            answer = cnt1 * 2 - 1
        elif cnt1 == cnt2:
            answer = cnt1 * 2
        else:
            while cnt1 < cnt2:
                cnt2 -= 1
                cnt1 += 2
            answer = cnt1 + cnt2
        print('#{} {}'.format(tc, answer))


sol()
