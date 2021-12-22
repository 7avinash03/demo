#python program to solve quadratic equations
"""
Program No.          :lab1.1.py
Program Name      :Quadradic.py
Author                    :Avinash
Topics                     :conditional statements  
"""
a=int (input("Enter the coefficeint of  x**2 :"))
b=int( input("Enter the coefficient of  x :"))
c=int(input("Enter the constant value :"))
if(a!=0):
    k1=-b+(b**2-4*a*c)**0.5
    k2=-b-(b**2-4*a*c)**0.5
    print("The solutins of given quadratic equation are ",k1/2*a,k2/2*a)
else:
    print("Entered  coefficents doesn't form the quadradic equations")
    
