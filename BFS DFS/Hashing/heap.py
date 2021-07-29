class Heap:
    def __init__(self):
        self.li = []

    #O(1)
    def get(self):
        if len(self.li) == 0:
            return None
        return self.li[0]

    def insert(self,value):

        self.li.append(value)
        self.upheap(len(self.li) - 1)

    def upheap(self, index):
        if index == 0:
            return

        p = self.parent(index)

        if self.li[index] < self.li[p]:
            self.swap(index, p)
            self.upheap(p)


    #O(logN)
    def remove(self):
        if len(self.li) == 0:
            return None
        removed = self.li[0]
        last =self.li[-1]

        if len(self.li) != 0:
            self.li[0] = self.li[-1]
            del self.li[-1]
            self.downheap(0)

        return removed

    def downheap(self, index):
        minimum = index
        left = self.left(index)
        right= self.right(index)

        if left < len(self.li) and self.li[minimum] > self.li[left]:
            minimum = left
        if right < len(self.li) and self.li[minimum] > self.li[right]:
            minimum = right


        if minimum != index:
            self.swap(minimum, index)
            self.downheap(minimum)

    def swap(self, first, second):
        temp = self.li[first]
        self.li[first] = self.li[second]
        self.li[second] = temp

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return index * 2 + 1

    def right(self, index):
        return index * 2 + 2

    # to remove N item in heao O(NlogN)
    def heapSort(self):
        li = []
        while len(self.li) != 0:
            li.append(self.remove())
        return li

if __name__ == '__main__':
    heap = Heap()
    for i in range(1, 10):
        heap.insert(i)
    # print(heap.get())
    # print(heap.remove())
    # print(heap.get())
    print(heap.heapSort())
