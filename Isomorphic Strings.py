def isomorphic_strings(str1,str2):
    dict1={}
    dict2={}
    for i in str1:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    for i in str2:
        if i in dict2:
            dict2[i]+=1
        else:
            dict2[i]=1
    
    l1=dict1.values()
    l2=dict2.values()
    if(len(dict1)==len(dict2)):
        i=0
        c=1
        while(l1[i]==l2[i]):
            c+=1
            i+=1
        if(c==len(dict1.values())):
            return 1
        else:
            return 0
    
print(isomorphic_strings('aab','xxy'))