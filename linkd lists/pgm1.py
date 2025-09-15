class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def traverse(self):
        curr = self.head
        while curr != None:
            print(curr.data, end="->")
            curr = curr.next 
        print("None")

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
        self.n += 1

    def insert_after(self,after,data):
        new_node=node(data)
        curr=self.head

        while curr!=None:
            if curr.data==after:
                break
            curr=curr.next

        if curr!=None:
            new_node.next=curr.next
            curr.next=new_node
        else:
            return "item not found"
        
    def reverse(self):
        temp=self.head
        prev=None
        while temp!=None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        self.head = prev    
    
L = linkedlist()
L.insert(1)    
L.insert(2)
L.insert(3)
L.insert(4)
# L.insert_after(2,700)
L.append(5)
L.traverse()
L.reverse()
L.traverse()

