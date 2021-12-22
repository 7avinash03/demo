#python program to print sub string between two sub strings
"""

Program No.        :
Program Name    :sub_string.py
Author                 :Avinash
Topics                   :Strings

s=input("Type the main string :")
a=input ("Type the first sub string :")
b=input("Type the second sub string:")
sl=len(s)
al=len(a)
bl=len(b)
c=""
for g in  range(int(s.index(s.index(a)+al)),int(s.index(s.index(b)+bl))):
    
    c.append(s[g])
print("The substring between two substrings is :{0}".format(c))
"""

s=input("Type the main string :")
a=input ("Type the first sub string :")
b=input("Type the second sub string:")
sl=len(s)
al=len(a)
bl=len(b)
c=""+s[s.index(a)+al:s.index(b)]
#c.append(string(s[s.index(a)+al:s.index(b)]))
print("The substring between two substrings is :{0}".format(c))

