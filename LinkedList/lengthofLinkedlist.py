class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:

    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" ")
            current = current.next

    def length(self):
        cnt = 0
        current = self.head
        while current is not None:
            cnt +=1
            current = current.next

        print('length: ',cnt)
        

my_list = linkedList()
my_list.insert(10)
my_list.insert(20)
my_list.insert(30)

my_list.length()