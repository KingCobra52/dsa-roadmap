class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        previous = None
        current = self.head
        while current is not None:
            if current.data == item:
                if previous is not None:
                    previous.next = current.next
                    return True
                else:
                    self.head = current.next
                    return True
            previous = current
            current = current.next
        return False

    def append(self, item):
        #add new node to the end of list
        temp = Node(item)
        if self.head is None:
            self.head = temp
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = temp

def main():
    mylist = LinkedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    print(mylist.head.data)
    print(mylist.head.next.next.data)

if __name__ == "__main__":
    main()
