# Explaination


# A linked list is a data structure that's kind of like a normal list (or array)
# A linked list is more flexible

# A linked list is made up of "nodes"
# These nodes have two parts:
	# Whatever value it's storing
	# And a pointer to the next node in the list

# So a node can be imagined as:
	# (val=6, pointer=where to find next node)

# A linked list is just many of these nodes LINKED together

	#   head  pointer                 Linked lists end with None
	#    (6)   -->   (4)   -->   (2)   -->   None

# Any given linked list is just its head, and the rest of the list is accessed by it

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

	def addNode(self, val):
		"""Add a new node to the end of a linked list"""
		pointer = self
		while pointer.next:
			pointer = pointer.next
		pointer.next = Node(val)

	def removeNode(self, val):
		"""Remove a node from the linked list"""
		pointer = self
		if pointer.val == val:
			self = self.next
		else:
			while pointer.next.val != val:
				pointer = pointer.next
			pointer.next = pointer.next.next


	def __str__(self):
		"""A magic method (worth reading about) that returns a string representation of an object"""
		pointer = self
		ret = str()
		while pointer.next:
			ret += f"{pointer.val}-->"
			pointer = pointer.next
		ret += str(pointer.val)
		return ret
	
	def __iter__(self):
		"""A magic method that's a generator"""
		pointer = self
		while pointer:
			yield pointer.val
			pointer = pointer.next


if __name__ == '__main__': # Example usage
	head = Node(16)
	head.addNode(8)
	head.addNode(4)

	head.removeNode(8)

	print(head) # If __str__() method wasn't included this would print something like:
				# <__main__.Node object at 0xrandomMemoryAddress>

	for i in head: # This uses __iter__()
		print(i)
