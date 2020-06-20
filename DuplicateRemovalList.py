# Python 3 code to demonstrate
# removing duplicated from list
# using naive methods

# initializing list
ListA=[1,2,1,3,3,4,5,5,6]
Rem_List=[]
for i in ListA:
    if i not in Rem_List:
        Rem_List.append(i)
print Rem_List