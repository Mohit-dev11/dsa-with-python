class Node:
    def __init__(self, items=None, next=None):
        self.items = items
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_Empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_Empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        # Return the reference of the node
        while temp is not None:
            if temp.items == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    def Print_all(self):
        temp = self.start
        while temp is not None:
            print(temp.items, end=' ')
            temp = temp.next

    def delete_first_node(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_items(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.items == data:
                self.start = None
        else:
            temp = self.start
            if temp.items == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.items == data:
                        temp.next = temp.next.next
                        break
                temp = temp.next

    def __iter__(self):
        return SLLIterator(self.start)

        #  jab bhi aap apne class kp iterable banane chate ho eka ur class banooo jo uski itertaor class
        # Driver Code


class SLLIterator:
    def __init__(self, start):
        self.current = start
#  iterator babano for class

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.items
        self.current = self.current.next
        return data


myList = SLL()
myList.insert_at_start(15)
myList.insert_at_start(55)
myList.insert_at_start(25)
myList.insert_at_last(75)
myList.delete_items(55)
# obj5 = myList.search(25)
# print(obj5.__class__)
# myList.insert_after(myList.search(55), 15)
print()
myList.Print_all()
for m in myList:
    print(m, end='')
print()
