s="hello world 123 hai"
lst=[]
i=0
n=len(s)
while  i<n:
    if s[i] in "aeiouAEIOU" or s[i].isdigit():
        lst.append(s[i])
       
    i+=1
print(lst)        
