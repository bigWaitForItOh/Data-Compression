#################################################################################################################################
#Huffman Encoding (HC) Algorithm through HC Tree
#Create a HTree Object and call construct () with 1 argument - a dictionary in which key=>character, value=>Frequency of character.
#call get_encodings () on the object to get a dictionary in which key=>character, value=>Huffman Code.
#returns empty dict if construct () was never called or construct () was supplied with empty dict
#Time Complexity: O (Nlog (N))
#################################################################################################################################

from heapq import heapify, heappush, heappop;

class Node (object):
	def __init__ (self, label, weight, left, right):
		self.label = label;
		self.weight = weight;
		self.left, self.right = left, right;

	def __lt__ (self, other):
		return (self.weight < other.weight);

	def describe (self):
		print ('Label: %s\tWeight: %d' % (self.label, self.weight));

class HTree (object):
	def __init__ (self):
		self.root, self.nodes = None, set ();
		self.encodings = {};

	def construct (self, frequencies):
		nodes = [Node (label, frequencies [label], None, None) for label in frequencies] + [Node (None, float ('inf'), None, None)];
		self.encodings = {label : '' for label in frequencies};

		heapify (nodes);

		x, y = heappop (nodes), heappop (nodes);
		while (nodes):
			parent = Node (None, x.weight + y.weight, x, y);
			self.nodes = self.nodes.union (set ([x, y]));

			heappush (nodes, parent);
			x, y = heappop (nodes), heappop (nodes);

		self.nodes.add (x);
		self.root = x;

	def get_encodings (self):
		stack, current = [None], self.root;
		while (current):
			if (current.right):
				stack.append (current.right);
				current = current.left;
			else:
				self.encodings [current.label] = '0';
				current = stack.pop ();
		return (self.encodings);
		
if (__name__ == '__main__'):
	freq = {
		'A' : 5,
		'B' : 9,
	    	'C' : 12,
	    	'D' : 13,
	    	'E' : 16,
	    	'F' : 45
	}
	huff_tree = HTree ();

	huff_tree.construct (freq);
	encodings = huff_tree.get_encodings ();
	for char in encodings: print ('%s : %s' % (char, encodings [char]));
