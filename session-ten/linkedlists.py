class Node:
    '''The Node (Cell) of a linked list'''
    def __init__(self,value):
        self.data = value
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,value):
        self.data = value

    def setNext(self, next):
        self.next = next

class LinkedList:
    '''The linked list ....'''
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count+= 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

if __name__ == "__main__":
    lst = LinkedList()
    lst.add(12)
    lst.add(34)
    lst.add(54)
    print(lst.isEmpty())
    print(lst.size())

