"""
Здесь, в этом файле, мы будем писать синтаксис питона
"""
import math
import turtle

# так мы будем оформлять комментарии

variable = 100

print(variable**2 + 13)
print(variable*13 + 16)
age = 26

print(f"Наш ответ номер один:  {variable**2+25}. Мне сколько-то лет {age}")
print("Наш ответ номер один: ", variable**2+25)

seconds_in_min = 60
mins_in_hour = 60
hours_in_day = 24
days_in_year = 365

seconds_in_year = seconds_in_min * mins_in_hour * hours_in_day * days_in_year
print(f"Количество секунд  году: {seconds_in_year}")

#Необычная арифметика Питона
our_number = 42

print(our_number**2) #число в квадрате
print(our_number**3) #число в кубе

print(our_number / 7) #делим наше число на 7
print(our_number * 10) #умножаем число на 10

print(our_number // 10) #целочисленное деление, целая часть от деления
print(our_number % 10) #остаток от деления на 10

our_number = our_number + 1

our_number += 2

print(math.pi)

our_sine = round (math.sin(math.pi),6)
our_cosine = round(math.cos(math.pi),6)

print(f"Наш родной синус: {our_sine}")
print(f"Наш родной Косинус: {our_cosine}")

#Поговорим про типы данных
my_name = "John Johnson"
my_age = 42
my_city = "Moscow"
my_wine = 2.5

first_row_group = [
    'Максим', 
    'Даша', 
    'кристина', 
    'Ваня'
    ]
second_row_group = [
    'Олег', 
    'Сергей', 
    'Сергей', 
    'Радмила', 
    'Саша', 
    'Надя'
    ]

print(type(my_name))
print(type(my_age))
print(type(my_city))
print(type(my_wine))

print(type(first_row_group))
print(type(second_row_group))

my_secret_system = {
    0:"Выходи",
    1:"не выходи",
    2:"пей",
    3:"Читай книгу",
    4:"спи",
    5:"учись"
}

type(my_secret_system)

print(my_secret_system[0])
print(my_secret_system[1])

# тест имени
student_name = "Ясельский Алексей Анатольевич"
smth = student_name.split()

print(type(smth))

print(smth[0])
print(smth[1])
print(smth[2])
print(len(smth))

other_list = smth[:2]
other_list = smth[-2:]

print("Hello World!")