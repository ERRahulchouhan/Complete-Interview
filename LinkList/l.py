class Node:
    def __init__(self,value):
        self.value = value
        self.next = next

class LinkList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.value
            
    def insert(self,value,loc):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail  = newNode
        else:
            if loc == 0:
                newNode.next = self.head
                self.head = newNode
            elif loc == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < loc-1 :
                    tempNode = tempNode.next
                    index +=1
                
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                
                if self.tail == tempNode:
                    self.tail = newNode
                    
l = LinkList()
l.insert(0,0)
l.insert(1,1)
l.insert(2,2)
print([i.value for i in l ])
                
                