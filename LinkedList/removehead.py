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

    def arr2list(self,numbers: list):
        head = Node(numbers[0])
        mover  = head
        for i in range(1,len(numbers)):
            temp = Node(numbers[i])
            mover.next = temp
            mover = temp

        return head

    def traval(self,head):
        current = head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

    def removehead(self,head):
        if head == None: 
            return head
        temp = head
        head=head.next

        return head.data

arr = [1,2,3,4,5]
mylist = linkedList()
head = mylist.arr2list(arr)
mylist.traval(head)
ans = mylist.removehead(head)
print(ans)


