from collections import deque
class MaxQueue:
    def __init__(self):
        self.que = deque([])
        self.ma = deque([])

    def max_value(self) -> int:
        if not self.ma:
            return -1
        return self.ma[0]

    def push_back(self, value: int) -> None:
        self.que.append(value)
        while self.ma and self.ma[-1]<value:
            self.ma.pop()
        self.ma.append(value)

    def pop_front(self) -> int:
        if not self.que:
            return -1
        val = self.que.popleft()
        if val==self.ma[0]:
            self.ma.popleft()
        return val

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
