def sol():
    def find_winner(player1, player2, length):
        player1.sort(reverse=True)
        player2.sort(reverse=True)
        if player1 == player2:
            print("D")
            return
        for _ in range(length):
            if player1[0] > player2[0]:
                print("A")
                return
            elif player1[0] < player2[0]:
                print("B")
                return
            del player1[0], player2[0]
        if player1:
            print("A")
            return
        print("B")
        return

    games = int(input())
    board = [list(map(int, input().split())) for _ in range(2 * games)]
    for i in range(0, 2 * games, 2):
        a = board[i][1:]
        b = board[i + 1][1:]
        find_winner(a, b, min(board[i][0], board[i + 1][0]))


sol()
