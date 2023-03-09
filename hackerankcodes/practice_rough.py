class node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def insert(self,value):
        new_node = node(value)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp:
                if temp.next == None:
                    temp.next = new_node
                temp = temp.next
                
    def printlinkedlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
if __name__ == '__main__':
    link = linkedlist()
    link.insert(2)
    link.insert(3)
    # ele = [1,2,3,4,5,6,7,8,9]
    
    link.printlinkedlist()