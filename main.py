def greet():
    print("-------------------")
    print(" Приветствуем Вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

def show_field():
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + ' ' + ' '.join(field[i]))


def user_input():
    while True:
        cords = input("         Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue
        if field[x][y] != "-":
            print(" Клетка занята! ")
            continue
        return x, y


def win_position():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False


def start():
    count = 0
    while True:
        count += 1
        show_field()
        if count % 2 == 1:
            print(" Ходит крестик!")
        else:
            print(" Ходит нолик!")

        x, y = user_input()

        if count % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "0"
        if win_position():
            break
        if count == 9:
            print(" Ничья!")
            break


greet()
field = [['-'] * 3 for _ in range(3)]
start()
