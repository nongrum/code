def great():
    print("hello")
    print("goodmorning")   
great()
great()

def add(x,y): 
    c = x+y
    print(c)
add(4,5)
add(4,4)
#return
def sub(x,y):
    c = x-y
    d = x*y
    e =x+y 
    return c, d, e
result1, result2, result3= sub(5,9)
print(result1, result2, result3)
