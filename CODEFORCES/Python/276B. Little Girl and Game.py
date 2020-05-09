s = input()
r = s[::-1]
if s==r or len(s)%2==1:
    print("First")
else:
    print("Second")
# s0 = input()
# r0 = s0[::-1]
# s = list(s0)
# r = list(r0)

# i=0;j=-1;count=0
# while i<len(s) and j>-len(s)-1:
#     if s==r:
#         if count%2==0:
#             print("First")
#             break
#         else:
#             print("Second")
#             break
#     if s[i]==r[i]:
#         i+=1;j-=1
#         # print(s, r)
#         # continue
#     else:
#         del s[j]
#         del r[i]
#         count+=1
#         # i+=1;j-=1
#         # print(s, r)