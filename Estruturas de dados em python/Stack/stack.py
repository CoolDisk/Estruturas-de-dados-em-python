from node import Node;

'''
A classe stack cria uma pilha que pode possuir um ou mais nós

métodos:

	construtor:

		instancia uma nova lista

		parâmetros:

			top => O topo da lista, o primeiro nó


	push:

		adiciona um novo topo para a lista

		parâmetros:

			value => valor do novo nó para o topo


	pop:

		se a lista possui valores, remove o topo e o retorna,
		senão, lança uma exceção


	peek:

		se a lista possui valores, retorna o valor topo da lista, o deixando intacto,
		senão, lança uma exceção


	clear:

		limpa a pilha


	fill:

		prenchee a pilha com um valor determinado

		parâmetros:

			qt => quantidade de elementos a serem colocados na lista

			val => valor que será colocado em cada novo espaço da lista


'''
class Stack():

	def __init__(self, top):
		self.top = Node(top);
		self.size = 1;

	def push(self, value):
		self.size += 1;
		node = Node(value);
		node.next = self.top;
		self.top = node;

	def pop(self):
		if self.size > 0:
			self.size -= 1;
			if self.top.next is None:
				raise IndexError("A lista não tem um próximo valor");

			self.top = self.top.next;

			return self.top.value;
		else:
			raise IndexError("A lista não possui elementos, não é possível retirar um.")

	def peek(self):
		if self.size <= 0:
			raise IndexError("A lista não possui elementos, não é possível coletar um.")

		if not self.top.next is None:
			return self.top.value;

	def clear(self):
		while self.size > 0:
			try:
				self.pop();
			except:
				continue;

	def fill(self, qt, val):
		for _ in range(0, qt):
			print("val: ",val);
			self.push(val);



# Teste das funcionalidades da lista

# cria lista
stack = Stack(12);

# adiciona 15 à lista
stack.push(15);

# adiciona 16 à lista
stack.push(16);

# escreve o topo da lista
print(stack.peek());

# limpa a lista
stack.clear();

# preenche a lista com 5 espaços com o valor 7
stack.fill(5, 7);

# printa o último valor da lista
print(stack.peek());

# remove os últimos três elementos da pilha
for _ in range(0, 3):
	stack.pop();

# adiciona o elemento 6 para a pilha
stack.push(6);

# printa o topo
print(stack.peek());

# remove os últimos 2 elementos da pilha
for _ in range(0, 1):
	stack.pop();

# printa o último valor restante, 5
print(stack.peek());

# limpa a lista ao final
stack.clear();

# ------------------------------------------by Arthur------------------------------------------
