#python program to find positive tuples in lists
"""
Program No.        :
Program Name    :positive.py
Author                 :Avinash
Topics                   :List,Tuples
"""
a=[(2,3,-5,0),(33,-8,10),(1,2,3,4,5),(0,0,0)]
print("The original list is :",a)
k=[]
"""
for i in a:
    l=len(i)
    for j in i:
        if(j<0):
            return break
        k.append(i)
f=[]
for i in k:
    if i not in f:
        f.append(i)
"""
k=[i for i in a if all(j>=0 for j in i)]

print("The modified list is :",k)        
