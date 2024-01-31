import queue

priority_queue = queue.PriorityQueue()

num1 = int(input("Enter total number of items: "))
for r in range(num1):
    p1 = int(input("Enter priority: "))
    item = input("Enter item: ")
    priority_queue.put((p1, item))

while not priority_queue.empty():
    priority, item = priority_queue.get()
    print(f"priority:{priority}, item:{item}")
