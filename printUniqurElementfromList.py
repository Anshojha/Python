def uniqueList(l):
    x =[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(uniqueList([1,2,3,4,1,2,3,4,5]))