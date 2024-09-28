#print(len(" "))

#for i in range(0,0):
#    print("Hello")


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    maxCount = 0

    for i in range(len(s)):

        if len(s) == 1:
            return 1

        charSet = set(s[i])
        charCount = 1

        j = i + 1
        while j < len(s) and s[j] not in charSet:
            charSet.add(s[j])
            charCount += 1
            j += 1

        if charCount > maxCount:
            maxCount = charCount

    return maxCount