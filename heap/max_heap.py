class Heap:
    def __init__(self):
        self.storage = []
        # This makes the math easier
        self.storage[0] = None

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def __swap__(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
