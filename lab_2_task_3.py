a= int(input())
if (a%4==0 and a%100!= 0) or (a%400 == 0):
  print(f'год будет високосным')
else:
  print(f'год не будет високосным')