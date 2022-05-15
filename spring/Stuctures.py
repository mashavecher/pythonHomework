class Stack:
    def __init__(self):
        self.value = []

    def add_value(self, value):
        if value == '':
            raise ValueError('no value given')
        self.value.append(value)
        return self.value

    def remove_value(self):
        if len(self.value) <= 0:
            raise IndexError('Stack is empty')
        return self.value.pop(-1)


class Container:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.end = None

    def empty(self):
        return self.front is None

    def add_to_queue(self, item):
        temp = Container(item)
        if self.end is None:
            self.front = self.end = temp
            return
        self.end.next = temp
        self.end = temp

    def remove_from_queue(self):
        if self.empty():
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.end = None
