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
    def removetail(self,head):
        if head == None:
            return head
        if head.next == None:
            return head
        
        current = head

        while current.next.next is not None:
            current = current.next

        current.next = None
        return head

    def deleteK(self,head,k):
        if head == None:
            return head
        if head.next == None:
            temp = head
            head = head.next
            return head
        cnt = 0
        temp = head
        prev = None

        while temp is not None:
            cnt +=1
            if cnt == k:
                prev.next = prev.next.next
                break
            prev = temp
            temp = temp.next
        return head
    
    def deleteElement(self,head,el):
            if head == None:
                return head
            if head.data == el :
                temp = head
                head = head.next
                return head
            temp = head
            prev = None
            while temp is not None:
                if temp.data == el:
                    prev.next = prev.next.next
                    break
                prev = temp
                temp = temp.next
            return head
        
    
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
ans = mylist.deleteElement(head,4)
mylist.traval(ans)


