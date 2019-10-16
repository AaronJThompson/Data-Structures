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
        pass

    def get_priority(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
