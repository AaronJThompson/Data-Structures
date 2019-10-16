import math
class Heap:
    def __init__(self):
        self.storage = []
        # This makes the math easier
        self.storage.append(None)

    def insert(self, value):
        self.storage.append(value)
        if self.get_size() > 1:
            self._bubble_up(len(self.storage) - 1)

    def delete(self):
        self.__swap__(1, len(self.storage) - 1) #Move top element to end
        max_node = self.storage.pop()
        self._sift_down(1)
        return max_node

    def get_max(self):
        if self.get_size() > 0:
            return self.storage[1]

    def get_size(self):
        return len(self.storage) - 1

    def __swap__(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    def _bubble_up(self, index):
        if index <= 1:
            return
        parent = math.floor(index / 2)
        if self.storage[index] > self.storage[parent]:
            self.__swap__(index, parent)
            self._bubble_up(parent)

    def _sift_down(self, index):
        left_child = index * 2
        right_child = left_child + 1

        if left_child < len(self.storage) - 1 and self.storage[left_child] > self.storage[index]:
            self.__swap__(left_child, index)
            self._sift_down(left_child)
        if right_child < len(self.storage) - 1 and self.storage[right_child] > self.storage[index]:
            self.__swap__(right_child, index)
            self._sift_down(right_child)
