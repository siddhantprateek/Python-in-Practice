class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # O(1)
    def insertFirst(self, data):
        node =  Node(data)
        node.next = self.head
        self.head = node

    # O(N)
    def insertLast(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return

        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node

    def find(self, target):
        temp = self.head
        while temp != None:
            if temp.data == target:
                return temp
            temp = temp.next
        return None

    def removeLast(self):
        if self.head == None:
            return None

        # when there is only one element in the list
        if self.head.next == None:
            removed = self.head.data
            self.head = None
            return removed

        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        removed = temp.next.data
        temp.next = None
        return removed

    def removeFirst(self):
        prev = self.head 
        self.head = prev.next
        prev.next = None
        return prev.data



    def hasCycle(self):
        slow, fast  = self.head ,self.head
        while slow is not None and fast is not None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        return False


    def cycleLength(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow :
                break

        temp = slow
        length = 0
        while True:
            temp = temp.next
            length += 1
            if temp == slow:
                break
        return length

    def middle(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            # when fast reaches the end the slow will reach the middle
            fast = fast.next.next
            slow = slow.next
        return slow.data

    def insertAfter(self, data, after):
        temp = self.find(after)
        originalNext = temp.next
        node = Node(data) 
        temp.next  = node
        node.next = originalNext

    def display(self):
        temp = self.head 
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
        print('None')



if __name__ == '__main__':
    ll = LinkedList()
    ll.insertFirst(2)
    ll.insertFirst(3)
    ll.insertFirst(8)
    ll.insertFirst(12)
    ll.display()
    ll.insertAfter(5, 8)
    ll.display()
    # print(ll.removeFirst())
    # ll.display()
    # print(ll.removeLast())
    # ll.display()
    last = ll.find(2)
    start = ll.find(8)
    last.next = start

    print(ll.cycleLength())