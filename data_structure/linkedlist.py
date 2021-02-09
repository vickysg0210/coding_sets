class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleLinkList(object):
    def __init__(self):
        self._head = None
    def is_empty(self):
        return self._head is None
# the head acts as the pointer for the first node and the data it points to
    def add(self, item):
        node = Node(item)
        node.next = self._head
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
