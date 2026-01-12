# #Задача №1
# num = input ('Введите число: ' )
# if num [-1] == "3":
#     print(True)
# else:
#     print(False)

# #Задача №2
# num_a, num_b, num_c = int (input("Введите число A: ")), int (input('Введите число B: ')), int (input('Введите число C: '))
# if num_a < 0:
#     print (str("Число А: True"))
# else:
#     print (str("Число A: False"))
# if num_b < 0:
#     print (str("Число B: True"))
# else :
#     print (str("Число B: False"))
# if num_c < 0:
#     print (str("Число C: True"))
# else:
#     print (str("Число C: False"))

# #Задача 3
# num_1 = int(input("Введите число 1: "))
# num_2 = int(input("Введите число 2: "))
# print ((num_1 % 2) == (num_2 % 2))

# #Задача 4
# num = int(input("Введите двухзначное число: "))
# sum = num // 10 + num % 10
# if 10 <= sum <= 99:
#     print ("да")
# else:
#     print ("нет")

# #Задача 5
# num = input ("Введите четрыхерзначное число: ")
# print (len (set(num)) == 1)

# #Задача 6
# str_1 = input("Введите строку: ")
# print (str_1 [2])                 # выводит третий символ
# print (str_1 [-2])                # выводит предпоследний символ
# print (str_1 [:5])                # выводит первые пять символов
# print (str_1 [:-2])               # выводит строку без последних двух символов
# print (str_1 [::2])               # выводит чётные индексы
# print (str_1 [1::2])              # выводит нечётные индексы
# print (str_1 [::-1])              # выводит строку в обратном порядке
# print (str_1 [::-2])              # выводит значения через один в обратном порядке
# print (len (str_1))               # выводит длинну строки

# #Задача 7
# word = input ("Введите слово: ")
# print (word[0] == word[-1])

# #Задача 8
# str_1 = input ("Введите строку: ")
# print (str_1 == str_1[::-1])

# # #Задача 9
# str_1 = input("Введите строку: ")
# count = str_1.count("f")
# if count == 1:
#     print(str_1.find("f"))
# elif count >= 2:
#     print(str_1.find("f"), count)

# #Задача 10
# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# print((x1 + y1) % 2 == (x2 + y2) % 2)