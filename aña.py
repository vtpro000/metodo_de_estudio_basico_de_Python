#crear calculadora
def sumar(a, b):                      
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

print("calculadora")
print("1. Sumar")
print("2. Restar")