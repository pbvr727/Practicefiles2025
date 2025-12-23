#how to swap variables
# a=10
# b=12
# a,b=b,a
# print(a,b)
# import datetime,time
# def decor(func):
#     def inner(name):
#         if name!="siva":
#             print("hello")
#             time.sleep(3)
#             print("decor")
#         return func(name)
#     return inner

# @decor
# def add(name):
#     dt=datetime.datetime.now()
#     print("hi",dt)
# print(add("balaji"))
# # print(add("siva"))
l=[1,2,3,4,5,6,7,9]
f=lambda x,y:x*y
print(f(2,4))
k=list(map(lambda x:x*x,l))
print(k)
e=list(filter(lambda x:x%2!=0,l))
print(e)
from functools import reduce
g=reduce(lambda x,y:x+y,l)
print(g)
a=15;b=19
a=a+b
b=a-b
a=a-b
print(a,b)
print("Hello1")