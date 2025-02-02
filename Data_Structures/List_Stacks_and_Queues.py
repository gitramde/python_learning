"""
Python does not have a built-in stack data structure, but we can use a list for the same purposes.

    1. append() - [O(1)] push an element to the stack
    2. pop() - [O(1)] Remove and return the top element of the stack
    3. [-1] - [O(1)] to access top element of the stack without removing it
    4. len() - [O(1)] to check if the stack is empty

"""
# STACK - Push and Pop

from typing import List

stack = []
stack.append(1)
stack.append(2)
print(f"Created a stack and appended 2 elements: {stack}")

stack = [1, 2]
top_element = stack.pop() # 2
print(f"Removing the top element and returning it: {top_element}")

stack = [1, 2]
top_element = stack[-1] # 2
print(f"Just accessing the top element: {top_element}")

stack = [1, 2]
print("accessing the stack (LIFO): ")
while len(stack) > 0:
    print(stack.pop())

def reverse_list(arr: List[int]) -> List[int]:
    arr_reverse = []
    while len(arr) > 0:
        arr_reverse.append(arr.pop())
    return arr_reverse

print("Reverse List")
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))


"""
A DEQUE stands for Double-Ended Queue is a data structure that is part of Collections module. 
It is a data structure that allows adding and removing elements from both ends efficiently. 
Regular Queue is FIFO (First In, First Out) principles, but a deque supports both FIFO and LIFO

Operations on deque:
append(x)	        - Adds x to the right end of the deque.	O(1)
appendleft(x)	    - Adds x to the left end of the deque.	O(1)
pop()	            - Removes and returns an element from the right end of the deque.	O(1)
popleft()	        - Removes and returns an element from the left end of the deque.	O(1)
extend(iterable)    - Adds all elements from iterable to the right end of the deque.	O(k)
extendleft(iterable)- Adds all elements from iterable to the left end of the deque (reversed order).	O(k)
remove(value)       - Removes the first occurrence of value from the deque. Raises ValueError if not found.	O(n)
rotate(n)	        - Rotates the deque n steps to the right. If n is negative, rotates to the left.	O(k)
clear()	            - Removes all elements from the deque.	O(n)
count(value)	    - Counts the number of occurrences of value in the deque.	O(n)
index(value)	    - Returns the index of the first occurrence of value in the deque. 
                      Raises ValueError if not found.	O(n)
reverse()	        - Reverses the elements of the deque in place.	O(n)
"""
# QUEUE - Enqueue and Dequeue

from collections import deque

