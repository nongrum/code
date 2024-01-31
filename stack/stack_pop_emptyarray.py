class Stack:
    def __init__(self):
       self.items = [] #initilize an empty array

    def is_empty(self):
        return len(self.items)==0
    
    def pop(self):
       if not self.is_empty():
          return self.items.pop()
       else:
          print("empty")
    
if __name__=="__main__":  
      
      stak=Stack()
      
      print(stak.is_empty())
      print(stak.pop())
      print(stak.items)