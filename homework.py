import sys


def check():
    print("\nПерезапустить программу?\nY/N")
    while True:
        string = input()
        if string == "Y":
            return True
        elif string == "N":
            sys.exit(0)


while True:
    print("Введите коэффициенты квадратного уравнения\n")
    try:
        a, b, c = list(map(int, input().split()))
    except ValueError:
        print("Некорректно введены коэффициенты уравнения.\n")
        if check(): continue
    if not a:
        print("Уравнение не квадратное или не существует.\n")
        if check(): continue
    D = (b ** 2) - (4 * a * c)
    if D >= 0:
        x1 = ((-b + D ** 0.5) / (2 * a))
        x2 = ((-b - D ** 0.5) / (2 * a))
        print("\nКорни уравнения:\nX1 =", x1, "\nX2 =", x2)
        if check(): continue
    else:
        print("Уравнение не имеет корней.\n")
        if check(): continue