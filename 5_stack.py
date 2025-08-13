# simply use Python list for Stack implementation
# LIFO: Last In First Out 

stack = []
stack.append(10)   # push
stack.append(20)
stack.append(30)
# stack: [10, 20, 30]

print(stack.pop())  # 30
print(stack.pop())  # 20
print(stack)        # [10]
