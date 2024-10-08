class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyLinkedList:

    def __init__(self, head=None):
        self.head = head

    def get(self, index: int) -> int:
        cur = self.head
        if cur == None:
            return -1
        while index and cur.next != None:
            cur = cur.next
            index -= 1
        if index != 0:
            return -1
        return cur.data

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            if self.head == None:
                return None
            cur = self.head
            while index > 1 and cur.next != None:
                cur = cur.next
                index -= 1
            if index == 1 and cur.next == None:
                self.addAtTail(val)
            elif index >= 1 and cur.next == None:
                return None
            else:
                next_node = Node(val)
                next_node.next = cur.next
                cur.next = next_node

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return None
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            if cur.next == None:
                return None
            while index > 1 and cur.next.next != None:
                cur = cur.next
                index -= 1
            if index == 1 and cur.next.next == None:
                cur.next = None
            elif index >= 1 and cur.next.next == None:
                return None
            else:
                cur.next = cur.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)