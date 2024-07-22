class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def remove_max(self):
        if len(self.heap) > 1:
            max_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self._heapify_down(0)
        elif len(self.heap) == 1:
            max_val = self.heap[0]
            self.heap.pop()
        else:
            max_val = None
        return max_val

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        parent_index = self._parent(index)
        if index > 0 and self.heap[parent_index] < self.heap[index]:
            self._swap(parent_index, index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = self._left_child(index)
        right_child_index = self._right_child(index)
        largest = index
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self._swap(largest, index)
            self._heapify_down(largest)


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(2)
max_heap.insert(15)
max_heap.insert(5)
max_heap.insert(4)
max_heap.insert(45)

print(max_heap.remove_max())  
print(max_heap.peek())       





class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def remove_min(self):
        if len(self.heap) > 1:
            min_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self._heapify_down(0)
        elif len(self.heap) == 1:
            min_val = self.heap[0]
            self.heap.pop()
        else:
            min_val = None
        return min_val

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        parent_index = self._parent(index)
        if index > 0 and self.heap[parent_index] > self.heap[index]:
            self._swap(parent_index, index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = self._left_child(index)
        right_child_index = self._right_child(index)
        smallest = index
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        if smallest != index:
            self._swap(smallest, index)
            self._heapify_down(smallest)


min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(2)
min_heap.insert(15)
min_heap.insert(5)
min_heap.insert(4)
min_heap.insert(45)

print(min_heap.remove_min())  
print(min_heap.peek())       