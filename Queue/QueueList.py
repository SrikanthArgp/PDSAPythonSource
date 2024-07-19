from abc import ABCMeta, abstractmethod


class AbstractQueue(metaclass=ABCMeta):

    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    @abstractmethod
    def enqueue(self, value):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue(AbstractQueue):

    def __init__(self):
        super().__init__()
        self._front = None
        self._rear = None

    def __iter__(self):
        probe = self._front
        while True:
            if probe is None:
                return
            yield probe.value
            probe = probe.next

    def enqueue(self, value):
        node = QueueNode(value)
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self._front.value
        if self._front is self._rear:
            self._front = None
            self._rear = None
        else:
            self._front = self._front.next
        self._size -= 1
        return value

    def peek(self):
        """returns the front element of queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._front.value



queue :LinkedListQueue = LinkedListQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)



# test __len__()
print(len(queue))

# test is_empty()
print(queue.is_empty())

# test peek()
print(queue.peek())

# test dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

print(queue.is_empty())