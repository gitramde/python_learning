"""
Python does not have a built-in stack data structure, but we can use a list for the same purposes.

    1. append() - [O(1)] push an element to the stack
    2. pop() - [O(1)] Remove and return the top element of the stack
    3. [-1] - [O(1)] to access top element of the stack without removing it
    4. len() - [O(1)] to check if the stack is empty

"""
from collections import deque
stack = []
stack.append(1)
stack.append(2)
print(f"Created a stack and appended 2 elements: {stack}")

stack = [1, 2]
top_element = stack.pop() # 2
print(f"Removing the top element and returning it: {top_element}")

stack = [1, 2]
top_element = stack[-1] # 2
print(f"Just accessing the top element: {top_element})

stack = [1, 2]
print(f"accessing the stack (LIFO): ")
while len(stack) > 0:
    print(stack.pop())


