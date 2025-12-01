"""
 0000000_SanchezJesus.py
 Portada:
 Name: Jesus Ernesto Sanchez Luevano
 Matricula: 0000000
 Group: A

 Resumen ejecutivo:
Este archivo contiene seis pequeños programas de Python que ilustran el uso de bucles for y while,
 incluyendo ejemplos que usan for con rango, para iterar una lista y varios patrones de bucle while 
 (centinela, intentos limitados, menú interactivo). Cada problema está documentado con descripción, 
 entradas, salidas, validaciones y tres casos de prueba (normal, borde, error).
El código está dividido en funciones para que los casos de prueba se puedan ejecutar automáticamente
 en el entorno principal.

Principios y buenas prácticas (notas breves):
- Usar "for" cuando se conoce el número de iteraciones de antemano (for i in range(...)).
- Usar "while" cuando las iteraciones dependen de una condición (por ejemplo, leer hasta 'EXIT').
- Inicializar contadores y acumuladores antes de los bucles.
- Actualizar las variables de control dentro de los bucles "while" para evitar bucles infinitos.
- Mantener los cuerpos de los bucles pequeños; extraer lógica compleja en funciones.

"""
"""
---------------------------
Problem 1: Sum of range with for
Description: Calculate the sum of integers from 1 to n (inclusive) and the sum of even
numbers in the same range using a for loop.
Inputs:
- n (int)
Outputs:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>
Validations:
- n must be convertible to int and n >= 1
- On invalid input: print "Error: invalid input"
Test cases:
1) Normal: n = 10 -> Sum 55, Even sum 30
2) Border: n = 1 -> Sum 1, Even sum 0
3) Error: n = 0 -> Error"""

n = input("Insert A number : ").strip()
try:
    n = int(n)
    sum = 0
    even_sum = 0

    for i in range(n+1):
        sum += i

        if i % 2 == 0:
            even_sum += i
    
    print(f"""
additions = {sum}
Even sum = {even_sum}
""")
except:
    print("Error invalid input")

print("\n------------------------------------")
"""
Problem 2: Multiplication table with for
Description: Print multiplication table for base from 1 to m.
Inputs:
- base (int)
- m (int)
Outputs:
- Lines like: "5 x 1 = 5"
Validations:
- base and m convertible to int, m >= 1
- On invalid input: print "Error: invalid input"
Test cases:
1) Normal: base=5, m=4 -> lines for 1..4
2) Border: base=2, m=1 -> one line
3) Error: base=3, m=0 -> Error
"""
print("\n------------------------------------")

try:

    base = int(input("Insert the base: "))
    m = int(input("Insert the limit of the multiplication table: "))

    for i in range (1, m+1):
        print(f"{base} * {i} = {i*base}")

except:
    print("Error invalid input")
"""

Problem 3: Average of numbers with while and sentinel
Description: Read floats until sentinel (-1) is entered. Compute count and average.
Inputs:
- a list of input values (strings or numbers). Sentinel is -1.
Outputs:
- "Count:" <count>
- "Average:" <average_value>
- If no valid data -> "Error: no data"
Validations:
- Each value must be convertible to float (except sentinel handling)
Test cases:
1) Normal: [1.0, 2.0, 3.0, -1] -> Count:3 Average:2.0
2) Border: [-1] -> Error: no data
3) Error: ["a", -1] -> "Error: invalid input"""

print("\n------------------------------------")
number = ""
numbers = []

while number != "-1":
    number = input("\nInsert a Number: ").strip()

    if number == "-1" and not numbers:
        print("Error: No Data")
        break

    if number == "-1":
        print("Exit")
        break
    try:
        float(number)   
    except ValueError:
        print("Error: Solo se permiten números.")
        continue
    numbers.append(number)
try:
    numbers_float = [float(n) for n in numbers]

    addition = sum(numbers_float)
    average = addition / len(numbers_float)

    print(f"""
    addition: {addition}
    average: {average}
    """)
except:
    print("No Data")
