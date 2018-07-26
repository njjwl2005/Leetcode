s="abba"
temp={}
length=1
i=0
j=0

if len(s)==0 or len(s)==1:
    print (len(s))
while i<=j and j<=len(s)-1:
    print("i=",i)
    print("j=",j)
    if s[j] not in temp:
        temp[s[j]]=j
    else:
        if j-i>length:
            length=j-i
        if temp
        i=temp[s[j]]+1
        temp[s[j]]=j
    j=j+1    
if j-i>length:
    length=j-i
print (j,i)
        


