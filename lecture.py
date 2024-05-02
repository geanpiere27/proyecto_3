
#1. **Estructuras condicionales (if-elif-else)**:
   
#Problema: Escribe un programa que determine si un número es positivo, negativo o cero.

num = float(input("Ingrese un número: "))
if num > 0:
       print("El número es positivo.")
elif num < 0:
       print("El número es negativo.")
else:
       print("El número es cero.")


#2. Bucles (for, while):
#Problema: Suma los primeros n números naturales.

n = int(input("Ingrese un número: "))
suma = 0
for i in range(1, n+1):
       suma += i
print("La suma de los primeros", n, "números naturales es:", suma)


#3.Bucles (break, continue):

#Problema: Encuentra el primer número positivo divisible por 17 entre 1 y 100.

for i in range(1, 101):
       if i % 17 == 0:
           print("El primer número positivo divisible por 17 es:", i)
           break


#4.Manejo de excepciones (try-except):

# Problema: Manejar la división por cero.
   
try:
       num = int(input("Ingrese un número: "))
       result = 10 / num
       print("El resultado de la división es:", result)
except ZeroDivisionError:
       print("Error: No se puede dividir entre cero.")
except ValueError:
       print("Error: Ingrese un número válido.")


# 5.Listas por comprensión:

# Problema: Generar una lista de los cuadrados de los números del 1 al 10.

squares = [x**2 for x in range(1, 11)]
print("Los cuadrados de los números del 1 al 10 son:", squares)


#6.Funciones recursivas:

# Problema: Calcular el factorial de un número.

def factorial(n):
       if n == 0:
           return 1
       else:
           return n * factorial(n-1)

num = int(input("Ingrese un número para calcular su factorial: "))
print("El factorial de", num, "es:", factorial(num))

