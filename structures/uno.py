class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next

        return count
