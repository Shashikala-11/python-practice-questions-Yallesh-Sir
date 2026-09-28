lst=[22,43,56,35,98,67,52]
n=len(lst)
i=0
while i<n:
    if lst[i]%2==0:
        print("Even -> ",lst[i])
    else:
        print("Odd -> ",lst[i])
    i+=1    