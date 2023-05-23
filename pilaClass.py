class Pila():
    
    def __init__(self):  #metodo constructor self-> referencia al abjeto que esta llamando
        self.elements = []

    def push(self, dato):
        self.elements.append(dato)

        

    def pop(self):
        if self.size() > 0:
            dato = self.elements.pop()
            return dato
        
    def size(self):
        return len(self.elements)

    
    def on_top(self):
        if self.size() > 0:
            return self.elements[-1]



pila_1 = Pila()
pila_1.push(3)
print(pila_1.size(), pila_1.elements)
pila_1.push(6)
print(pila_1.size(), pila_1.elements)
pila_1.push(1)
print(pila_1.size(), pila_1.elements)

print(pila_1.pop())
print(pila_1.size(), pila_1.elements)
print(pila_1.pop())
print(pila_1.size(), pila_1.elements)
print(pila_1.pop())
print(pila_1.size(), pila_1.elements)
print(pila_1.pop())
print(pila_1.size(), pila_1.elements)