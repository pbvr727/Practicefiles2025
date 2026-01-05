# l=[5,9,1,8,7]
# l1=[]
# for i in range(len(l)):
#     for j in range(i+1,len(l)+1):
#         if len(l[i:j])==1:
#             s=sum(l[i:j])
#             l1.append(s)
# print(l1)
# l2=l1[0]
# for i in l1:
#     if i>l2:
#         l2=i
# print(l2)
###################################
# s="aababcabc"
# c=0
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         # print(s[i:j])
#         if len(s[i:j])==3:
#             print(s[i:j])
#             se=set(s[i:j])
#             if len(se)==3:
#                 # print(se)
#                 c=c+1      
# print(c);print(se)
################Sliding window technique#######3333333
# s="xyzzaz"
# l1=[]
# l=0
# r=3
# for i in range(len(s)):
#     l.append(s[i])
#     if r-l1==3:
#         l.pop(l1)
#         l1=l1+1
# print(l1)
for i in [0, 1]:
     for j in [0, 1]:
         for k in [0, 1]:
            for m in [2,1]:
                print((i, j, k,m,"forloops"))


      

