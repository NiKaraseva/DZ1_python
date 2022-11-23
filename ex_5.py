# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21


print('Введите координату X точки A: ')
XA = float(input())
print('Введите координату Y точки A: ')
YA = float(input())
print('Введите координату X точки B: ')
XB = float(input())
print('Введите координату Y точки B: ')
YB = float(input())

print(f'Расстояние между точками A {(XA, YA)} и B {(XB, YB)} = {round((((XB - XA)**2) + ((YB - YA)**2))**(1/2), 2)}')