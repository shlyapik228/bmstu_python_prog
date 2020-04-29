# Значения функций при различных x

# Программа выводит все значения z1(x), z2(x) при -1<=x<=1

# Переменные:   x - Аргумент;
#               z1,z2 - Значение функций z1 и z2 соответственно;
#               max - Максимальное значение функции z2;
#               maxa - Максимальное значение аргумента x;
#               y=x/10;
#               n - Порядковый номер значения;

#---------------------------------------
# Примеры:
#---------------------------------------
# При x=-1:
#  z1=-1.5   z2=-20.3  
#---------------------------------------
# При x=0.0:
#  z1=-1.0   z2=-7.1  
#---------------------------------------
# При x=1.0:
#  z1=-0.5   z2=5.1   
#---------------------------------------

from math import cos

x=-10.0
n=1
y=x/10
z2=1.8*y**4+2.6*y**3-2.3*y*y+10.1*y-7.1
max=z2
maxa=-11
print('\n\nПодсчёт значений z1 и z2 при различном аргументе x:\n')
print('┌─────────┬────────────┬──────────┬────────────┐')
print('│  Номер  │ Аргумент x │    Z1    │     Z 2    │')
while x<=10:
    y=x/10
    z1=y-cos(y)
    z2=1.8*y**4+2.6*y**3-2.3*y*y+10.1*y-7.1
    x+=1
    if z2>max:
        max=z2
        maxa=y
    print('├─────────┼────────────┼──────────┼────────────┤')
    print('│{:5d}    │{:9.1f}   │{:9.5f} │ {:9.5f}  │'.format(n,y,z1,z2))
    n+=1
print('└─────────┴────────────┴──────────┴────────────┘')
print('Максимальное значение функции z2:',max)
print('Максимальное значение аргумента x при котором оно достигается:',maxa)
input('\nНажмите Enter для завершения.')
