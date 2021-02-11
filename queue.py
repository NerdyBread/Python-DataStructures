# Explaination

# A queue is a data structure with two operations
	# queue
	# dequeue (I bet you can guess where those names come from)

# The queue operation adds an item to the end of the queue
	# So if it looked like this to start:
		# (start) 1, 2, 3 (end)
	# And I queued 4, it would look like:
		# (start) 1, 2, 3, 4 (end)

# Dequeue removes the item at this start (and usually returns it), which would be the least recent item added
	# From the example before, if I were to dequeue I would wnd up with:
	# (start) 2, 3, 4 (end)

# A queue operates like a line (or queue) in real life
# Like at a store, the first person in line checks out first, then the person behind them, and so on

# Code starts here

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Queue:
	def __init__(self, start=None):
		self.start = Node(start)
		self.end = None  # Both begin as the same value

	def queue(self, val):
		"""Add an item to the end of the queue"""
		if not self.start:
			self.start = Node(val)
			self.end = None

		elif not self.end:
			self.end = Node(val)
			self.start.next = self.end

		else:
			# Add item to the end, make that item the end
			self.end.next = Node(val)
			self.end = self.end.next
	
	def dequeue(self):
		"""Remove the item at the beginning of the queue and return it"""
		start_val = self.start.val
		self.start = self.start.next
		return start_val

	def __str__(self):
		"""String representation of an object"""
		pointer = self.start
		ret = "Start-->"
		while pointer:
			ret += f"{pointer.val}->"
			pointer = pointer.next
		ret += " End"
		return ret

	def __iter__(self):
		"""Function that acts as an iterator, also known as a generator"""
		pointer = self.start
		while pointer:
			yield pointer.val
			pointer = pointer.next

if __name__ == '__main__': # Example usage
	test = Queue(20)
	test.queue(12)
	test.queue(4)
	test.queue(8)
	test.dequeue()
	print(test) # Uses __str__()
	for item in test:  # Uses __iter__(), could also be written as iter(test) or test.__iter__()
		print(item)
	