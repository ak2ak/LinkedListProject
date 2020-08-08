def advanceArray(nums):
    furthest_reach = 0
    last_index = len(nums)-1
    i=0
    while i<=furthest_reach and furthest_reach<last_index:
        furthest_reach = max(furthest_reach,nums[i]+i)
        i+=1
    return furthest_reach>=last_index

print(advanceArray([3,2,2,0,1]))