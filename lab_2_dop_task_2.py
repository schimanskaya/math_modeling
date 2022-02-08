a =int(input("a = "))
b =int(input("b = "))
c =int(input("c = "))
if a+b <= c and b+c <= a and c+a <= b:
  print(" такой треугольник не существует")
elif a != b and a != c and b != c:
  print (" разносторонний треугольник")
elif a==b and b==c and c==a:
  print ("равносторонний треугольник")
else:
  print("равнобедренный треугольник")