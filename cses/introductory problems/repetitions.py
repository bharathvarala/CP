s=input()
def f(s,a):
    ans=0
    c=0
    for i in range(len(s)):
        if s[i]==a:
            c+=1 
        else:
            ans=max(c,ans)
            c=0
    ans=max(ans,c)
    return ans

print(max(f(s,"A"),f(s,"C"),f(s,"T"),f(s,"G")))



# s=input()
# d={}
# i=0
# j=0
# ans=0
# while j<len(s):
#     if s[j] in d:
#         d[s[j]]+=1 
#     else:
#         d[s[j]]=1 
#     if len(d)==1:
#         ans=max(j-i+1,ans)
#         j+=1 
#     else:
#         while len(d)!=1:
#             d[s[i]]-=1
#             if d[s[i]]==0:
#                 del d[s[i]]
#             i+=1 
#         j+=1 
# print(ans)