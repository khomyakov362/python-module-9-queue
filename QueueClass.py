from LinkedListClass import Node

class Queue:
    
    def __init__(self, max_length : int = 10, start : Node = None, finish : Node = None) -> None:
        """Can be initialised as empty, or be given existing start and finish nodes.
            self.start is the last element to be used, self.finish is the only accessible element.
            max_length determines the maximum number of elements in the queue."""

        self.start = start
        self.finish = finish
        self.max_length = max_length
    
    def __reduce_queue(self, func, accumulator = None):
        """Helper method, is used by other methods. Performs a function for each element of the queue.
            Returns some value, which depends of the function. The return value is stored in the accumaltor variable.
            If the accumulator is not given, it is self.start."""

        current_node = self.start
        if accumulator is None:
            accumulator = current_node
        while current_node:
            accumulator = func(accumulator, current_node)
            current_node = current_node.next_node
        return accumulator

    @property
    def length(self):
        """The method returns the current number of elements in the queue."""
        return self.__reduce_queue((lambda acc, el: acc + 1), 0)
    
    def IsEmpty(self) -> bool:
        """Returns True if the queue is empty, otherwise -- False."""
        return not bool(self.finish)
    
    def IsFull(self) -> bool:
        """Returns True if the queue is full, otherwise -- False."""
        return self.length == self.max_length
    
    def Show(self) -> None:
        """Displays the contents of the queue."""
        self.__reduce_queue(lambda acc, el: print(el.data))
        if self.IsEmpty():
            print('The queue is empty.')
    
    def Enqueue(self, data : str) -> None:
        """Adds an element to the beginning of the queue if it is not full."""

        if self.IsFull():
            print('The queue is full. No more elements can be added.')
            return
        
        if self.start is None:
            self.start = Node(data)
            self.finish = self.start
        else:        
            new_node = Node(data, self.start)
            self.start = new_node
    
    def Dequeue(self):
        """Removes the element at self.finish from the queue and returns it."""

        if self.IsEmpty():
            print('The queue is empty.')
            return
        
        if self.start is self.finish:
            value = self.start.data
            self.start = None
            self.finish = None
            return value
        
        second_to_last = self.__reduce_queue(lambda acc, el: el if el.next_node is self.finish else acc)
        value = self.finish.data
        second_to_last.next_node = None
        self.finish = second_to_last
        return value
