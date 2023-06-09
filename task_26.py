#Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# Определение функции:

def pow(n, m):
    k = int (m)                           # определение целой части для показателя степени
    if k == 0:                            # если показатель степени равен 0, то результат всегда равен 1
        return 1
    elif k > 0:                           # если показатель степени положительный 
        return n * pow(n, k - 1)
    else:                                 # если показатель степени отрицательный
        return float (1/n) * pow(n, k + 1)
    
# Расчет и вывод результата

print()
print('- - - Возведение числа в целую степень - - -')
print()
a = float (input('Введите число: '))
b = float (input('Введите число для определения степени: '))
print()
print('Результат возведения числа %s в степень %s равен %s' % (a, int (b), round (pow(a, b),2)))