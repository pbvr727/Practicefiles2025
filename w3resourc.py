s='w'#Result : 'w3ce'

if len(s)>2:
    print(s[:2]+s[-2:])
else:
    print("empty")
#Replace first char occurrences with $.
S='restart'#Result : 'resta$t'
ch=S[0]
d=S.replace(ch,"$")
print(ch+d[1:])
# print(10//10)
print(0%10)
# l=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in l-1:
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
# a=int(input("enter a number:"))
# t=a
# r=0
# while a>0:
#     d=a%10#4
#     r=r*10+d
#     print(r,"r value")
#     a=a//10
#     print(r)
# if t==r:
#     print("palindrome")
# else:
#     print("not")
di={1:10,2:11,3:20}
di[2]=6
print(di[2])

