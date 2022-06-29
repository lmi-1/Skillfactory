def greet():
    print("-------------------")
    print(" Приветствуем Вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

def show_field(f):
    num ='  0 1 2'
    print(num)
    for row,i in zip(f,num.split()):
        print(f"{i} {' '.join(str(j) for j in row)}")

def user_input(f,user):
    while True:
        place=input(f"Ходит {user} .Введите координаты: ").split()
        if len(place)!=2:
            print('Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Вышли из диапазона')
            continue
        if f[x][y]!='-':
            print('Клетка занята')
            continue
        break
    return x,y


# field = [['-']*3 for _ in range(3)]
# greet()
# show_field(field)
# user_input(field,'x')


