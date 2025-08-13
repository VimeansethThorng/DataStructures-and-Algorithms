from collections import deque

queue = deque()

# Enqueue: Append to right → enqueue
queue.append("A")
queue.append("B")
queue.append("C")

# Dequeue: Pop from left → dequeue
print(queue.popleft())  # A
print(queue.popleft())  # B
print(queue)            # deque(['C'])
