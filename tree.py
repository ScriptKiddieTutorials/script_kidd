"""
My own implementation of a tree after trial and error
may not be the most efficient/clean way to do this
but hey, at least I'm original!!
"""

class Node():
	LEN = 3
	# Don't do this. It's horrible
	# Just don't.
	# Please.
	# It's reminiscent of the 'default iterable argument' "bug"

	# children = []

	# node_list = []
	def __init__(self, parent, c, depth):
		self.cnt = 0
		self.children = [] # Always do this instead.

		self.c=c
		self.depth = depth

		self.parent = parent
		if self.parent is not None:
			self.parent.children.append(self)
			print(f"Added {self} to {self.parent}")


	def __repr__(self):
		return f"<{self.c}>"


	def __str__(self):
		return f"<{self.c}::{self.children}>"


	def __getitem__(self, i):
		return self.children[i]


	def _get_unique(self, c):
		for child in self.children:
			if child.c == c:
				return child

		return Node(self, c, depth=self.depth+1)

	def get_unique(self, c):
		child = self._get_unique(c)
		child.cnt += 1
		return child


root = Node(None, None, 0)

def iter_to_tree(node, string):
	for c in string:
		node = node.get_unique(c)
	return node


node1 = iter_to_tree(root, "123")
node2 = iter_to_tree(root, "12a")


