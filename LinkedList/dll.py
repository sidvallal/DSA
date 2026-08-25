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
    
    def KthNode(self,head,k):

        cnt = 0
        temp = head
        while temp is not None:
            if cnt == k:
                break
            temp = temp.next
            cnt +=1

        if temp is None:
            return self.head

        back = temp.prev
        front = temp.next

        if back == None and front == None:
            return None
        elif back == None:
            self.delfirst(head)
        elif front == None:
            self.deltail(head)

        else:
            back.next = temp.next
            front.prev= temp.prev

        return self.head

    def deleteNode(self,head):

        temp = head

        front = temp.next
        back = temp.prev

        if front == None:
            back.next = None

        back.next = front
        front.prev = back

        return head
        
    def addfirst(self,head,k):

        new_node = Node(k,None,None)

        if head == None:
            self.head = new_node
            return self.head
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        return new_node

    def addlast(self,head,k):

        new_node = Node(k,None,None)

        temp = self.head

        if temp == None:
            self.head = new_node
            return self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

        return self.head
        
            
mylist = Linkedlist()
head = mylist.array2dll([1,2,3,4,5])
# ans = mylist.delfirst(head)
# mylist.traval(ans)
# ans = mylist.deltail(head)
# mylist.traval(ans)
# ans = mylist.KthNode(head,2)
# mylist.traval(ans)
# ans = mylist.addfirst(head,0)
# mylist.traval(ans)
ans = mylist.addlast(head,6)
mylist.traval(ans)