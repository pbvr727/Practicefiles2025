s2 = "A geek in need is a geek indeed"
s1 = "geek"
# if s2.find(s1)!=-1:
#     print("sub")
# else:
#     print("no sub")
# i="sub" if s2.find(s1)!=-1 else "no sub"
# print(i)
#Regular expressions
# import re
# if re.search(s1,s2):
#     print("avail")
# else:
#     print("unavail")
# test_list1 = ["Gfg", "is", "Best"]
# test_list2 = ["I love Gfg", "Its Best for Geeks", "Gfg means CS"]
# s1=set(test_list1)
# s2=set(" ".join(test_list2).split())
# s3=s1.intersection(s2)
# l2=list(s3)
# r1=[]
# for i in test_list1:
#     if i in l2:
#         r1.append(True)
#     else:
#         r1.append(False)
# print(r1)
#All substrings Frequency in String
# test_str="ababa"
# di={}
# for i in range(len(test_str)):
#     for j in range(i+1,len(test_str)+1):
#         sub=test_str[i:j]
#         print(sub)
#         if sub in di:
#             di[sub]=di[sub]+1
#         else:
#             di[sub]=1
# print(di) 
# s3="ababa"
# for i in range(6):
#     for j in range(i+1,7):
#         print(i,"i","j",j)
#         print(s3[i:j])
#     if 
##
# s="geeksgeeks"
# print(s.count("geeks"))
# test_str = 'geeksgees are geeks for all geeksgeeksgeek'
# sub_str = 'geeks'
# count=0
# sd=""
# word=test_str.split()
# for i in word:
#     print(i)
#     f=i.count(sub_str)
#     if f>=count:
#         count=f
#         sd=count*sub_str
# print(sd)
# for i in [0, 1]:
#      for j in [0, 1]:
#          for k in [0, 1]:
#             for m in [2,1]:
#              print((i, j, k,m,"forloops"))
# import itertools
# import datetime
# for i in itertools.product([0,1],[0,1],[0,1],[2,1]):
#     print(i)
# print(datetime.datetime.now())
s="abcabcabcbb"
d={}
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        t=s[i:j]
        print(t)
        if t in d:
            d[t]+=1
        else:
            d[t]=1
print(d)
# s = "GeeksforGeeks is an awesome website."
# a = ["Geeks", "awesome"]
# for i in a:
#     s=s.replace(i,"")
#     print(s)





        






