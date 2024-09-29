def fourSumCount(nums1, nums2, nums3, nums4):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type nums3: List[int]
    :type nums4: List[int]
    :rtype: int
    """
    count = 0
    for i in nums1:
        for j in nums2:
            for k in nums3:
                nr = 0 - k - j - i
                aux = []
                aux.extend(nums4)
                while nr in aux:
                    count += 1
                    aux.remove(nr)
    return count