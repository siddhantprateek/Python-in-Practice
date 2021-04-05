class Queue:

    def __init__(self, size = 10):
        self.size = size
        self.data = [None for _ in range(size)]
        self.end = 0


    def isFull(self):
        self.end == self.size

    def isEmpty(self):
        self.end == 0


    def insert(self, item):
        if self.isFull():
            print('Queue is Full')
            return False

        self.data[self.end] = item
        self.end += 1



#
    def remove(self):
        if self.isEmpty():
            print('Queue is Empty')
            return False

        # Queue remove the element from the beginning
        removed = self.data[0]

        # on Removal the Queue is shifted in front
        for i in range(1, self.end):
            self.data[i - 1] = self.data[i]

        self.end -= 1
        return removed

#
    def bbsort(self):
        for i in range(self.end):
            for j in range(self.end - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]


    def front(self):
        return self.data[self.end]

    def display(self):
        return self.data[:self.end]



queue = Queue(10)


queue.insert(5)
queue.insert(10)
queue.insert(22)
queue.insert(6)
queue.insert(7)

# bbsort() works
# queue.bbsort()
print(queue.display())

queue.remove()
queue.remove()

print(queue.display())
# queue.bbsort()
# print(queue.display())