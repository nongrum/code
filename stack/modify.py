class Stack:
    def __init__(k):
       k.item = [] #initilize an empty array

    def is_empty(mty):
        return len(mty.item)==0
    
    def push(mty, item):
        mty.item.append(item)
    def pop(k):
          if not k.is_empty():
      
           return k.item.pop()
          else: 
            print("empy")
    
if __name__=="__main__":  
      
      call=Stack()
      call.push(1)
     
      print(call.is_empty())
      print(call.pop())
      print(call.item)