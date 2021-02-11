# Explaination

# A stack is a data structure that can perform two operations:
	# Push
	# And Pop

# Push adds and item to the "top" of the stack
# Pop removes an item from the "top" of the stack

# That means that the stack uses "first in last out (FILO)"

	# Meaning that if you were to start a stack with the 2, "push" 4 to it, and "push" 8 to it,
	# the stack would be something like this:
		# 8 (the top)
		# 4
		# 2 (the bottom)

	# Notice 2 is at the bottom of the stack

# Now if we were to "pop" an item from that stack, the item removed would be 8 because it's at the top
# Then the stack would be:
	# 4 (the new top)
	# 2 (still the bottom)


# Code starts here
	
class Node:
	"""Used to hold one value in the stack along with it's references (pointers to other nodes)"""
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

class Stack:
	def __init__(self, top=None):
		self.top = Node(top)
	
	def push(self, val):
		"""Adds item to the top of the stack"""
		if not self.top: 
			# If the stack is empty, the top becomes this value
			self.top = val
		else:
			# Otherwise, the new value is added above the top and becomes the top
			self.top.next = Node(val)
			self.top.next.prev = self.top
			self.top = self.top.next

	def pop(self):
		"""Removes the top node and returns it's value"""
		top_val = self.top.val
		self.top = self.top.prev
		return top_val

	def isEmpty(self):
		# I figured I'd throw something in about good code practice, specifically returning booleans
		# Someone's first instinct might be something like:
		"""
		if self.top is None: (or "if not self.top")
			return True
		else:
			return False
		"""
		# But there is a better way, instead return the boolean directly and skip the if-else
		return self.top is None # If there is no top, the stack is empty, and this condition will be true, 

	def __str__(self):
		"""String representation of an object"""
		pointer = self.top
		ret = "Top-->"
		while pointer:
			ret += f"{pointer.val}\n      "
			pointer = pointer.prev
		return ret

	def __iter__(self):
		"""Function that acts as an iterator, also known as a generator"""
		pointer = self.top
		while pointer:
			yield pointer.val
			pointer = pointer.prev

if __name__ == '__main__': # Example usage
	test = Stack(10)
	test.push(4)
	test.push(7)
	test.push(5)
	test.push(6)

	test.pop()
	test.pop()

	for item in test: # This uses __iter__()
		print(item)

	print(test) # Implicitly calls __str__()
