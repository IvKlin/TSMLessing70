# # пример 1
# var_1 = 10
# var_2 = 11
# print(var_1 == var_2) #False
# print(var_1 != var_2) #True
# print(var_1 >= var_2) #False
# print(var_1 <= var_2) #True
# print(var_1 > var_2) #False
# print(var_1 < var_2) #True
# print(var_1 is var_2) #False
#
# # пример 2
# var_1 = ['Hello']
# var_2 = ['hello']
# print(var_1 == var_2) #False
# print(var_1 != var_2) #True
# print(var_1 >= var_2) #False
# print(var_1 <= var_2) #True
# print(var_1 > var_2) #False
# print(var_1 < var_2) #True
# print(var_1 is var_2) #False


# # if elif else
# var_1 = 4
# if var_1 > 0:
#     print ('positive')
# elif var_1 == 0:
#     print ('zero')
# else var_1 < 0:
#     print ('negative')
#
# # and и or или not не
# var_1 = - 43
# if var_1 > 0:
#     print ('positive')
#     if 10 <= var_1 <= 99:
#         print ('2 sing number')
#
# elif var_1 == 0:
#     print ('zero')
# else:
#     print ('negative')

str_1 = '0123456789'
length = len(str_1)
print(str_1[10::-1])