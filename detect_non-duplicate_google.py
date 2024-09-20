def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hashSet = set()
    for i in nums:
        if i not in hashSet:
            hashSet.add(i)
        else:
            hashSet.remove(i)
    for i in hashSet:
        return i

nums = [2,2,1]
print(singleNumber(nums))


def singleNumberFaster(nums):
    result = 0
    for num in nums:
        result ^= num # XOR operator = 0 if both bits are the same, 1 if different -> Two same numbers will cancel each other out
    return result


nums = [2,2,1]
print(singleNumberFaster(nums))