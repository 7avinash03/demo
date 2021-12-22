#python program to convert the list elements into dictionary
"""
Program No.        :
Program Name    :dictionary.py
Author                 :Avinash
Topics                   :List,List Comprehension,Dictionary
"""
l=[3,4,"rt","dfg",34,"34","56",23]
print("The original list is :",l)
d={}
for i in range(0,len(l)-1):
    if(i%2!=0):
        d[l[i]]=l[i-1]


print("The required dictionary is :",d)     
