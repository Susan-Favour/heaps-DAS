#Question 001: Implement a heap data structure
class MinHeap:
    def __init__(self):
        # Initialized an empty list to store heap elements
        self.heap = []
    def insert(self, val):
        # Added the new value to the end of the list
        self.heap.append(val)
        # Heapifyed up to maintain the heap property
        self._heapify_up(len(self.heap) - 1)
    def extract_min(self):
        if len(self.heap) == 0:
            # If the heap is empty, raise an error
            raise IndexError("extract_min from an empty heap")
        # Swaped the root (minimum element) with the last element
        self._swap(0, len(self.heap) - 1)
        # Removed the last element (previous root) and stored it
        min_val = self.heap.pop()
        # Heapifyed down from the root to maintain the heap property
        self._heapify_down(0)
        # Returned the minimum element
        return min_val
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        # Continued to heapify up until the heap property is restored
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            # Swaped the current element with its parent
            self._swap(index, parent_index)
            # Updated the current index to the parent's index
            index = parent_index
            # Recalculated the parent index
            parent_index = (index - 1) // 2
    def _heapify_down(self, index):
        # Continued heapifying down until the heap property was restored
        while (index * 2 + 1) < len(self.heap):
            # Assumed the left child is the smaller child
            smallest = index * 2 + 1
            right_child = index * 2 + 2
            # If the right child exists and is smaller, update smallest
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child
            # If the current element is smaller than both children, break
            if self.heap[index] <= self.heap[smallest]:
                break
            # Swaped the current element with the smaller child
            self._swap(index, smallest)
            # Updated the current index to the smallest child's index
            index = smallest
    def _swap(self, i, j):
        # Swaped the elements at indices i and j
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(4)
min_heap.insert(15)
min_heap.insert(20)
min_heap.insert(0)
min_heap.insert(8)

print(min_heap.extract_min())  
print(min_heap.extract_min())  
print(min_heap.extract_min())

min_heap.insert(3)
print(min_heap.extract_min())  

#Question 002: Find the k-th Largest Element in an Array
import heapq
def find_kth_largest(nums, k):
    # Created a min-heap with the first k elements of the array
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    # Iterated over the remaining elements in the array
    for num in nums[k:]:
        # If the current element is larger than the smallest element in the heap
        if num > min_heap[0]:
            # Replace the smallest element with the current element
            heapq.heapreplace(min_heap, num)
    # The root of the heap is the k-th largest element
    return min_heap[0]

array = [3, 2, 1, 5, 6, 4]
k = 2
result = find_kth_largest(array, k)
print(f"The {k}-th largest element in the array is: {result}")

#Question 003: Find the k-th smallest Element in a heap 
import heapq
def find_kth_smallest(heap, k):
    # Created a copy of the heap to avoid modifying the original heap
    min_heap = heap[:]
    heapq.heapify(min_heap)
    # Extracted the minimum element k times
    kth_smallest = None
    for _ in range(k):
        kth_smallest = heapq.heappop(min_heap)
    return kth_smallest


heap = [3, 2, 1, 5, 6, 4]
k = 3
result = find_kth_smallest(heap, k)
print(f"The {k}-th smallest element in the heap is: {result}")

#Question 004: Merge k Sorted Lists
import heapq
def merge_k_sorted_lists(lists):
    # Created a min-heap
    min_heap = []
    # Pushed the first element of each list along with the list index and element index
    for i, lst in enumerate(lists):
        if lst:  # Check if the list is not empty
            heapq.heappush(min_heap, (lst[0], i, 0))
    # List to store the result
    result = []
    # While there are elements in the heap
    while min_heap:
        # Pop the smallest element from the heap
        val, list_index, element_index = heapq.heappop(min_heap)
        result.append(val)
        # If there is a next element in the same list, push it to the heap
        if element_index + 1 < len(lists[list_index]):
            next_element = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_element, list_index, element_index + 1))
    return result

lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]
merged_list = merge_k_sorted_lists(lists)
print(merged_list) 

#Question 005: Given an array of points where each point is an integer pair (x,y) , return k the closest points to the origin(0,0)
import heapq
def k_closest_points(points, k):
    # Created a max-heap to store the closest k points
    max_heap = []
    # Iterated through each point in the array
    for (x, y) in points:
        # Calculated the squared distance from the origin
        distance = x**2 + y**2
        # Push the negative of the distance along with the point to the heap
        # We use negative distance to simulate a max-heap using heapq which is a min-heap by default
        heapq.heappush(max_heap, (-distance, (x, y)))
        # If the heap size exceeds k, pop the farthest point
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    # Extract the points from the heap
    return [point for (_, point) in max_heap]

points = [(1, 3), (-2, 2), (5, 8), (0, 1)]
k = 2
closest_points = k_closest_points(points, k)
print(closest_points)  

#Question 006: Given a stream of numbers, compute the running median of the list so far after each new element
import heapq
class RunningMedian:
    def __init__(self):
        # Max-heap for the lower half of the numbers
        self.lower_half = []
        # Min-heap for the upper half of the numbers
        self.upper_half = []
    def add_number(self, num):
        # Added number to the max-heap (lower half)
        heapq.heappush(self.lower_half, -num)
        # Balance the heaps: ensured the max-heap's max is less than or equal to the min-heap's min
        if self.lower_half and self.upper_half and (-self.lower_half[0] > self.upper_half[0]):
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        # Balance the sizes of the heaps to ensure the size property
        if len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        elif len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))
    def get_median(self):
        # If the number of elements is odd, the max-heap will have one extra element
        if len(self.lower_half) > len(self.upper_half):
            return -self.lower_half[0]
        # If the number of elements is even, the median is the average of the two heaps' roots
        return (-self.lower_half[0] + self.upper_half[0]) / 2

stream = [5, 15, 1, 3]
running_median = RunningMedian()
medians = []
for number in stream:
    running_median.add_number(number)
    medians.append(running_median.get_median())
print(medians)  # Output: [5, 10.0, 5, 4.0]

#Question 007: Given a string, find the first K non-repeating characters in it
from collections import Counter, deque
def first_k_non_repeating_characters(string, k):
    # Count the frequency of each character in the string
    char_count = Counter(string)
    # Create a queue to store the non-repeating characters in the order they appear
    non_repeating_queue = deque()
    # Iterate through the string and add non-repeating characters to the queue
    for char in string:
        if char_count[char] == 1:
            non_repeating_queue.append(char)
    # Retrieve the first K non-repeating characters from the queue
    result = []
    while non_repeating_queue and len(result) < k:
        result.append(non_repeating_queue.popleft())
    return result

string = "swiss"
k = 2
first_k_non_repeating = first_k_non_repeating_characters(string, k)
print(first_k_non_repeating)  

#Question 008: Given an array of meeting time intervals consisting of start and end times[start1, end1] ,[start2, end2]. …, [startN, endN] determine if a person could attend all meetings
def can_attend_all_meetings(intervals):
    # Sorted the intervals by their start times
    intervals.sort(key=lambda x: x[0])
    # Iterated through the intervals and checked for overlaps
    for i in range(1, len(intervals)):
        # If the start time of the current meeting is less than the end time of the previous meeting
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True

intervals = [[0, 30], [5, 10], [15, 20]]
can_attend = can_attend_all_meetings(intervals)
print(can_attend)  
intervals = [[7, 10], [2, 4]]
can_attend = can_attend_all_meetings(intervals)
print(can_attend)  


    

 







