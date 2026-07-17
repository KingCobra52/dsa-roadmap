import ctypes

class DynamicArray:
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.array = self._make_array(self.capacity)

    def __len__(self):
        return self.length

    def _make_array(self, new_capacity):
        #creates a new ctypes array of a given state
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if not 0 <= i < self.length:
            raise IndexError("Index out of bounds")
        return self.array[i]

    def append(self, item):
        #self.capacity must be > self.length
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.length] = item
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("Does not exist")
        value = self.array[self.length - 1]
        self.array[self.length - 1] = None
        self.length -= 1

        return value

    def _resize(self, new_capacity):
        # TODO: allocate a bigger array, copy old elements over, swap it in
        self.capacity = new_capacity
        new_array = self._make_array(new_capacity)
        for index in range(self.length):
            new_array[index] = self.array[index]
        self.array = new_array
