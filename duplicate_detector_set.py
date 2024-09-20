
def containsDuplicate(nums):
    numsSet = set()
    for i in nums:
        if i in numsSet:
            return True
        numsSet.add(i)
    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))



def containsDuplicateFaster(nums):
    return len(set(nums)) != len(nums)

nums = [1,2,3,1]
print(containsDuplicateFaster(nums))