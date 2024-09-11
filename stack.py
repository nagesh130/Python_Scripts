class  stack:
    def __init__(self):
      self.items = []

    def isempty(self):
        return  self.items

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def Peek(self):
        return self.items(len(self.items))

    def size(self):
        return len(self.items)

# locad values on the stack

s = stack()

# look that cals the range of 20 that loads the values into the stack
for x in range(22):
    s.push(x)

# prints the stack
print (s.isempty())


print(s.size())