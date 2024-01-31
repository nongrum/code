class Stack:
    def __init__(self):
       self.items = [] #initilize an empty array

    def is_empty(self):
        return len(self.items)==0
    
    def push(self, item):
        self.items.append(item)
    
      

if __name__=="__main__":
      
      stak=Stack()
      stak.push(1)
      stak.push(2)
      stak.push(3)
      print(stak.is_empty())
      print(stak.items)
      stak.pop(())