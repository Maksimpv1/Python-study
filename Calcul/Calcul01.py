from colorama import init
from colorama import Fore, Back, Style
init()

print ( Back.GREEN )
#Слабый калькулятор

step1 = input("Выбор функции +\-")

print ( Back.CYAN )

a = float(input("Введите первое число: "))
b = float(input("Ведите второе число: "))

if step1 == "+":
    c = a + b
    print ( Back.YELLOW)
    print("Результат: " + str(c))
elif step1 == "-":
    c = a - b
    print ( Back.YELLOW)
    print("Результат: " + str(c))
else:
    print("Нету такой функции!")

input() 