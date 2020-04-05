class SingleNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList:

    def __init__(self):
        self.size = 0
        self.head = SingleNode(0)
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        p = self.head
        for _ in range(index + 1):    # 伪头结点占了一位
            p = p.next
        return p.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            # 在头部插入
            index = 0
        self.size += 1
        # 找到要插入位置的节点的前驱节点
        p = self.head
        for _ in range(index):
            p = p.next
        to_add = SingleNode(val)
        to_add.next = p.next
        p.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        p = self.head
        for _ in range(index):
            p = p.next
        p.next = p.next.next

class DoubleNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList:
    """
    找到要处理节点的前驱pred和后继节点succ
    """
    def __init__(self):
        self.size = 0
        self.head = DoubleNode(0)
        self.tail = DoubleNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val):
        pred = self.head
        succ = self.head.next
        self.size += 1
        to_add = DoubleNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtTail(self, val):
        succ = self.tail
        pred = self.tail.prev
        self.size += 1
        to_add = DoubleNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        self.size += 1
        to_add = DoubleNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next    # pred.next为当前要删除的节点
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):    # 不包括尾节点
                succ = succ.prev
            pred = succ.prev.prev
        
        self.size -= 1
        pred.next = succ
        succ.prev = pred



# Your MyLinkedList object will be instantiated and called as such:
# ["MyLinkedList","addAtHead","addAtTail","addAtHead","addAtTail","addAtHead","addAtHead","get","addAtHead","get","get","addAtTail"]
# [[],[7],[7],[9],[8],[6],[0],[5],[0],[2],[5],[4]]
# [null,null,null,null,null,null,null,8,null,6,7,null]
obj = MyLinkedList()
print(obj.addAtHead(1))
print(obj.addAtTail(3))
print(obj.addAtIndex(1, 2))
# print(obj.get(1))
# print('====', obj.print())
print(obj.deleteAtIndex(1))
# print(obj.get(1))
obj.print()
