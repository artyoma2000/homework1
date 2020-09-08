print('Задача 1')
test_number = int(input("Введите тетовую переменную: "))

print(f'Выводим тетовую переменную {test_number}')

test_line = input("Введите тетовую строку: ")

print(f'Выводим тетовую переменную {test_line}')

print('Задача 2')
test_time = int(input("Введите время в секундах: "))

hours = test_time // 3600

print(f'{test_time // 3600}:{(test_time % 3600) // 60}:{test_time % 60}')

print('Задача 3')
number = int(input("введите чило n: "))

print(number + number*11 + number*111)

print('Задача 4')
biggestNumber = int(input('Введите чило для опредиления наибольшей цифры: '))

number_find = 0

while biggestNumber != 0:
    if number_find < biggestNumber % 10:
        number_find = biggestNumber % 10
    biggestNumber = biggestNumber // 10

print(number_find)

print('Задача 5')

profit = int(input('Введите значение выручки: '))

сosts = int(input('Введите значение издержек: '))

if profit > сosts:
    results = profit - сosts
    print('Положительный')
    quantity = int(input('Введите колличетво работников: '))
    print(f'{results / quantity} прибыль на одного работника')
else:
    print('Работаем не в плюс')

print('Задача 5')

first_result = int(input('Введите результат в первый день: '))

run_results = int(input('Введите желаемый результат: '))

days = 1

print(f'В {days}-й день результат составил {first_result} километров')

while first_result < run_results:
    days += 1
    first_result = first_result + first_result*0.1
    print(f'В {days}-й день результат составил {round(first_result, 2)} километров')


