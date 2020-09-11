lista = []
numero = int(input("ingresar todos los numeros: "))
while numero!=0:
    lista.append(numero)
    numero = int(input("ingresar todos los numeros: "))

print(len(lista))
sum(lista)