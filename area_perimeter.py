#python program to create two methods which caluclate area and perimeter
"""
Program No.      :
Program Name  :
Author                :Avinash
Topics                 :
"""
def area(l,b):
    area_=l*b
    print("{0} is area when length and breadth are {1} and {2} respectively".format(area_,l,b))
def perimeter(l,b):
    perimeter_=2*(l+b)
    print("{0} is perimater when length and breadth are {1} and {2} respectively".format(perimeter_,l,b))
#Drive code
a=float(input("Enter the length of rectangle :"))
b=float(input("Enter the breadth of rectangle :"))
area(a,b)
perimeter(a,b)    
