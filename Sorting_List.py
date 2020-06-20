'''
                                            Sorting list by 3 methods
Note:Ascending order Using bubble sort
L=[4,16,18,5,6]
steps 1:Total 5 elemengts are there so n=5
steps 2:We need to compare each element with next element then need to do swapping if not less
steps 3:Here 5 elelmengts are there so 4 comparisions are requires in each pass(Total 4 pass are required)
example==pass 1:i)compare 4 and 16 if grater swap else no [4,16,18,5,6] ii)compare 16 nd 18 then no swap [4,16,18,5,6]
iii)compare 18 and 5 then swap [4,16,5,18,6] iv)compare 6 and 18 then  swap [4,16,5,6,18]
like continue upto 4 pass
pass1:              Pass 2:          Pass 3:          Pass 4:
[4,16,18,5,6]   [4,16,5,6,18]
[4,16,18,5,6]   [4,5,16,6,18]
[4,16,5,18,6]   [4,5,6,16,18]
[4,16,5,6,18]   [4,5,6,16,18]


'''
ListA=[34,23,4,14,35]
for i in range(0,len(ListA)-1):#outer for loop 4 pass are required bcz 5 elelements are there
    for j in range(0,len(ListA)-1):#inner loop need to 4 comparision with next elelments
        if(ListA[j]>ListA[j+1]):
            ListA[j],ListA[j+1]=ListA[j+1],ListA[j]#it does 16 comparision in four passes
print ListA

'''
Method2:
AS in above method it has to do all comparios even though  some last  elements are in order
like in 1st pass greater element wiil be last so next time is not required to compariion
like in second pass last two element are in order
like in third pass last 3 element will be in order

like inner for loop will be for j in range(0,len(ListB)-1-i) 
'''
ListB=[2,67,3,4,1]
for i in range(0,len(ListB)-1):
    for j in range(0,len(ListB)-1-i):
        if(ListB[j]>ListB[j+1]):
            ListB[j],ListB[j+1]=ListB[j+1],ListB[j]
print ListB

'''
Method 3:
in this method in any pass if allready elements are in ascending order no need to go next pass for comparision
use flag=0 after first for loop
if comparision den flag=1 else break loop
'''
Listc=[2,67,3,4,1]
for i in range(0,len(Listc)-1):
    flag=0
    for j in range(0,len(Listc)-1-i):
        if(Listc[j]>Listc[j+1]):
            Listc[j],Listc[j+1]=Listc[j+1],Listc[j]
            flag=1
    if(flag==0):
        break

print Listc











