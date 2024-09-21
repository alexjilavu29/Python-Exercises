# Description: Given an array of strings, group anagrams together.
# Cool solution, but only if the characters don't repeat in the strings.
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagramMap = {}
    for i in strs:
        index = 0
        for char in i:
            index += 2 ** (ord(char) - 97)
        if index not in anagramMap:
            anagramMap[index] = []
        anagramMap[index].append(i)
    result = []
    for i in anagramMap:
        result.append(anagramMap[i])
    return result
