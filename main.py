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
# field = [['-']*3 for _ in range(3)]
# show_field(field)

