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

    def arr2list(self, numbers: list):
        if len(numbers) == 0:
            return None

        self.head = Node(numbers[0])
        mover = self.head

        for i in range(1, len(numbers)):
            temp = Node(numbers[i])
            mover.next = temp
            mover = temp

        return self.head

    def traval(self,head):
        current = head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

    def addhead(self,k):
        if self.head == None: 
            temp = Node(k)
            return temp
        temp = Node(k)
        temp.next = self.head
        return temp

    def addtail(self,k):
        if self.head == None:
            self.head = Node(k)
            return self.head
        
        temp = self.head

        while temp.next is not None:
            temp = temp.next

        new_node = Node(k)
        temp.next = new_node

        return self.head
        

    def addKth(self, k, data):
        new_node = Node(data)

        # Empty list
        if self.head is None:
            if k == 1:
                self.head = new_node
            return self.head

        # Insert at position 1
        if k == 1:
            new_node.next = self.head
            self.head = new_node
            return self.head

        temp = self.head
        count = 1

        # Move to the node just before position k
        while temp is not None and count < k - 1:
            temp = temp.next
            count += 1

        # k is greater than list length + 1
        if temp is None:
            return self.head

        new_node.next = temp.next
        temp.next = new_node

        return self.head
    
    def insertBeforeX(self, data, x):
        new_node = Node(data)

        # Empty list
        if self.head is None:
            return self.head

        # x is at the head
        if self.head.data == x:
            new_node.next = self.head
            self.head = new_node
            return self.head

        temp = self.head

        while temp.next is not None:
            if temp.next.data == x:
                new_node.next = temp.next
                temp.next = new_node
                return self.head

            temp = temp.next

        # x not found
        return self.head
        
    
arr = [1,2,3,4,5]
mylist = linkedList()
head = mylist.arr2list(arr)
# mylist.traval(head)
# ans = mylist.removehead(head)
# print(ans)
# ans = mylist.removetail(head)
# mylist.traval(ans)
# ans = mylist.deleteK(head,4)
# mylist.traval(ans)
# ans = mylist.deleteElement(head,4)
# mylist.traval(ans)
# ans = mylist.addhead(0)
# mylist.traval(ans)
# ans = mylist.addtail(6)
# mylist.traval(ans)
# ans = mylist.addKth(3,3)
# mylist.traval(ans)
ans = mylist.insertBeforeX(10,2)
mylist.traval(ans)


