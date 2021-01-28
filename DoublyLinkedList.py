class Node():
  def __init__(self, data):
        self.data = data 
        self.prev = None 
        self.next = None

class DoubleList():
    def __init__(self):
        self.head = None
    
    def addNode(self, data):
        newNode = Node(data)
        if(self.head == None):
            newNode.prev = None 
            self.head = newNode
            return
        tail = self.head
        while(tail.next != None):
            tail = tail.next
        newNode.prev = tail 
        tail.next = newNode

    def printList(self):
        t = self.head
        while(t is not None):
            print('Node is: ', t.data)
            t = t.next
    
    def leftNeighbor(self, num):
        t = self.head 
        while(t.data is not num):
            t = t.next
        print('my LEFT neighbor: ', t.prev.data)

    def rightNeighbor(self, num):
        t = self.head 
        while(t.data is not num):
            t = t.next
        if(t.next == None):
            print('NOBODY TO MY RIGHT or NUm Not In List')
        else:
            print('RIGHT neighbor: ', t.next.data)




if( __name__ == "__main__"):
    dd = DoubleList()
    dd.addNode(12)
    dd.addNode(13)
    dd.addNode(14)
    dd.addNode(15)
    dd.addNode(16)
    dd.addNode(17)
    dd.addNode(128)
    dd.leftNeighbor(16)