class MyHashSet(object):

    def __init__(self):
        # print("Called __init__() function.")
        self.set = []
        # print(self.set)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        # print("Called contains() function.")
        if len(self.set) == 0:
            # print(self.set)
            return False
        for i in range(0, len(self.set)):
            if self.set[i] == key:
                # print(self.set)
                return True
        # print(self.set)
        return False

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        # print("Called add() function.")

        if not self.contains(key):
            self.set.append(key)
        # print(self.set)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        # print("Called remove() function.")
        if self.contains(key):
            for i in range(0, len(self.set)):
                if self.set[i] == key:
                    self.set.pop(i)
                    # print(self.set)
                    break
        # print(self.set)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)