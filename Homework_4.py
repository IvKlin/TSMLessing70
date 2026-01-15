# # Задача 1
# tup = (1, 2,3,4,5,6,7,8,9)
# dif = max(tup) - min(tup)
# print('Разность =', dif)
#
# # Задача 2
# tup = (5, 2, -2, 7, -8, -9, 1)
# changes = 0
# for i in range(1, len(tup)):
#     if tup[i] * tup[i-1] < 0:
#         changes += 1
# print("Количество смен знака:", changes)
#
# #Задача 3
# tup = (5, 2, -2, 7, -8, -9, 1, 11, 15, 17, 0)
# for i in tup:
#     if i < 2:
#         continue
#     prime = True
#     for d in range(2, int(i**0.5) + 1):
#         if i % d == 0:
#             prime = False
#             break
#     if prime:
#         print(i, end=' ')

# #Задача 6
# list_1 = [4, 1, 6, 9]
# list_2 = [8, 1, 2, 4, 9, 5, 7, 6]
# diff = [x for x in list_1 if x not in list_2]
# if diff:
#     print(min(diff))
# else:
#     print('нет такого элемента')

# #Задача 7
# list_1 = [18, 42, 8, 122]
# reverse = lambda n: int(str(n)[::-1])
# new_list = []
# for i in list_1:
#     new_list.append(i)
#     if i % 2 == 0:
#         new_list.append(reverse(i))
# print(new_list)

# #Задача 8
# list_1 = [5, 2, 4, 5, 1, 2]
# count = {}
# for item in list_1:
#     count[item] = count.get(item, 0) + 1
# for val, cnt in count.items():
#     print(f'{val} – {cnt}')

# #Задача 11
# nums = input().split()
# seen = set()
# for n in nums:
#     print('YES' if n in seen else 'NO')
#     seen.add(n)

# #Задача 12
# n = int(input())
# ok = set(range(1, n+1))
# while True:
#     q = input().strip()
#     if q == 'HELP': break
#     nums = set(map(int, q.split()))
#     ans = input().strip()
#     if ans == 'YES':
#         ok &= nums
#     else:
#         ok -= nums
# print(*sorted(ok))

# # Задача 13
# school = {'9а': 28, '9б': 31, '9в': 29, '9м': 27, '9ф': 30}
# school['9б'] = 33
# school['9к'] = 26
# del school['9м']
# total = sum(school.values())
# print('Всего учащихся 9-х классов:', total)
