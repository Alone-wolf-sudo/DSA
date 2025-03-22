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
    # return stack

def pop(stack):
    if is_empty(stack):
        print("Stack is empty")
    else:
        stack.pop()
        print("popped element from stack")

def peek(stack):
    if is_empty(stack):
        print("stack is empty")
    else:
        print("Top element is",stack[-1])

def print_stack(stack):
    print("stack elements are ",stack)


if __name__ == "__main__":
    # Creating a stack
    stack = create_stack()
    # Push elements
    push(stack, 10)
    push(stack, 11)
    push(stack, 12)
    # Pop elements
    pop(stack)
    # peek elements
    peek(stack)
    # print elements
    print_stack(stack)
