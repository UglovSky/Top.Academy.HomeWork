### Задачи на циклы:
from tabnanny import check

# Вывод чётных чисел от 1 до 100:
# Напиши программу, которая выводит все чётные числа от 1 до 100, используя цикл for или while.

a:list = []
for i in range(101):
    if i % 2 == 0:
        a.append(i)
print(a)


# Сумма чисел от 1 до N:
# Напиши программу, которая принимает число N и вычисляет сумму всех чисел от 1 до N.

b:int = int(input("Введите число: "))
summ:int = 0
for i in range(b+1):
    summ += i
print(summ)


# Поиск минимального числа в списке:
# Напиши программу, которая находит минимальное значение в заданном списке чисел с помощью цикла.

num:list = [3,6,8,7,9,5,6]
min_num:list = num[0]
for i in num:
    if i < min_num:
        min_num = i
print(f'Минимальное значение: {min_num}')


# Факториал числа:
# Напиши программу, которая вычисляет факториал числа N с использованием цикла.

c:int = 4
factorial:int = 1
for i in range(c):
    i+=1
    factorial *= i
print(factorial)


# Числа Фибоначчи:
# Напиши программу, которая выводит первые N чисел последовательности Фибоначчи.

n:int = int(input("Сколько чисел последовательности Фибоначчи вы бы хотели получить?: "))
fib1: int = 1
fib2: int = 1
fib_sum: int = 0

print(fib1,fib2, end = ' ')

i = 0
while i < n:
     i+=1
     fib_sum = fib1 + fib2
     fib1 = fib2
     fib2 = fib_sum
     print(fib_sum, end = ' ')

print('') # - *Звуки каких то костылей*, в противном случае принт цепляется к следующей задаче.


### Задачи на срезы:

# Разворот строки:
# Напиши программу, которая принимает строку и выводит её в обратном порядке, используя срез.

# a:str = input("Введите слово: ")[::-1]  # Типа срез, но вроде как надо рекурсию :D
# print(a)

def revers(var:str) -> str:
    if len(var) == 1:
        return var
    else:
        return var[-1] + revers(var[:-1])

n:str = revers('dogs')

print(n)


# Срез списка:
# Напиши программу, которая принимает список и возвращает новый список,
# состоящий из каждого второго элемента оригинального списка.


def create_new_list() -> list:
    letters_list: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    new_letters_list: list = []
    if len(letters_list) == 0:
        return letters_list
    else:
        for i in range(len(letters_list)):
            new_letters_list.append(letters_list[::2])
            return new_letters_list

a = create_new_list()

print(' '.join(map(str, a)))


# Палиндром:
# Напиши программу, которая проверяет, является ли строка палиндромом
# (одинаково читается в обе стороны) с использованием срезов.

def palindrome_check(word:str):                                        # Возвращает False, не могу понять почему
   if len(word) < 1:
       return  True
   else:
       if word == word[::-1]:
           return f'{word} является палиндромом'
       else:
           return False

a:str = palindrome_check('око за око')
print(a)


# Извлечение подстроки:
# Напиши программу, которая принимает строку и два индекса, и выводит подстроку, начиная с первого индекса и заканчивая
# вторым(исключительно), используя срезы.

def line_slice(line: str, index_start: int, index_end: int):    # I need какой-то help, я не понимаю, как это решать через рекурсию
    new_line = line[index_start:index_end]
    return new_line

a:str = line_slice('Фрейя-скандинавская богиня', 0, 10)

print(a)


# Шахматная доска:
# Дан список из строк, представляющих шахматную доску. С помощью срезов напиши программу,
# которая выводит только чёрные клетки (например, элементы с нечётными индексами).

def chess_board() -> list:                                                             # Возвращает None, не могу понять почему
    chessboard:list = ['a9', 'a8', 'a7', 'a6', 'a5', 'a4', 'a3', 'a2', 'a1', 'b9', 'b8',
                       'b7', 'b6', 'b5', 'b4', 'b3', 'b2', 'b1', 'c9', 'c8', 'c7', 'c6',
                       'c5', 'c4', 'c3', 'c2', 'c1', 'd9', 'd8', 'd7', 'd6', 'd5', 'd4',
                       'd3', 'd2', 'd1', 'e9', 'e8', 'e7', 'e6', 'e5', 'e4', 'e3', 'e2',
                       'e1', 'f9', 'f8', 'f7', 'f6', 'f5', 'f4', 'f3', 'f2', 'f1', 'g9',
                       'g8', 'g7', 'g6', 'g5', 'g4', 'g3', 'g2', 'g1', 'h9', 'h8', 'h7',
                       'h6', 'h5', 'h4', 'h3', 'h4', 'h2', 'h1']
    chessboard_black:list = []
    if len(chessboard) == 0:
        return chessboard
    else:
        for index in range(len(chessboard)):
            chessboard_black.append(chessboard[::2])
            return chessboard_black


# Словари

#Создайте программу 'Фирма'. Нужно хранить информацию о человеке:
# ФИО, телефон, рабочий email, название должности, номер кабинета, skype.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.

firm: dict = {
     'name': 'Alexander Shmid',
     'phone_number': 9544323343,
     'email': 'sander@gmail.com',
     'post': 'Самый главный по печенькам',
     'cabinet number': 203,
     'skype': '@sander'
}

def add_info(key: str, value: any):
    if key not in firm.keys():
        firm[key] = value
    else:
        return "Такое значение тут уже есть"


def remove_info(key:str):
    del firm[key]
    return firm


def find_info(key:str):
    return firm.get(key)


def replase_firm_info(key:str, value:any):
    if key in firm.keys():
        firm[key] = value
    else:
        return "Такого значения тут нет"

a:str = add_info('age', 19)
print(a)

b:str = find_info('cabinet number')
print(b)

d:dict = remove_info('name')
print(d)

c:str = replase_firm_info('cabinet number', 100)
print(find_info('cabinet number'))






