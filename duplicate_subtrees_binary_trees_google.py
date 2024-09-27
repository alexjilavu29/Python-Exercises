
def findDuplicateSubtrees(root):

    subtreeMap = {}

    def subtreeMaker(treeNode):

        if not treeNode:
            return "#"

        subtree = []

        subtreeLeft = subtreeMaker(treeNode.left)
        subtreeRight = subtreeMaker(treeNode.right)

        if treeNode.val != "#":
            subtree.append(treeNode.val)

        if subtreeLeft != "#":
            subtree.extend(subtreeLeft)

        if subtreeRight != "#":
            subtree.extend(subtreeRight)

        subtreeMap[str(subtree)] += 1

        print(subtreeMap)

        return subtree

    subtreeMaker(root)

    duplicates = []

    for i in subtreeMap:
        if subtreeMap[i] > 1:
            duplicates.append(i)

    return duplicates
