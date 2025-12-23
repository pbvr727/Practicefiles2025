import re
# # reobj=re.compile("a")
# x="[^\.]"
# p=re.finditer(x,'balaji123@')
# c=0
# for i in p:
#     c=c+1
#     print(i.start(),"stat",i.end(),"end",i.group(),"group")
# print(c)
n=input("enter n number:")
rec=re.fullmatch("[7-9]\D{9}",n)
if rec:
    print("print match")
else:
    print("not print match")
print("jj")

