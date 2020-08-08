class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):

        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next 

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node


a = LinkedList()
a.append('a')
a.append(32)
a.append(3242)
a.append(324)
a.printList()
