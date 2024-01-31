class Stack:
    def __init__(self):
       self.items = [] 

    def push(self, item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items)==0
    def  peek(self):
        if not self.is_empty():
           return self.items[-1]
        else:
           print("empty")
     
    def size (self):
       return len(self.items)
    
    def pop(self):
       if not self.is_empty():
          return self.items.pop()
       else:
          print("empty")
if __name__=="__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    

    print(stack.is_empty()) #false
    print(stack.peek()) #3
    print(stack.pop())  #3
    print(stack.size()) # 2
    print(stack.items) #[1,2]

