def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    numMap = {}

    for i in nums:
        if i not in numMap:
            numMap[i] = 1
        else:
            numMap[i] += 1

    sortedMap = [v[0] for v in sorted(numMap.items(), key=lambda item: item[1], reverse=True)]

    print(sortedMap)

    result = []

    for i in sortedMap:
        if k > 0:
            result.append(i)
            k -= 1
        else:
            break

    return result
