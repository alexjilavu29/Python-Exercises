import time


def findDuplicateSubtrees(root):
    def hashingFunction(subtree):

        hashCode = ""

        for i in range(len(subtree)):
            hashCode += str(subtree[i].val)

        return hashCode

    subtreeMap = {}
    subtreeList = []

    def subtreeMaker(treeNode):

        if not treeNode:
            return "#"

        subtree = []

        subtreeLeft = subtreeMaker(treeNode.left)
        subtreeRight = subtreeMaker(treeNode.right)

        if treeNode.val != "#":
            subtree.append(treeNode)

        if subtreeLeft != "#":
            subtree.extend(subtreeLeft)

        if subtreeRight != "#":
            subtree.extend(subtreeRight)

        subtreeCode = hashingFunction(subtree)

        if subtreeCode not in subtreeMap:
            subtreeMap[subtreeCode] = 1
            subtreeList.append(subtree)
        else:
            subtreeMap[subtreeCode] += 1

        print(subtreeMap)

        return subtree

    subtreeMaker(root)

    duplicates = []

    print
    subtreeList

    for i in subtreeList:
        if subtreeMap[hashingFunction(i)] > 1:
            duplicates.append(i[0])
            print(duplicates)

    return duplicates


# Declare variables for findDuplicateSubtrees function
root = [1,2,3,4,None,2,4,None,None,4]

# Time the function

start_time = time.time()

print(findDuplicateSubtrees(root))

print("--- %s seconds ---" % (time.time() - start_time))
