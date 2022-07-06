from dataclasses import dataclass

@dataclass
class NumberNode:
	value: float

	def eval(self):
		return self.value

	def __repr__(self):
		return f"{self.value}"

@dataclass
class AddNode:
	node_a: any
	node_b: any

	def eval(self):
		return self.node_a.eval() + self.node_b.eval()

	def __repr__(self):
		return f"({self.node_a}+{self.node_b})"

@dataclass
class SubtractNode:
	node_a: any
	node_b: any

	def eval(self):
		return self.node_a.eval() - self.node_b.eval()

	def __repr__(self):
		return f"({self.node_a}-{self.node_b})"

@dataclass
class MultiplyNode:
	node_a: any
	node_b: any

	def eval(self):
		return self.node_a.eval() * self.node_b.eval()

	def __repr__(self):
		return f"({self.node_a}*{self.node_b})"

@dataclass
class DivideNode:
	node_a: any
	node_b: any

	def eval(self):
		return self.node_a.eval() / self.node_b.eval()

	def __repr__(self):
		return f"({self.node_a}/{self.node_b})"

@dataclass
class PlusNode:
	node: any

	def __repr__(self):
		return f"(+{self.node})"
	
@dataclass
class MinusNode:
	node: any

	def __repr__(self):
		return f"(-{self.node})"