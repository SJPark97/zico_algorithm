N = int(input())
card_list = list(range(1, N+1))

while card_list:
    print(card_list.pop(0), end=' ')
    if card_list:
        card_list.append(card_list.pop(0))
