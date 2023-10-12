#sQ.1) Write a Program to implement stack and demonstrate push, pop and peek operations in python.

class stack:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
       return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
       return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s=stack()
print("data",s.isEmpty())
for i in range(1,10):
    s.push(i)
 
#s.push("true")
for i in range(1,10):
  print("data",s.pop())
#print("data",s.pop())
print("length=",s.size())
    
