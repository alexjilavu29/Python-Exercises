def removeElement(nums, val):
    k = 0
    l = len(nums)
    i = 0
    while i < l - 1:
        if nums[i] == val:
            j = l - 1
            while nums[j] == val:
                j -= 1
                l -= 1
            aux = nums[i]
            nums[i] = nums[j]
            nums[j] = aux
            l -= 1
        else:
            k += 1
        i += 1
    return k

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums,val))