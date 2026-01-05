#list sort
l=[5,2,35,0,6,4,11,10]
# for i in range(len(l)):
#     for j in range(0,len(l)-1-i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)
##############################################################################
#list minimum and maximum find
# c=0
# for i in range(len(l)):
#         if l[i]<c:
#             c=l[i]
# print(c)
######################################################################
#Two Sum
#nums = [2,7,11,15], target = 9  
# nums=[3,3]  
# target=6
# for i in range(len(nums)):
#     for j in range(i,len(nums)-1):
#         if nums[j]+nums[j+1]==target:
#             print(j,j+1)
##############################################################################
#Palindrome Number
# n=int(input("enter n number:"))
# temp=n
# r=0
# while (n>0):
#     digi=n%10
#     r=r*10+digi
#     n=n//10
# if temp==r:
#     print("palindome")
# else:
#     print("not palilndrome")
#######################################################
# #longest common prefix
# d=""
# sr=["fllower","fly","flight"]
# for i in range(len(sr)):
#     for j in range(2):
#         if sr[i][j]:
#             d=d+sr[i][j]
#             print(d)
#     print()
s="puvvada bala venkata ramanjaneyulu"
# s1=len(s)
# c=0
# for i in range(s1-1):
#     c1=abs(ord(s[i])-ord(s[i+1]))
#     print(c1,end=" ")
#     c=c+c1
# print(c)
# d=[1,2,3,4]
# for i in range(len(d)):
#     print(i,"i value")
#     for j in range(i+1,len(d)+1):
#         print(d[i:j])
# s="puvvada"
# s1=len(s)
# c=0
# for i in range(s1):
#     for j in range(i+1,s1+1):
#         print(s[i:j],end=" ")
#         c=c+1
# print(c)
# l=[5,9,1,8,7]
# length=3
# l1=len(l)
# f=0
# for i in range(l1):
#     for j in range(i+1,l1+1):
#         d=0
#         k=l[i:j]
#         if len(k)==length:
#             print(k)
#             p=sum(k)
def fun(s):
    c=0
    for i in range(len(s)):
        for j in range(i,len(s)+1):
            #print(s[i:j],end=" ")
            if len(s[i:j])==2:
                c=c+1
                print(s[i:j],end=" ")
                print(c)

s="Rama s"
fun(s)

           
    





