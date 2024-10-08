def removeElement(nums, val):
    k = 0
    l = len(nums)
    i = 0

    # Parce through numbers
    while i < l - 1:
        if nums[i] == val:
            j = l - 1
            while nums[j] == val and l>0:
                j -= 1
                l -= 1
            if j>i:
                aux = nums[i]
                nums[i] = nums[j]
                nums[j] = aux
            l -= 1
        i += 1
    i = 0

    # Count the number of elements different from val
    while i < len(nums) and nums[i] != val:
        k += 1
        i += 1
    return k

# Declare variables for removeElement function
nums = [2,3,3]
val = 3
print(removeElement(nums,val))