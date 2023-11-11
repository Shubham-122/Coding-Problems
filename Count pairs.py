def Count_pairs(nums,target):
    hashmap={}
    result=[]
    required=0
    for i in range(len(nums)):
        curr=nums[i]
        required=target-curr
        if(required not in hashmap):
            hashmap[curr]=i
        else:
            result.append(i)
            result.append(hashmap.get(required))
    return (result)
print(Count_pairs([1,5,7,1],6))

# def Count_pairs(nums,target):
#     hashmap={}
#     result=[]
#     required=0
#     for i in range(len(nums)):
#         curr=nums[i]
#         required=target-curr
#         if(required not in hashmap):
#             hashmap[curr]=i
#         else:
#             return True
#     return False
# print(Count_pairs([1,5,7,1],6))