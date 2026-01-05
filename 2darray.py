# k=[[1,2,3],[9,8,7],[3,5,6]]
# print(k[0][2])
# for i in range(len(k)):
#     for j in range(3):
#         print(k[j])
# for i in range(3):
#     print(k[i][0])
k=["balaji","ommm","sita"]
for i in range(len(k)):
    print(k[i],end=" ")
# for i in range(5):
#     for j  in range(5):
#         print("*",end="_$")
#         if j!=4:
#             print("-",end="")
#     print()
# s="Bala venkata ramanjaneyulu"
# print(s.split())
# for i in s.split():
#     print(i)
# for i in range(5):
#     for j in range(4):
#         print("*",end="_")
#         if j==1:
#             print("*",end=" ")
#     print(" ")
# r=3
# c=15
# for i in range(6):
#     for j in range(30):
#         print("*",end="_")
#     print()
# r=20
# c=5
# for i in range(r):
#     for j in range(c):
#         print("*",end="_")
#     print()
# r=4
# c=4
# for i in range(r):
#     for j in range(c):
#         if i==0 or j==c-1 or i==r-1 or j==0:
#                     print("*",end="")
#         else:
#                     print("",end=" ")
#         if j!=c-1:
#             print(" ",end="")
#     print()
# r=3
# c=10
# for i in range(r):
#     for j in range(c):
#         if i==0 or j==c-1 or i==r-1 or j==0 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
for i in range(5):
    for j in range(5,9):
        if i!=4 and j<=4:
            print("*",end=" ")
    print()