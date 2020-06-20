def divideList(lst):
    dct = {}

    for element in lst:
        if len(element) not in dct:
            dct[len(element)] = [element]
        elif len(element) in dct:
            dct[len(element)] += [element]
    print dct
    print sorted(dct)

    res = []
    for key in sorted(dct):
        res.append(dct[key])

    return res


# Driver code
lst = ['The', 'art', 'of', 'programming']
print(divideList(lst))


L=["hello","dh","raj","rajkumar"]
dic={}
for i in L:
    if(len(i) not in dic):
        dic[len(i)]=[i]
    elif len(i) in dic:
        dic[len(i)]+=[i]

res=[]
for j in sorted(dic):
    res.append(dic[j])
print res



