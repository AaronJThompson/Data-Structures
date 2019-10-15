"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
        return self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
        return self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        return self


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.head is not None:
            self.head.insert_before(value)
        elif self.tail is None:
            node = ListNode(value)
            self.head = self.tail = node
        self.length += 1



    def remove_from_head(self):
        if self.head is not None:
            return self.head.delete()
            self.length -= 1

    def add_to_tail(self, value):
        if self.tail is not None:
            self.tail = self.tail.insert_after(value)
        else:
            self.add_to_head(value)
        self.length += 1


    def remove_from_tail(self):
        if self.tail is not None:
            self.tail = self.tail.delete().prev
            self.length -= 1

    def move_to_front(self, node):
        value = node.value
        if self.head is node:
            return
        if self.tail is node:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)


    def move_to_end(self, node):
        value = node.value
        if self.tail is node:
            return
        if self.head is node:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    def delete(self, node):
        pass

    def get_max(self):
        pass
