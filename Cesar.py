import os

def limpiar():
    os.system("cls")

limpiar()

print("1. Cifrar")
print("2. Descifrar")
opcion = input("Opcion: ")
limpiar()

print("1. Ingles")
print("2. Español")
tipo_alfabeto = input("Alfabeto: ")
limpiar()

alfabeto = "abcdefghijklmnopqrstuvwxyz" if tipo_alfabeto=="1" else "abcdefghijklmnñopqrstuvwxyz"

texto = input("Texto: ")
desplazamiento = int(input("Desplazamiento: "))
limpiar()

norm = "aeiou"
tilde = "áéíóú"

resultado = ""

for letra in texto:
    mayus = letra.isupper() # mayusculas
    l = letra.lower() # Lo pasa a minisculas

    p = tilde.find(l) #quitar tilde
    if p != -1:
        l = norm[p] # la pasa sin tilde para cifrarla 

    if l in alfabeto:
        i = alfabeto.index(l)
        i = (i + desplazamiento if opcion=="1" else i - desplazamiento) % len(alfabeto)
        nueva = alfabeto[i]
        resultado += nueva.upper() if mayus else nueva
    else:
        resultado += letra

print("Resultado:", resultado)
input("\n>>>")
limpiar()
