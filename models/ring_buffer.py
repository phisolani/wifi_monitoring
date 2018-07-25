class RingBuffer:
    def __init__(self, size):
        self.data = [None for i in xrange(size)]

    def __str__(self):
        return str(self.data)

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data