from sys import displayhook


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        nn = Node(data)
        if not self.head:
            self.head = nn
            return
        currenth = self.head

        while currenth.next:
            currenth = currenth.next
        currenth.next = nn

    def display(self):
        currenth = self.head
        while currenth:
            print(currenth.data)
            currenth = currenth.next
        print("None")

lists = LinkedList()
lists.append(5)
lists.append(10)
lists.append(15)
lists.append(20)
lists.append(25)
lists.display()