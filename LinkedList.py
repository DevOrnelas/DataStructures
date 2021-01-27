class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addNode(self, num):
        newNode = Node(num)
        if(self.head == None):
            print('adding Head of Node....')
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            print('adding to the end of the chain...')
            temp.next = newNode
            newNode.next = None
            print('end of the chain is now nullified')
    
    def peek(self, num):
        # DOES LIST CONTAIN NUMBER?
        temp = self.head
        while(temp):
            if(temp.data == num):
                print('Number found in List !')
                return True
            temp = temp.next
        print('Number Not Found in List')
        return False

# CRATE A NEW HEAD NODE 
    
    def newHeadNode(self, num):
        newNode = Node(num)
        temp = self.head
        self.head = newNode
        self.head.next = temp
        return

    def printNodes(self):
        # start at the head
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next



if __name__ == "__main__":
    a = LinkedList()
    a.addNode(99)
    a.addNode(909)
    a.addNode(666)
    a.addNode(222)
    a.addNode(255)
    a.printNodes()
    a.peek(909)
    a.peek(9)
    a.newHeadNode(101)
    a.printNodes()