r=10
c=10
c1=r-1
for i in range(r):
    for j in range(c1-i):
        print(" ",end=" ")
    for k in range(10):
        print("*",end=" ")
    print()
r=15
# c=6
# c1=r+1
# for i in range(r):
#     for j in range(c1-inn):
#         print("",end="")
#     for k in range(c):
#         print("#",end="")
#     print()
# r=5
# c=10
# c1=4
# for i in range(r):
#     for j in range(c1-c):
#         print(" ",end=" ")
#     for k in range(r-c1+i):
#         print("&",end=" ")
#     print()
# n=4
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     for k in range(i):
#         print("v_",end="")
#     print()
# for i in range(5):
#     for j in range(3-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("l",end=" ")
#     print()
my_list = [10, 20, 4, 45, 99,-1]
for i in range(len(my_list)):
    for j in range(0,len(my_list)-i-1):
        if my_list[j]>my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
print(my_list)

for i in range(11):
    for j in range(0,11-i):
        print(" ",end=" ")
    for k in range(10):
        print("#",end="")
        for n in range(10-i):
            print("B",end=" ")
    print()
p=[2,4,3,1,6,9,8,7,5]
for i in range(len(p)):
    for j in range(0+i,len(p)):
        if p[i]>p[j]:
            p[i],p[j]=p[j],p[i]
print(p)


