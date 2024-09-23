"""
Task
Given an integer, , perform the following conditional actions:

If is odd, print Weird
If is even and in the inclusive range of to , print Not Weird
If is even and in the inclusive range of to , print Weird
If is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .
Constraints
Output Format
Print if the number is weird. Otherwise, print .WeirdNot Weird
Sample Input 0
3
Sample Output 0
Weird
Explanation 0
n = 3
n is odd and odd numbers are weird, so print .Weird
Sample Input 1
24
Sample Output 1
Not Weird
Explanation 1
n = 24
n > 20 and is even, so it is not weird.
"""

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())    
    
if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
elif n > 20:
    print("Not Weird")

"""    
Explicación del Código
1- Lectura de la entrada: n = int(input().strip()) lee el número entero desde la entrada 
estándar y elimina cualquier espacio adicional.

2- Condición de imparidad: if n % 2 != 0 verifica si el número es impar (el residuo de la 
división por 2 no es cero).

3- Condiciones para números pares:
elif 2 <= n <= 5: Verifica si el número está en el rango de 2 a 5.
elif 6 <= n <= 20: Verifica si el número está en el rango de 6 a 20.
elif n > 20: Verifica si el número es mayor que 20.

4- Salida: Dependiendo de la condición que se cumple, el programa imprime el mensaje correspondiente.
"""

