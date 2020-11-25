'''
#第一种方法：python collections.OrderedDict
from collections import OrderedDict
class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]


    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)
'''
#第二种方法：哈希表+双向链表
class DoubleLinkedListNode:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity:int):
        self.cache = {}
        self.head = DoubleLinkedListNode()
        self.tail = DoubleLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key:int):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.movetoHead(node)
        return node.value

    def put(self, key:int, value:int):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.movetoHead(node)
        else:
            node = DoubleLinkedListNode(key, value)
            self.addtoHead(node)
            self.cache[key] = node
            self.size += 1
            if self.size > self.capacity:
                node = self.removeTail()
                self.cache.pop(node.key)
                self.size -= 1
    
    def movetoHead(self, node):
        self.removeNode(node)
        self.addtoHead(node)

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def addtoHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node



    
             



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)