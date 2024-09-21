import time

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    result = []
    i = 0
    l = len(nums1)
    while i < len(nums1):
        if nums1[i] in nums2:
            result.append(nums1[i])
            nums2.pop(nums2.index(nums1[i]))
            nums1.pop(i)
            l -= 1
        else:
            i += 1
    return result

# Declare variables for intersect function
nums1 = [1,2,2,1]
nums2 = [2,2]

# Time the function

start_time = time.time()

print(intersect(nums1,nums2))

print("--- %s seconds ---" % (time.time() - start_time))


def intersectFaster(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    ptr1 = 0
    ptr2 = 0

    i = []
    while ptr1 < len(nums1) and ptr2 < len(nums2):
        if nums1[ptr1] == nums2[ptr2]:
            i.append(nums1[ptr1])
            ptr1 += 1
            ptr2 += 1
        elif nums1[ptr1] < nums2[ptr2]:
            ptr1 += 1
        else:
            ptr2 += 1
    return i

# Declare variables for intersectFaster function
nums1 = [1,2,2,1]
nums2 = [2,2]

# Time the function

start_time = time.time()

print(intersectFaster(nums1,nums2))

print("--- %s seconds ---" % (time.time() - start_time))
