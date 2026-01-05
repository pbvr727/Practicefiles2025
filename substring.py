#Bruteforce mechanisum
s="xyzzaz"
# count=0
# for i in range(len(s)):
#     for j in range(i+3,len(s)+1):
#         d=s[i:j]
#         if len(d)==3:
#             x=set(d)
#             if len(x)>=3:
#                 print(x)
#                 count=count+1
#             print(count)
#Sliding window
s = "aababcabc"
s="xyzzaz"
s1=len(s)

# lis=[]
# l=0
# c=0
# for i in range(s1):
#     lis.append(s[i])
#     # print(lis)

#     if i-l==3:
#         lis.pop(0)
#         l+=1
#         c=c+1
#     # print(lis,"count",c)
#     if i-l+1==3:
#         print(lis)
di={}
l=0
for i in range(s1):
    if s[i] in di:
        di[s[i]]+=1
    else:
        di[s[i]]=1
    print(di)
    if i-l==3:
        di[s[i]]-+1
        if di[s[l]]==0:
            di.pop(di[s[l]])    
            l+=1
        print(di)
    if i-l+1==3:
        print(di)
    





      

    