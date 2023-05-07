# python3

import sys

class Solver:
	def __init__(self, s):
		self.s = s
		self.m1 = 10 ** 9 + 7
		# self.m2 = 10 ** 9 + 9
		self.x = 777777 # random
		self.calculate_prefix_x()
		self.hash_all_prefix()

	def calculate_prefix_x(self):
		self.prefix_x = [1 for _ in range(len(self.s))]
		for i in range(1,len(self.s)):
			self.prefix_x[i] = (self.prefix_x[i-1] * self.x) % self.m1

	def hash_all_prefix(self):
		self.all_prefix = [0 for _ in range(len(self.s))]
		for i in range(1,len(self.s)):
			self.all_prefix[i] = ((ord(s[i-1]) + self.all_prefix[i-1]) * self.x) % self.m1 

	def ask(self, a, b, l):
		h_a = (self.all_prefix[a + l] - self.prefix_x[l] * self.all_prefix[a]) % self.m1
		h_b = (self.all_prefix[b + l] - self.prefix_x[l] * self.all_prefix[b]) % self.m1
		return h_a == h_b

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
