# num=[3,2,3,5,5,5,10,10,10,5,5]
# d={}
# for i in  num:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)
# o=len(num)//2
# a=0
# for j in d:
#     val=d[j]
#     if val>=o:
#         a=j
#         print(a)
#         break
# for i in d:
#     temp=d[i]
#     if temp<len(d)//2:
#         temp=i
#     print(i)
# l=[1,2,3,4,1,2,3,4,5,1,2,1,2,1,2,1,2,1]
# for i in range(len(l)):
#     for j in range(0,len(l)-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)
#Number of Good pairs
# l=[1,2,3,1,1,3]
# #op=4 condition num[i]==num[j] and i<j
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]==l[j] and i<j:
#             print(i,j)
# l=[5,5,5,5,5,5,5,5,5,5,5]
# l1=len(l)
# k=l1-1
# j=k*(k+1)//2
# print(j)
nums=[5,5,5,5,5,5,5,5,5,5,5]
dici={}
for i in range(len(nums)):
    if nums[i] in dici:
        dici[nums[i]]+=1
    else:
        dici[nums[i]]=1
print(dici)
a=0

for j in dici:
    v=dici[j]
    print(v)
    a=v*(v+1)//2
print(a)
# j="aAbg"
# s='aAAbbbb'
# d={}
# for i in range(len(s)):
#     if s[i] in d:
#         d[s[i]]+=1
#     else:
#         d[s[i]]=1
# print(d)
# o=0

# for k in range(len(j)):
#     ch=j[k]
#     if ch in d:
#         o=o+d[ch]
# print(o)

# s="the quick brown fox jumps over the lazy dog"
# d={}
# v=97
# for i in s:
#     if i!=" " and i not in d:
#         d[i]=chr(v)
#         v=v+1
# print(d)
# msg="nx ftnu bs htwt"
# a=""
# for j in msg:
#     if d[j]==" ":
#         a=a+" "
#     else:
#         d[i]=d[j]
#         a=a+d[i]
# print(a)
# for i in range(6):
#     for j in range(6-i):
#         print(chr(65+j),end="")
#     print()
# l=[1,4,2,5,3]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
  
# print(l2)
