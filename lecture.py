# El operador morsa (`:=`), también conocido como "operador de asignación de expresión", es una característica
# introducida en Python 3.8. Se utiliza para asignar un valor a una variable como parte de una expresión, y al mismo
# tiempo, permite utilizar ese valor en la misma expresión. Es útil en situaciones donde deseas realizar una operación
# y asignar el resultado a una variable en una sola línea. Aquí tienes un ejemplo y un problema que podrías resolver 
#con el operador morsa:

#Ejemplo:


# Ejemplo de operador morsa
x = 5
if (y := x + 1) > x:
    print("El valor de y es:", y)


#Problema 1:

#Escribe un programa que pida al usuario ingresar dos números y luego imprima el mayor de los dos números junto con su diferencia.

# Problema con operador morsa
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

mayor = num1 if (num1 := num1 if num1 > num2 else num2) > num2 else num2
diferencia = abs(num1 - num2)

print("El mayor número es:", mayor)
print("La diferencia entre los dos números es:", diferencia)
