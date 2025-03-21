# This is to Learn all about Stack Data Structure
# Stack Operations: Push, Pop, Peek, isEmpty, isFull


def create_stack():
    stack = []
    return stack

def is_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

def push(stack, element):
    stack.append(element)
    print("pushed element to stack")

def pop(stack, element):
    if is_empty(stack):
        print("Stack is empty")
    else:
        stack.pop(element)
        print("popped element from stack")

def peek(stack):
    if is_empty(stack):
        print("stack is empty")
    else:
        print(stack[-1])


if __name__ == "__main__":
    # Creating a stack
    stack = create_stack()
    # Push elements
    stack = push(stack, 10)
    # Pop elements
    # peek elements
