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

    def delfirst(self,head):
        if self.head == None or self.head.next == None:
            return None

        prev = self.head
        self.head = self.head.next
        self.head.prev = None
        prev.next = None

        return self.head

    def deltail(self,head):
        if self.head == None or self.head.next == None:
            return None

        tail = self.head

        while tail.next is not None:
            tail = tail.next

        back = tail.prev
        tail.prev = None
        back.next = None

        return self.head



mylist = Linkedlist()
head = mylist.array2dll([1,2,3,4,5])
# ans = mylist.delfirst(head)
# mylist.traval(ans)
ans = mylist.deltail(head)
mylist.traval(ans)