print("\n------------------------------------")
"""
Problem 4: Password attempts with while
Description: User has MAX_ATTEMPTS to provide correct password.
Inputs:
- a list of attempted passwords (strings) - simulations of user input
Outputs:
- "Login success" on success
- "Account locked" if attempts exhausted
Validations:
- MAX_ATTEMPTS is a positive integer
Test cases:
1) Normal: attempts: ["wrong","admin123"] -> Login success (on second try)
2) Border: attempts: ["admin123"] -> Login success (first try)
3) Error: attempts exhausted without correct password -> Account locked
"""


MAX_ATTEMPS = 5
password = "Admin_1234"
counter = 0

while counter < MAX_ATTEMPS: 
        pin = input("Insert your pin: ")
        if (password == pin):
            print("WELCOME")
            break
        
        else : 
            print("Incorrect PIN")
            counter+=1
            remaining_attemps= MAX_ATTEMPS - counter
        
        if remaining_attemps > 0 :
            print(f"Incorrect pin : {remaining_attemps}")
        else:
            print("You have exceeded the maximum number of attempts. Your account has been blocked.")
print("\n------------------------------------")
"""
# ---------------------------
# Problem 5: Simple menu with while
# Description: Simple text menu loop. In this file we simulate the user's selections by
# providing a list of options to feed the menu. The menu supports: 1 (greet), 2 (show counter),
# 3 (increment counter), 0 (exit). Invalid options produce an error message.
#
# Inputs:
# - a list of option inputs (strings or ints) to simulate a user interacting with the menu.
#
# Outputs:
# - prints messages according to options. For batch mode, function returns the concatenated log.
#
# Validations:
# - options must be convertible to int and in {0,1,2,3}
#
# Test cases:
# 1) Normal: ["1","3","2","0"] -> Hello! then Counter incremented then Counter:1 then Bye!
# 2) Border: ["0"] -> Bye!
# 3) Error: ["9","0"] -> Error: invalid option then Bye!
# 
# """
counter_menu = 0

while True:
    try:
        print("""
             1 : Greeting
             2: show counter
             3: increment counter,
             0: Exit
""")
        option = int(input("Selec One Option :"))
    except:
        print("Error invalid input")
        continue

    if option == 0:
        print("bye bye ^^")
        break
    elif option == 1:
        print("HIIIII!!!1")
    elif option == 2:
        print(f"counter : {counter_menu}")
    elif option == 3:
        print("Counter incremented succefully")
        counter_menu += 1
    else:
        print("Error: invalid option")



print("\n------------------------------------")
"""

Problem 6: Pattern printing with nested loops
Description: Print a right triangle of asterisks with n rows. Optionally print inverted pattern.
Inputs:
- n (int)
Outputs:
- lines containing 1..n asterisks
- optional inverted pattern after
Validations:
- n convertible to int and n >= 1
Test cases:
1) Normal: n=4 -> lines: *,**,***,****
2) Border: n=1 -> *
3) Error: n=0 -> Error"""

try:
    n = int(input("Insert the quantity to the triangle : ").strip())

    if n > 0: 
        for i in range(1,n+1):
                print("*" * i)
        
        for i in range(n-1, 0, -1): #Lo hice nomas pa que vea que hay nivel,  y porque esta bien facil
            print("*" * i)
    else : 
        print("Error INvalid Input")
except:
    print("Error Invalid Inpuy")

"""
Conclusions:
- For loops are best when the number of iterations is known; while loops are ideal when
repetition depends on a condition or user input.
- Counters and accumulators simplify counting and summation tasks inside loops.
- While loops must update control variables (like attempts or sentinel checks) to avoid
infiniteloops; always reason about termination conditions.
- Menus and password attempts are typical real-world examples of while loops.
- Nested loops make pattern generation simple; complexity grows multiplicatively.

# References (minimum 5):
# 1) Python documentation - The for statement. https://docs.python.org/3/tutorial/controlflow.html
# 2) Python documentation - The while statement. https://docs.python.org/3/tutorial/controlflow.html
# 3) "Automate the Boring Stuff with Python" by Al Sweigart (loops chapter)
# 4) Real Python - Python For Loops. https://realpython.com/python-for-loop/
# 5) W3Schools - Python While Loops. https://www.w3schools.com/python/python_while_loops.asp
# 6) Lecture notes for Programming Basics (course material)
# 
# """

"""
Url del repositorio de github:
https://github.com/Ernesto356/homework.git
"""