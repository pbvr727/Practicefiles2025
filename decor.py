# def decor(func):
#     def inner(name):
#         if name=="balaji":
#             print("Welcome to Hyderabad")
#         else:
#             return func(name)
#     return inner

# @decor
# def simple(name):
#     print("Hellio",name)
# simple("balaji")
# simple("raavi")
import re
count=0
# pattern=re.compile("is")
# m=pattern.finditer("ThIsisconfuse")
m=re.finditer("s","ThIsisconfuse")
for i in m:
    count=count+1
print(count)
# l=[i*i for i in range(510)]
# print(l)
# s="A2B6C5P9"
# s1=""
# s2=""
# l=""
# for i in s:
#     if i.isalpha():
#         s1=i
#     else:
#         s2=s1*int(i)
#         l=l+s2
#         print(l)
# n=int(input("input enter n number:"))
# temp=n
# r=0
# while 0<n:
#     digi=n%10
#     r=r*10+digi
#     n=n//10
# if temp==r:
#     print("Palindrome")
# else:
# #     print("Not palindrome")
# n=int(input("Enter n number:"))
# flag=False
# l=[]
# if n<=1:
#     print("1")
# else:
#     for i in range(2,int(n**0.5)+1):
#         if i%n==0:
#             flag=True
#             break
#     else:
#         l.append(i)
# print(l)           
# if flag:
#     print("Not pime")
# else:
#     print("prime")
# n=int(input("enter n number"))

# l=str(n)
# l1=len(l)
# k=0
# for i in l:
#     k=k+int(i)**l1  
# print(k)
# if n==k:
#     print("Armsong number")
# else:
#     print("Not Arm sronf")
        
    
