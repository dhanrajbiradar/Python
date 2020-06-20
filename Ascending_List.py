ListA=[4,5,6,3,5,6,7,8]
ListB=[]
for i in range(len(ListA)):
    for j in range(i+1,len(ListA)):
        if ListA[i]>ListA[j]:
            temp=ListA[i]
            ListA[i]=ListA[j]
            ListA[j]=temp
print ListA
