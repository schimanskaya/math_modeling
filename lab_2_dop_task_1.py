print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a =int(input("a = "))
b =int(input("b = "))
c =int(input("c = "))

d = b**2 - 4*a*c
print(f' дискриминант = :', d )
if d > 0:
  x1 = ((-b + (d**0.5)) / (2*a))
  x2 = ((-b - (d**0.5)) / (2*a))
  print(f'x1 ={x1} x2 ={x2} ')
elif d == 0:
  x = -b / (2 * a)
  print(f'x = :', x)
else:
  print("Корней нет")