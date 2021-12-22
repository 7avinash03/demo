#python program to find factorial of given number using recursive function
"""
Program No.      :
Program Name  :
Author                :Avinash
Topics                 :
"""
def factorial(n):
    factorial(1)=1
    print(n)
    while(n!=0):
        factorial_=n*int(factorial(n-1))
        print(factorial_)

a=int(input("Enter the positive integer :"))
factorial(a)    
