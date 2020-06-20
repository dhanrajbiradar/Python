'''
Given a list of integers with duplicate elements in it. The task to generate another
list, which contains only the duplicate elements. In simple words, the new list should
 contain the elements which appear more than one.
Examples :
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]

Input :  list = [-1, 1, -1, 8]
Output : output_list = [-1]

'''

ListA=[20,20,30,40,1,40,1,4,20,40]
ListB=[]
SizeA=len(ListA)
for i in range(SizeA):
    k=i+1
    for j in range(k,SizeA):
        if ListA[i]==ListA[j] and ListA[i] not in ListB:
            ListB.append(ListA[i])
print ListB





