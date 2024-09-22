import time

# Description: Given an array of strings, group anagrams together.
# Cool solution, but only if the characters don't repeat in the strings.
def groupAnagramsUnique(strs):
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

# Declare variables for groupAnagramsUnique function
strs = ["eat","tea","tan","ate","nat","bat"]

# Time the function

start_time = time.time()

print(groupAnagramsUnique(strs))

print("--- %s seconds ---" % (time.time() - start_time))


# Description: Given an array of strings, group anagrams together.
# This is a better solution for when the characters repeat in the strings.
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagramMap = {}
    for i in strs:
        sortedWord = ''.join(sorted(i))
        if sortedWord not in anagramMap:
            anagramMap[sortedWord] = []
        anagramMap[sortedWord].append(i)
    result = []
    for i in anagramMap:
        result.append(anagramMap[i])
    return result

# Declare variables for groupAnagrams function
strs = ["eat","tea","tan","ate","nat","bat"]

# Time the function

start_time = time.time()

print(groupAnagrams(strs))

print("--- %s seconds ---" % (time.time() - start_time))
