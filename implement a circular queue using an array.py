class Queue:
    def __init__(self, c):
        self.arr = [0] * c
        self.capacity = c
        self.size = 0
        self.front = 0

    def getFront(self):
        if self.size == 0:
            return -1
        return self.arr[self.front]

    def getRear(self):
        if self.size == 0:
            return -1
        rear = (self.front + self.size - 1) % self.capacity
        return self.arr[rear]

    def enqueue(self, e):
        if self.size == self.capacity:
            return
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = e
        self.size += 1

    def dequeue(self):
        pass


