from hw.my_calc import *
import time


#4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     #периметр квадрата, площадь квадрата и диагональ квадрата.

def calculator(a):
    per=a*4
    sq=a**2
    diag=(2*a**2)**(1/2)
    result=(per,sq,diag)
    return result
#print(calculator(2))

#4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
   #  в формате аргумент: значение. Например:
	#name: John
	#last_name: Smith
	#age: 35
	#position: web developer

def print_args(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {str(value)}')

#print(print_args(name='Ваня',age=50,salary='3000$'))


#4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
    # положительные числа
my_list = [20, -3, 15, 2, -1, -21]
list_final = list(filter(lambda x: x >= 0, my_list))
#print(list_final)

#4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
from functools import reduce
result=reduce(lambda x,y:x*y,list_final)
#print(result)

#4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
def timer(func):
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} выполнился за {round(runtime,3)} секунд")
        return result
    return _wrapper

@timer
def currency_translator(dollars,rubles):
    '''Функция принимает 2 аргумента:
    dollars- кол-долларов,
    rubles- курс доллара в рублях,
    и возвращает доллары конвертированные в рубли'''
    time.sleep(3)
    return dollars*rubles

#print(currency_translator(1.5,70))

#4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#     Примените эти функции в качестве методов в другом файле.

object = Methods()
b = object.mult(2,2)
print('b=',b)
c = object.summator(5,-5)
print('c=',c)
z = b+c
print('z=',z)
h = object.div(6,0)
print('h=',h)