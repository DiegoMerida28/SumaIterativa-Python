num1 = int(input("Ingresa el primer n�mero: "))
num2 = int(input("Ingresa el segundo n�mero: "))

suma = 0

for i in range(num2):
    suma += num1

print(f"La suma de {num1} y {num2} es: {suma}")
