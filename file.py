
#Task 1
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(int(input("enter the value of number")))
print(result) 

#Task2
n=int(input('enter the number'))
from math import*
print(f'square root:{sqrt(n)}')
print(f'logarithm:{log10(n)}')
print(f'sine:{sin(n)}')





