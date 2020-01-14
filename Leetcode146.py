class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.pre = self.head
    
    def move_to_tail(self,key):
        node = self.hashmap[key]
        node.pre.next = node.next
        node.next.pre = node.pre

        self.tail.pre.next = node
        node.pre = self.tail.pre
        self.tail.pre = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_to_tail(key)
        res = self.hashmap.get(key,-1)
        if res==-1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_to_tail(key)
        else:
            if len(self.hashmap)==self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.pre = self.head
            new = ListNode(key, value)
            self.hashmap[key] = new
            self.tail.pre.next = new
            new.pre = self.tail.pre
            new.next = self.tail
            self.tail.pre = new

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
