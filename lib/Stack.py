class Stack:

    def __init__(self, items = [], limit = 100):
        pass
        self.items = []
        self.limit = limit

        for item in items:
            if(not self.full()):
                self.items.append(item)


    def isEmpty(self):
        pass
        return self.items == []

    def push(self, item):
        pass
        if (not self.full()):
            self.items.append(item)
        else:
            return None

    def pop(self):
        pass
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        pass
    
        return self.items[len(self.items)]

    def size(self):
        pass
        return len(self.items)

    def full(self):
        pass

        if (len(self.items) >= self.limit):
            return True
        return False

    def search(self, target):
        pass
        for i in reversed(range(len(self.items))):
            if self.items[i] == target:
                return len(self.items) -1  - i 
        return -1