from node import Node;

from random import randint;

'''
A classe queue cria uma fila que pode possuir um ou mais nós

métodos:

	construtor:

		instancia uma nova fila

		parâmetros:

			first => O primeiro valor da fila, o primeiro nó


    __len__:

        retorna o tamanho da fila


	push:

		adiciona um novo valor para a fila

		parâmetros:

			value => valor do novo nó para o final


	pop:

		se a fila possui valores, remove o primeiro e o retorna,
		senão, lança uma exceção


	peek:

		se a fila possui valores, retorna o primeiro valor da fila, o deixando intacto,
		senão, lança uma exceção


	clear:

		limpa a fila


	fill:

		prenchee a fila com um valor determinado

		parâmetros:

			qt => quantidade de elementos a serem colocados na fila

			val => valor que será colocado em cada novo espaço da fila


    __peer__:

        retorna uma lista contendo todos os elementos da fila




'''
class Queue():

    _size = 0;

    def __init__(self, first):
        self.first = Node(first);
        self.last = self.first;
        self._size += 1;

    def __len__(self):
        return self._size;

    def push(self, val):
        node = Node(val);
        if self.last is None:
            self.last = node;
        else:
            self.last.next = node;
            self.last = node;
        if self.first is None:
            self.first = node;

        self._size += 1;

    def pop(self):
        if self._size > 0:
            if not self.first is None:
                self.first = self.first.next;
                self._size -= 1;
                return self.first;
        else:
            raise IndexError("A fila está vazia");

    def peek(self):
        if self._size > 0:
            if not self.first is None:
                return self.first.value;
            else:
                raise IndexError("A fila não possui um primeiro elemento");
        else:
            raise IndexError("A fila está vazia");

    def clear(self):
        for c in range(0, self._size):
            print(c);
            self.pop();

    def fill(self, qtd, val):
        for c in range(0, qtd):
            self.push(val);

    def __peer__(self):
        values = [];
        values.append(self.first.value);
        cur_value = self.first;
        for i in range(0, self._size):
            if not cur_value.next is None:
                pointer = cur_value.next;
            else:
                continue;
            values.append(pointer.value);
            cur_value = pointer;

        return values;

# Teste das funcionalidades da fila

# cria a fila
queue = Queue(12);

# adiciona 13 a fila
queue.push(13);

# preenche a fila com 5 valores 3
queue.fill(5, 3);

# printa todos os valores da fila
for i in queue.__peer__():
    print(i);

# printa o primeiro valor da pilha
print(queue.peek());

# limpa a fila
queue.clear();

# adiciona 5 valores aleatórios entre 1 a 999 para a fila
for _ in range(0, 5):
    n = radint(1, 999);
    queue.push(n);

# printa a lista de todos os valores da fila
print(queue.__peer__());

# remove o primeiro elemento
queue.pop();

# escreve o novo primeiro elemento
print(queue.peek());

# ------------------------------------------by Arthur------------------------------------------
