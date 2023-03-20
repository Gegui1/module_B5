board = [['_']*3 for _ in range(3)]

def show_board(f):
   print('  0 1 2')
   for i in range(len(board)):
      print(str(i), *board[i])

def players_input(f):
    while True:
        place = input('Введите координаты').split()
        if len(place) != 2:
            print('Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x,y = map(int,place)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Вышли из диапазона')
            continue
        if f[x][y] != '_':
            print('Клетка занята')
            continue
        break
    return x,y

def winner_1(f,player):
    def check_line(a1, a2, a3, player):
        if a1==player and a2==player and a3==player:
            return True
    for n in range(3):
        if check_line(f[n][0],f[n][1],f[n][2], player) or \
           check_line(f[0][n], f[1][n], f[2][n], player) or \
           check_line(f[0][0], f[1][1], f[2][2], player) or \
           check_line(f[2][0], f[1][1], f[0][2], player):
             return True
    return False

count = 0
while True:
    if count == 9:
        print('Ничья')
    if count%2 == 0:
        player = 'x'
    else:
        player = 'o'
    show_board(board)
    x,y = players_input(board)
    board[x][y] = player
    if winner_1(board,player):
        print(f"Выиграл {player}")
        show_board(board)
        break
    count += 1