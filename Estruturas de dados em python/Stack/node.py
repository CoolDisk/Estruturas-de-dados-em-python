'''
A classe node representa cada nó da pilha

propriedades:

value => valor do nó
next => o próximo valor da piilha, ou seja, o que está abaixo do atual ex.

| atual |
| next  | << 

'''


class Node():

	next = None;

	def __init__(self, value):
		self.value = value;

		
		
