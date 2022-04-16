def one():
    while True:
        try:
            z = int(input("Введите число z: "))
            x = int(input("Введите число x: "))
            c = int(input("Введите число c: "))
        except ValueError:
            print("Введите число!")
        else:
            print("Наибольшее число: ", max(z, x, c))
        break


def two():
    b = 0
    while True:
        try:
            z = int(input("Введите число z: "))
            x = int(input("Введите число x: "))
            c = int(input("Введите число c: "))
            q = int(input("Введите число q: "))
            w = int(input("Введите число w: "))
        except ValueError:
            print("Введите число!")
        else:
            lst = [z, x, c, q, w]
            for i in lst:
                if lst[i] > 0:
                    b += 1
            print(b)
            break


def three():
    z = input("Введите число, букву или знак: ")
    if z.isspace() or z == "":
        print("Пусто 0_0")
    elif z.isdigit() == True:
        print("Это число")
    elif z.islower() or z.isupper():
        print("Это буква")
    else:
        print("Это знак")


def four():
    z = input("Введите число: ")
    if z.isdigit():
        print("Оно натуральное")
    else:
        print("Число не натуральное")


def five_one():
    while True:
        try:
            a = int(input("Введите сторону a: "))
            if a < 0:
                continue
            b = int(input("Введите сторону b: "))
            if b < 0:
                continue
            c = int(input("Введите сторону c: "))
            if c < 0:
                continue
        except ValueError:
            print("Введите натуральное число!")
        else:
            if (a < b + c) or (b < a + c) or (c < a + b):
                print("Такой треугольник существует")
            else:
                print("Такого треугольника нет")
            break


def five_two():
    while True:
        try:
            a = int(input("Введите градус угла a: "))
            if a < 0:
                continue
            b = int(input("Введите градус угла b: "))
            if b < 0:
                continue
            c = int(input("Введите градус угла c: "))
            if c < 0:
                continue
        except ValueError:
            print("Введите натуральное число!")
        else:
            if a + b + c == 180:
                print("Такой треугольник существует")
            else:
                print("Такого треугольника нет")
            break


def five_swticth():
    print("Выберите способ нахождения треугольника")
    while True:
        try:
            a = int(input("1 - По сторонам. 2 - По сумме углов: "))
            if a == 1:
                five_one()
            elif a == 2:
                five_two()
        except ValueError:
            print("Ошибка")
        break


def six():
    while True:
        try:
            z = int(input("Введите номер билета: "))
            if len(str(z)) != 6:
                continue
        except ValueError:
            print("Ошибка")
        else:
            z = str(z)
            if int(z[0] + z[1] + z[2]) == int(z[3] + z[4] + z[5]):
                print("Поздравляю, ваш билет:", z, " - счастливый!")
            elif int(z[0] == z[1] == z[2] == z[3] == z[4] == z[5]):
                print("Поздравляю, ваш билет:", z, " - счастливый!")
            elif int(z[0] == z[5] and z[1] == z[4] and z[2] == z[3]):
                print("Поздравляю, ваш билет:", z, " - счастливый!")
            else:
                print("Печалька, ваш билет:", z, " - несчаслтивый :(")
            break


def seven():
    while True:
        try:
            a = int(input("Введите длину ребра a: "))
            if a < 0:
                continue
            b = int(input("Введите длину ребра b: "))
            if b < 0:
                continue
            c = int(input("Введите длину ребра c: "))
            if c < 0:
                continue
            x = int(input("Введите длину стороны x: "))
            if x < 0:
                continue
            y = int(input("Введите длину cтороны y: "))
            if y < 0:
                continue
        except ValueError:
            print("Введите число!")
        else:
            if (a < x and b < y) or (a < y and b < x):  # ПЕРЕДЕЛАТЬ ЗАДАНИЕ!!!!!!
                print("КИРПИЧ ЗАШЁЛ!")
            else:
                print("Кирпич не влез")
        break


def eight():
    print("Вводите числа в диапазоне от 1 до 8")
    while True:
        try:
            k = int(input("Введите k[1-8]: "))
            if (k >= 1) and (k <= 8): break
        except ValueError:
            print("Введите число!")
    while True:
        try:
            l = int(input("Введите l[1-8]: "))
            if (l >= 1) and (l <= 8): break
        except ValueError:
            print("Введите число!")
    while True:
        try:
            m = int(input("Введите m[1-8]: "))
            if (m >= 1) and (m <= 8): break
        except ValueError:
            print("Введите число!")
    while True:
        try:
            n = int(input("Введите n[1-8]: "))
            if (n >= 1) and (n <= 8): break
        except ValueError:
            print("Введите число!")
    rook = False
    if (k == m) or (l == n):
        rook = True
    elephant = False
    if (k == l) and (m == n):
        elephant = True
    horse = False
    if ((k + 1 == m) and (l + 2 == n)) \
            or ((k - 1 == m) and (l + 2 == n)) \
            or ((k + 2 == m) and (l + 1 == n)) \
            or ((k + 2 == m) and (l - 1 == n)) \
            or ((k + 1 == m) and (l - 2 == n)) \
            or ((k - 1 == m) and (l - 2 == n)) \
            or ((k - 2 == m) and (l - 1 == n)) \
            or ((k - 2 == m) and (l + 1 == n)):
        horse = True
    pawn = False
    if ((l == 2 and k == m) and (n == l + 1 or n == l + 2)) or (k == m and l + 1 == n):
        pawn = True
    print("Ладья - ", rook)
    print("Слон - ", elephant)
    print("Конь - ", horse)
    print("Пешка - ", pawn)
