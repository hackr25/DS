#Q.1) Write a program to implement the concept of Queue with different operations in python.

class queue:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
       return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

s=queue()
print(s.isEmpty())
s.enqueue("abc")
s.enqueue("xyz")
s.enqueue("pqr")
print("length=",s.size())
print("data",s.dequeue())
print("data",s.dequeue())
print("data",s.dequeue())
print("length=",s.size())
