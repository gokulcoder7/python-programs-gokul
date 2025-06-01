import string
s=input('ENTER STR:')
n=len(s)

print("lengt=",n)
#print(string.printable)
sp="!#$%&()*+,-./:;<=>?@^_`{|}~"
l=list(sp)

res=[0]*n

for i,c in enumerate(s):
    if c in l:
        res[i]=c
        continue
    else:
        res[i]=0
print(res)

# reverse string without changing position of special characters
rev=s[::-1]
revv=[0]*n
for v,c3 in enumerate(rev):
    if c3 in sp:
        revv[v]=''
    else:
        revv[v]=c3

re=''.join(revv)
c=0
print(re)
for j,c2 in enumerate(res):
    if c2==0:
        res[j]=re[c]
        c+=1

print(res)
        

print(''.join(res))



