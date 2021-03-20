from chapter2.linkedlist import Node


class Stack():
    def __init__(self, data):
        self.top = Node(data)

    def pop(self):
        if self.top is not None:
            item = self.top.data
            self.top = self.top.next
            return item
        else:
            print("Nothing to pop")

    def push(self, item):
        if self.top is not None:
            new_node = Node(item)
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = Node(item)

    def peek(self):
        if self.top is not None:
            return self.top.data
        else:
            print("Nothing to peek")

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

if __name__ == "__main__":
    test_stack = Stack(10)
    print(test_stack.peek())
    test_stack.push(30)
    test_stack.push(50)
    print(test_stack.peek())
    print(test_stack.pop())
    print(test_stack.peek())