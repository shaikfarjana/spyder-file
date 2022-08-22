# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

data=pd.read_csv('cars.csv')

zaara = "zeeshan"

print(zaara)

print(zaara,2,3)

print(type("farzana"))

print(type(3))

print(type(1.5))

# list

x=[45,20,"zaara",6]

print(x[0])

print(x[0:2])

for i in range(1,20):
    print(i)

    
for i in range(0,22,2):
    
    print(i)
for i in range(1,22,3):
    
    print(i)
a=1
b=2

if a>b:
    print('greater')
elif b==a:
    print('equal')
else:
    print('b is greater')
# Loops
# For loop

# for i in range(0,9):
#     print(i)

for i in x:
    print(i)
    if i==45:break

y=0
while True:
    print('a')
    y=y+1
    if y==5:break
string="my daughter is a good girl"
for x in string:
    if x=='g':
        continue
    print(x)

students=['zaara','zeeshan','maahir','mehak']
for value in students:
    print(value)
for v in range(1,100):
    print(v)
    print(students[1:3])
students.append('jumaina')
print(students)
students[1:3]=['zoha','zoya']
print(students)
NUMBER=10;
number=20
print(NUMBER)
print(number+NUMBER)
print("feroz")
print('feroz')
print('feroz'+"farzana")
print('feroz',5)
print('feroz'+str(5))


starter=1
while starter<10:
    print("here")
    starter+=1
    