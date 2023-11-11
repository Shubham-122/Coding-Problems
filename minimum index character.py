def minimum_indexed_charater(stri,patt):
    l=[]
    
    for i in patt:
        if i in stri:
            l.append(stri.index(i))
    print(l)
    return min(l)


print(minimum_indexed_charater('geeksforgeeks','set'))