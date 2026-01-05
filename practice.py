# l=[-100,10,8,9,5,10,6,3,2,1,0,-1,-2,100,500]
# for i in range(len(l)):
#     for j in range(i,len(l)-1-i):
#         if l[j]>l[j+1]:
#             print(l[j],l[j+1],end=" ")
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)
# s="011101"
# rs=""
# ls=""
# count,count1=0,0
# for i in range(len(s)):
#     if s[i]=='0':
#         ls=s[i]
#         count=count+1
#         print("ls",count)
#     else:
#         rs=s[i]
#         count1=count1+1
#         print("rs",count)
# print("rs",count+count1)
# code = [5,7,1,4] 
# t=3
# #Output: [12,10,16,13]
# s=0
# for i in range(len(code)):
#     for j in range(len(code)-1,i,-1):
#         s=code[j]+s
#         print(s)

# count=1
# # Output: 4
# def sub(sentence,searchWord):
#     sl=sentence.split()
#     for i,k in enumerate(sl,start=1):
#         print(i,k)
#         if k.startswith(searchWord):
#             return i
#     return -1
# sentence = "i love eating burger"
# searchWord = "balajipuvvada"
# print(sub(sentence,searchWord))
#Fair Pairs
# nums = [0,1,7,4,4,5]
# lower = 3
# upper = 6
# l1=len(nums)
# for i in range(l1):
#     for j in range(i+1,l1):
#         if lower<=nums[i]+nums[j]<=upper:
#             print(i,j)
# w="BALAJI"
# f=False
# for i in w:
#     if w.isupper():
#         f=True
# if f:
#     print("lower")
# else:
#     print("sb")
# s="puvvada bala venkata ramanjaneyulu"
# for i,k in enumerate(s,start=1):
#     print("index=",i,"k=",k)
# a=1,00,000
# print(type(a))
# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         print("N",n)
#         result=n*fact(n-1)
#         print(result)
#     return result
# print(fact(5))
# l=[1,2,3,4,5,6,7,7,7,8,8,8,7,5,6]
# d={}
# for i in range(len(l)):
#     if l[i] in d:
#         d[l[i]]+=1
#     else:
#         d[l[i]]=1
# print(d)
# x=len(l)//2
# print(x)
# a=0
# for j in d:
#     v=d[j]
#     if v>=x:
#         a=v
#         break
# print(a)
# for i in range(5):
#     for j in range(7):
#         if i==0 or i==4 or j==0 or j==6:
#             print("*",end=" ")
#     print()
from math import gcd
# str1 = "ABCABC"
# str2 = "ABC"
# output="ABC"

# if str1+str2==str2+str1:
#     g=gcd(len(str1),len(str2))
#     print(g)
#     print(str1[g:])
# else:
#     print("")

# s1="puvvada"
# r=len(s)
# r1=len(s1)
# r2=r-r1
# print(r2)
# print(s[:r2])
# s="ACT"
# s1="CAT"
# a=0
# for i in s1:
#     print(ord(i))
#     if ord(i)>=a:
#         a=ord(i)
#     print(chr(a))


# s2=sorted(s)
# s3=sorted(s1)
# j="anagram" if s2==s3 else "not"
# print(j)
l=[10,8,5,4,7,9,2,1,0,11]
# for i in range(len(l)):
#     for j in range(0,len(l)-1-i):
#         if l[j]<=l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
#     print(l)
for i in range(len(l)):
    for j in range(i,len(l)-1):
        if l[i]<l[j+1]:
            l[i],l[j+1]=l[j+1],l[i]
print(l)








    

   