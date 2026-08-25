class Node:
    def __init__(self,val,next,prev):
        self.data = val
        self.next = next
        self.prev = prev

class Linkedlist:
    def __init__(self):
        self.head = None

    def array2dll(self,numbers):
        self.head = Node(numbers[0],None,None)
        prev = self.head

        for i in range(1,len(numbers)):
            temp = Node(numbers[i],None,prev)
            prev.next = temp
            prev = temp

        return self.head

    def traval(self,head):
        temp = head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

mylist = Linkedlist()
head = mylist.array2dll([1,2,3,4,5])
mylist.traval(head)