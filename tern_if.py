a, b = (int(input()) for _ in 'xx')
print('<' if a < b else '>' if a > b else '=')


d = int(input()) - int(input())
print('<=>'[(d >= 0) + (d > 0)])



a, b, c = int(input()), int(input()), int(input())
print(a if b < a > c else b if a < b > c else c )

#выводит максимальное число из 3х введенных


n = int(input())
print(n // 2 if not n % 2 or n == 1 else n)

#На свой день рождения Петя купил красивый и вкусный торт, который имел идеально круглую форму. Петя не знал, сколько гостей придет на его день рождения, поэтому вынужден был разработать алгоритм, согласно которому он сможет быстро разрезать торт на N равных частей. Следует учесть, что разрезы торта можно производить как по радиусу, так и по диаметру.
#Помогите Пете решить эту задачу, определив наименьшее число разрезов торта по заданному числу гостей.
#Входные данные
#Программа получает на вход натуральное число N – число гостей, включая самого виновника торжества
#Выходные данные
#Выведите минимально возможное число разрезов торта.
