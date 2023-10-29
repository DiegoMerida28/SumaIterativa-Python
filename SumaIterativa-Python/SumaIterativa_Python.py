num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

suma = 0

for i in range(num2):
    suma += num1

print(f"La suma de {num1} y {num2} es: {suma}")
