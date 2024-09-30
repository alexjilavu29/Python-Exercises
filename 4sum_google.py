def fourSumCount(nums1, nums2, nums3, nums4):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type nums3: List[int]
    :type nums4: List[int]
    :rtype: int
    """
    count = 0
    ComboMap12 = {}
    ComboMap34 = {}
    for i in range(0, len(nums1)):
        for j in range(0, len(nums1)):

            key12 = nums1[i] + nums2[j]
            key34 = nums3[i] + nums4[j]

            if key12 not in ComboMap12:
                ComboMap12[key12] = 1
            else:
                ComboMap12[key12] += 1

            if key34 not in ComboMap34:
                ComboMap34[key34] = 1
            else:
                ComboMap34[key34] += 1

    for i in ComboMap12:
        opposite = i * (-1)
        if opposite in ComboMap34:
            count += ComboMap12[i] * ComboMap34[opposite]

    return count