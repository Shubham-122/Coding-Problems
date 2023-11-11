def second_most(arr,n):
    map={}
    for i in arr:
        if i in map:
            map[i]+=1
        else:
            map[i]=1
    map.sort()
    l=len(map)
    return map[l-1]
arr=['aaa','bbb','ccc','bbb','aaa','aaa']
n=len(arr)
print(second_most(arr,n))