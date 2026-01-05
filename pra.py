# #Sort Python Dictionary by Key or Value
d = {'ravi': 9, 'rajnish':10, 'sanjeev': 15}
# print(len(d),"total dixtionary")
# print(len(d.keys()))
# print(len(d.values()))
# k=list(d.keys())
# v=list(d.values())
# print("k",k,"v",v)
# for i in range(len(v)):
#     for j in range(0,len(v)-1-i):
#         print(i,j)
#         if v[j]>v[j+1]:
#             print(v[j])
#             v[j],v[j+1]=v[j+1],v[j]
# print(v)
# for i in range(len(k)):
#     for j in range(0,len(k)-1):
#         if k[j]>k[j+1]:
#             k[j],k[j+1]=k[j+1],k[j]
# print(k)
# # print(dict(zip(k,v)))

# for i in k:
#     i=d[i]
# print(d)
# d = {'ravi': 9, 'rajnish':10, 'sanjeev': 15}
from collections import defaultdict
d1=defaultdict(list)
d1['Sneha'].append("bala")
d1['Sneha'].append("balaji")
d1=defaultdict(int)
d1['priyamani']=10
d1['priyamani1']=13
d1["roja"]
print(d1)
# from collections import defaultdict
# input={1:'a',2:'a',3:'b',5:'a'}
# input1=defaultdict(list)
# #output={'a':[1,2],'b':3}
# for k,v in input.items():
#     print(k,":",v)
#     input1[v].append(k)
#     if len(input1)<1:
#         print(input1)
# print(input1)
# # sentence = "apple banana apple orange banana apple"
# c=defaultdict(int)
# for i in sentence.split():
#     c[i]+=1
# print(c)
def decor(func):
    def inner(name,name1):
        if name=="bala":
            print(name+name1)
        else:
            return func(name,name1)
    return inner
@decor
def add(name,name1):
    print(name,name1)
add("bala","rama")
add("sita","ram")
def gen(n):
    for i in range(n):
        yield i
c=gen(5)
for i in range(c):
    print(type(i))









