my_list = []
def insert_element (value):
    my_list.append (value)
def delete_element (value):
    if value in my_list :
        my_list.remove (value)
    else:
        print ("it empty")
        
def display ():
    print (my_list)
 
insert_element (6)
insert_element (10)
insert_element (15)
insert_element (20)
insert_element (30)
insert_element (25) 
insert_element (20)
display ()  
delete_element (7) # it will print it empty because value is not on the list
delete_element(10)
delete_element(15)
delete_element(5) 
delete_element(20)
display() 
 