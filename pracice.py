s="a1bccb1a"
# s1=len(s)//2
# s2=len(s)
# for i in range(s1):
#     print(s[i])
#     for j in range(s2-1,0,-1):
#         print(s[j])
#         if s[i]==s[j]:
#             print(s[i],s[j])
g=""
for i in range(len(s)-1,-1,-1):
    g=s[i]+g
print(g)

    
    