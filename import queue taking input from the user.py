import queue

priority_queue = queue.PriorityQueue()

# Take input from the user and insert elements into the priority queue
for r in range(3):
    p1 = input("enter p1:")
    i1 = input("enter item:")
    priority_queue.put(p1,i1)

while not priority_queue.empty():
    priority, item = priority_queue.get()
    print(f"priority: {priority}, item: {item}")
