import math
class Heap:
    def __init__(self, comparator = None):
        self.storage = []
        self.comparator = comparator
        if comparator is None:
            # Default to max heap
            self.comparator = lambda x, y: x > y

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        self.__swap__(0, len(self.storage) - 1) #Move top element to end
        max_node = self.storage.pop()
        self._sift_down(0)
        return max_node

    def get_priority(self):
        if self.get_size() > 0:
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index < 1:
            return
        parent = math.ceil(index / 2) - 1
        if self.comparator(self.storage[index], self.storage[parent]):
            self.__swap__(index, parent)
            self._bubble_up(parent)


    def _sift_down(self, index):
        pass

    def __swap__(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
