#Python program to find amstrong number
"""
Program No.     :1.6
Program Name:amstrong.py
Author              :Avinash
Topics              :print statementss
"""
n=int(input("Enter a number :"))
m=n
k=len(str(n))
dup=0
for i in range(k):
    x=int(n%10)
    n=int(n/10)
    dup=dup+x**k
if(dup==m):
    print("{0} is amstrong number".format(m))
else:
    print("{0} is not amstrong number".format(m))



    



    
