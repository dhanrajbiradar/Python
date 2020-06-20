'''
Given list is ["source:Destination:Flight_id:Ticket_num"]
Output LIst should be:["Flight_id:number_of_passangers"]
example:   L1=["BANG:CHN:BAN200:143","HYD:BANG:HYD100:12","MUMB:HYD:MUM300:20",
                                            "BANG:CHN:BAN200:145","MUMB:HYD:MUM300:20"]
'''

ListA=["BANG:CHN:BAN200:143","HYD:BANG:HYD100:12","MUMB:HYD:MUM300:20","BANG:CHN:BAN200:145","MUMB:HYD:MUM300:20"]
ListB=[]
ListC=[]
for i in ListA:
    ListB.append(i.split(":")[2])
print ListB

for j in ListB:
    if j not in ListC:
        ListC.append(j)
print ListC
ListD=[]
for k in ListC:
    ListD.append(str(ListB.count(k)))
ListE=zip(ListC,ListD)
print ListE
ListF=[]
for M in ListE:
    ListF.append(":".join(M))
print ListF


