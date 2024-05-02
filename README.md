### EL OPERADOR MORSA


El operador morsa de Python (:=): Todo lo que necesitas saber
 

Una buena práctica en Python, y en cualquier otro lenguaje de programación, es buscar la forma de hacer el código más limpio, conciso y legible. El operador morsa de Python (:=) es un avance significativo en este sentido. Introducido en la versión 3.8 de Python, permite asignar valor a variables donde antes no era posible. En esta publicación se explicará qué es el operador morsa de Python, por qué se introdujo, cómo usarlo y varios casos de uso práctico.

### Por qué se introdujo el operador morsa de Python (:=)

El operador morsa, también conocido como el operador de asignación de expresiones de fusión, es una característica relativamente nueva del lenguaje. Apareció por primera vez en 2019 con el lanzamiento de la versión 3.8. El operador se representa mediante dos puntos seguidos de un signo igual (:=). Su principal función es permitir la asignación de valores a variable dentro de una expresión, al mismo tiempo que se evalúa esta. Algo que no se podía hacer antes de la su introducción. Antes de Python 3.8, era necesario realizar la asignación de valores en una línea separada y evaluar el resultado en otra, lo que a menudo resultaba en una sintaxis más complicada.

Siendo este el motivo por el que se introdujo el operador morsa de Python. Solucionar el problema que provocaba la repetición innecesaria de expresiones y la dificultad para escribir código limpio y conciso en ciertas situaciones. Al permitir la asignación de variables dentro de expresiones el código resultante es más legible. Lo que facilita el mantenimiento y la colaboración en proyectos de desarrollo de software.

## Cómo usar el operador morsa de Python
El uso del operador morsa es bastante sencillo, solamente se coloca dentro de la expresión donde se necesita evaluar esta y el resultado se asigna a la variable. A continuación, se muestran algunos ejemplos.

### Asignación de variables en condicionales
Uno de los usos más habituales del operador morsa es dentro de los condicionales. Es posible que sea necesario realizar una operación, comprobar si cumple una condición y sacar el valor por pantalla. Esto, antes de la aparición del operador morsa se debía hacer en varias líneas.
```PYTHON
suma = a + b

if suma > 100:
    print(f'La suma es {suma}')
```
Una operación que se puede simplificar mucho con esta operación.
```PYTHON
if (suma:= a + b) > 100:
    print(f'La suma es {suma}')
```
En este caso, gracias al uso del operador morsa, se puede asignar la suma de a mas b a la variable sumaen el propio if y usar posteriormente dentro de la función print(). Lo que hace el código mucho más compacto.

### Asignación de variables en bucles
Otro posible uso del operador aparece en los bucles, pudiendo asignar el valor en el momento que se valida. Por ejemplo, en un bucle while en el que se está procesando un archivo se puede cargar la línea de esta antes de procesarla.
```PYTHON
while (linea := archivo.readline()) != "":
    procesar_linea(linea)
```
Sin el operador, el código necesario sería bastante más complejo.
```PYTHON
linea = archivo.readline()

while linea != "":
    procesar_linea(linea)
    
    linea = archivo.readline()
```
### Asignación de variables en listas por comprensión
Gracias a ***las listas por comprensión de Python*** se puede escribir código compacto y elegante. Pero qué pasa si necesitamos filtrar en base al resultado de una función e incluir este resultado en la lista. En este caso el código tendría que ser cómo el siguiente.
```PYTHON
[calcular_resultado(x) for x in lista_valores if calcular_resultado(x) > 0]
```
Lo que implica ejecutar hasta dos veces la función sobre todos los valores. Una opción para evitar tener que evaluar dos veces la función es aplicar la función sobre todos los valores y luego volver a iterar para filtrar.
```PYTHON
[y for y in [calcular_resultado(x) for x in lista_valores] if y > 0]
```
Solución que también es complicada de leer. En este caso el uso del operador morsa de Python hace que el código sea sencillo y fácil de leer.
```PYTHON
[res for x in lista_valores if (res := calcular_resultado(x)) > 0]
```
Desde mi punto de vista la última lista por compresión es bastante más sencilla y elegante. Además de evitar que sea necesario evaluar dos veces una función que podría ser bastante costosa en tiempo de ejecución.

## Conclusiones
El operador morsa es una nueva característica de Python que simplifica la asignación de variables dentro de expresiones. Facilitando la escritura de código más limpio, conciso y legible. En esta entrada se ha explorado el origen del operador morsa y visto algunos de los casos de uso de este.