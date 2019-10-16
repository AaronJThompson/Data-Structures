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
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass

    def __swap__(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
