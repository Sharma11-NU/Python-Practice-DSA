"""
This is my practice file for linked list.
What do we understand by linked list and how it is used in
DSA - Data Structure and algorithm

"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head    # for my understanding itr = start from
        llstr = ''
        while itr:
            llstr += str(itr.data)+'-->' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head   # for my understanding itr = start from

        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head         # for my understanding itr = start from head

        while itr.next:
            itr = itr.next      # for my understanding itr = start from next value

        itr.next = Node(data,None)

    def insert_at(self, index, data):
        if  index < 0 or index >= self.get_length():
            raise Exception("Enter a valid index")

        if index == 0:
            self.insert_at_start(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception (" Enter a valid index ")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        # if the head node is the one to remove
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next is not None:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next


if __name__ == '__main__':

    ll = LinkedList()
    ll.insert_value([1,2,3,4,5,6,8])
    ll.insert_at(6,7)
    ll.remove_at(7)
    ll.print()
    ll = LinkedList()
    ll.insert_value(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()







