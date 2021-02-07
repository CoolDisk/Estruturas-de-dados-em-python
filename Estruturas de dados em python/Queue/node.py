'''
A classe node representa cada nó da fila

propriedades:

value => valor do nó
next => o próximo valor da fila, ou seja, o que está atrás dele.

| atual |  | next | <<

'''


class Node():

    next = None;

    def __init__(self, value):
        self.value = value;
