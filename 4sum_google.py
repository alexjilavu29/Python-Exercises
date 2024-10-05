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


# 4sum with only one list
def fourSum(nums, target):

    result = []

    if len(nums) < 4:
        return result

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            for k in range(j + 1, len(nums) - 1):
                for l in range(k + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        quadruplet = list((nums[i], nums[j], nums[k], nums[l]))
                        quadruplet.sort()
                        if quadruplet not in result:
                            result.append(quadruplet)

    return result



def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    result = []

    if len(nums) < 4:
        return result

    pairMap = {}

    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] not in pairMap:
                pairMap[nums[i] + nums[j]] = []
            pairMap[nums[i] + nums[j]].append(list((nums[i], nums[j])))

    print(pairMap)

    for i in pairMap:
        if target - i in pairMap:
            for j in pairMap[i]:
                for k in pairMap[target - i]:
                    if j != k:
                        quadruplet = []
                        quadruplet.extend(j)
                        quadruplet.extend(k)
                        quadruplet.sort()
                        if quadruplet not in result:
                            result.append(quadruplet)

    return result



def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    result = []

    if len(nums) < 4:
        return result

    pairMap = {}

    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] not in pairMap:
                pairMap[nums[i] + nums[j]] = []

            ij_list = []

            if nums[i] == 0:
                ij_list.append(nums[i] + (i * 10 ** len(nums[i])))
            else:
                ij_list.append(nums[i] + (i * 10 ** len(nums[i])) * (nums[i] / abs(nums[i])))

            if nums[j] == 0:
                ij_list.append(j * 10 ** len(nums[j]))
            else:
                ij_list.append(nums[j] + (j * 10 ** len(nums[j])) * (nums[j] / abs(nums[j])))

            pairMap[nums[i] + nums[j]].append(ij_list)

    print(pairMap)

    for i in pairMap:
        if target - i in pairMap:
            for j in pairMap[i]:
                for k in pairMap[target - i]:
                    if j != k:

                        q = []
                        q.extend(j)
                        q.extend(k)

                        qSet = set(q)

                        if len(q) == len(qSet):

                            j_update = []
                            j_update.extend(j)

                            if j_update[0] >= 0:
                                j_update[0] = j_update[0] % 10
                            else:
                                j_update[0] = (-1) * (abs(j_update[0]) % 10)

                            if j_update[1] >= 0:
                                j_update[1] = j_update[1] % 10
                            else:
                                j_update[1] = (-1) * (abs(j_update[1]) % 10)

                            k_update = []
                            k_update.extend(k)

                            if k_update[0] >= 0:
                                k_update[0] = k_update[0] % 10
                            else:
                                k_update[0] = (-1) * (abs(k_update[0]) % 10)

                            if k_update[1] >= 0:
                                k_update[1] = k_update[1] % 10
                            else:
                                k_update[1] = (-1) * (abs(k_update[1]) % 10)

                            quadruplet = []
                            quadruplet.extend(j_update)
                            quadruplet.extend(k_update)

                            print(quadruplet)
                            quadruplet.sort()
                            if quadruplet not in result:
                                result.append(quadruplet)

    return result
