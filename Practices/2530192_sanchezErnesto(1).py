"""
Portada: 
Nombre: Sanchez Luevano Jesus Ernesto
matricula: 2530192
Grupo: 1-1 IM

"""
"""
Este archivo contiene ejercicios prácticos centrados en el uso de funciones en Python.
Una función es un bloque de código reutilizable definido con def que puede aceptar parámetros y valores de retorno. 
Los parámetros son los nombres utilizados en las definiciones de funciones; los argumentos son los valores reales
que se pasan al llamar a la función. Separar la lógica en funciones mejora la modularidad, la capacidad de prueba y la reutilización.
Devolver valores es preferible a solo imprimir, ya que permite un mayor procesamiento y facilita las pruebas unitarias.
Este documento implementa seis problemas, cada uno con una descripción, entradas, salidas, validaciones, casos de prueba y una funció
correspondiente que implementa el comportamiento requerido.
"""

"""
Principios y buenas prácticas (lista corta):
- Preferir funciones pequeñas con una sola responsabilidad.
- Evitar código duplicado; extraer la lógica repetida a las funciones auxiliares.
- Utilizar funciones puras siempre que sea posible: misma entrada -> misma salida, sin efectos secundarios.
- Documentar brevemente la función y los parámetros que espera.
- Usar nombres de función claros: calcular_área, resumir_números, aplicar_descuento.
"""

"""
# Problem 1: Rectangle area and perimeter (basic functions)
# Description: Calculate area and perimeter of a rectangle using two functions.
# Inputs: width (float), height (float)
# Outputs: prints "Area:" and "Perimeter:" with numeric values
# Validations: width > 0 and height > 0
# Test cases:
# 1) Normal: width=5, height=3 -> Area:15, Perimeter:16
# 2) Border: width=0.1, height=0.1 -> small valid values
# 3) Error: width=-2, height=3 -> Error: invalid input
"""

def calculate_area (widht, height):
    return widht * height

def calculate_perimeter(widht, heihgt):
    return 2 * (widht+height)


widht = 0 
height = 0

try: 
    widht = float(input("insert the weight: "))
    height = float(input("insert the height: "))

except:
    widht = 0
    height = 0 

if widht <= 0 or height <= 0 : 
    print("Error the widht or the height cant be less than or equal to 0")
else: 
    area = calculate_area(widht, height)
    perimeter = calculate_perimeter(widht, height)
    print(f"area : {area}")
    print(f"perimeter : {perimeter}")


print("\n -------------------------------")

"""
Problem 2: Grade classifier (function with return string)
Description: Classify a numeric score into letter grade A-F.
Inputs: score (float or int)
Outputs: prints "Score:" and "Category:"
Validations: 0 <= score <= 100
Test cases:
1) Normal: score=92 -> Category: A
2) Border: score=90 -> Category: A; score=89.9 -> B
3) Error: score=150 -> Error: invalid input
"""
def classify_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else : 
        return "F"

try: 
    score =float(input("insert your score: "))
except:
    score = -1

if score < 0 or score > 100:
    print("Error Invalid input")

else: 
    category = classify_score (score)
    print(f" Score {score} \
            Category : {category}")


print ("\n-----------------------")
"""
Problem 3: List statistics function (min, max, average)
 Description: Summarize a list of numbers returning a dict with min, max, average.
 Inputs: numbers_list (list of numbers)
 Outputs: prints "Min:", "Max:", "Average:"
 Validations: list not empty; all elements convertible to numbers
 Test cases:
 1) Normal: "10,20,30" -> Min:10, Max:30, Average:20
 2) Border: "5" -> Min:5, Max:5, Average:5
 3) Error: "10,abc,30" -> Error: invalid input
"""

def summarize_numbers(numbers_list):
    summary = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return summary

numbers_text = input("Insert numbers separated by commas : ").strip()

if not numbers_text:
    print("error invalid input")
else:
    try:
        parts = numbers_text.split(",")
        numbers_list = []

        for part in parts:
            part = part.strip()
            if part == "":
                print("error, the number cannot be null")
            else:
                numbers_list.append(float(part))

        if len(numbers_list) == 0:
            print("Error, the list cannot be null")
        else:
            result = summarize_numbers(numbers_list)
            print(f"Max : {result['max']}")
            print(f"min : {result['min']}")
            print(f"average : {result['average']}")
    except:
        print("Error invalid Input")


print ("\n --------------------")

"""
# Problem 4: Apply discount list (pure function)
 Description: Return a new list with discounted prices, leaving original list unchanged.
 Inputs: prices_list (list of float), discount_rate (float between 0 and 1)
 Outputs: prints "Original prices:" and "Discounted prices:"
 Validations: prices_list not empty, all prices > 0, 0 <= discount_rate <= 1
 Test cases:
 1) Normal: prices=[100,200], discount_rate=0.1 -> [90,180]
 2) Border: discount_rate=0 or 1
 3) Error: negative price or invalid discount_rate
"""

def apply_disocunt (prices_list, discount_rate):
    discounted = []
    for prices in prices_list:
        discounted_prices= prices - (prices*discount_rate)
        discounted.append(discounted_prices)
    return discounted

price_text = input("insert prices: ").strip()
discount_text = input("insert discount rate (0 to 1): ").strip()

if not price_text or  not discount_text:
    print("Error: Invalid input, cannot be null")
else: 
    try:
        discount_rate =float(discount_text) 
        if discount_rate >= 0 or discount_rate < 1:
            parts = price_text.split(",")
            prices_list = []
            for part in parts : 
                part = part.strip()
                if part == "":
                    print("Error the number cannot be null")
                else:
                    price = float(part)
                
                if price < 0: 
                    print("Error, the price cannot be negative")
                else:
                    prices_list.append(price)
            if len(prices_list) == 0 :
                print("Error the number list cannot be null")
            else: 
                discounted_list = apply_disocunt(prices_list, discount_rate)
                print(f"Original prices: {prices_list}" )
                print(f"prices with discount: {discounted_list}")
        else:
            print("Error invalid input")

    except Exception as error:
        print("Error Invalid Input")

print("\n-------------------------------")

"""
 Problem 5: Greeting function with default parameters
 Description: Build greeting using optional title and required name.
 Inputs: name (string), title (string optional)
 Outputs: print "Greeting:"
 Validations: name must not be empty after strip()
 Test cases:
 1) Normal: name='Alice', title='Dr.' -> "Hello, Dr. Alice!"
 2) Border: name='Bob', title='' -> "Hello, Bob!"
 3) Error: name='' -> Error: invalid input
"""


def greet(UserName="", userTitle=""):
    UserName = UserName.strip()
    userTitle = user_title.strip()

    if not user_title:
        return f"{user_name}"
    else:
        return f"{userTitle} {user_name}"


user_name = input("Insert your name: ").strip()
user_title = input("insert your title: ").strip()

if not user_name:
    print("invalid input: User name cannot be null")
else:
    try:

        if not user_title:
            full_name = greet(user_name)
        else:
            full_name = greet(user_name, user_title)
        
        print(f"Greeting: {full_name}")

    except Exception as error:
        print(error)


print("\n-------------------------")
"""
Problem 6: Factorial function (iterative implementation)
 Description: Compute n! using an iterative approach. Iterative chosen to avoid
 deep recursion and stack limits; iterative is simple and efficient for n<=20.
 Inputs: n (int)
 Outputs: prints "n:" and "Factorial:"
 Validations: n integer, 0 <= n <= 20 (to avoid extremely large numbers)
 Test cases:
 1) Normal: n=5 -> 120
 2) Border: n=0 -> 1
 3) Error: n=-1 or n=21 -> Error: invalid input
"""

def factorial_number(n):
    result=1
    for i in range(1 , n+1):
        result = result * i
    return result

number = 0
try: 
    number = int(input("Insert a number (1-20): "))
except:
    number = 0

if number < 1 or number > 20:
    print("Invalid Number: Please insert a number inside the specified range")

else : 
    factorial = factorial_number(number)

    print (f"Number: {number}")
    print (f"Factorial : {factorial}" )
"""
Conclusions:
 Functions help organize code into reusable, testable units and reduce duplication.
 Returning values instead of printing makes functions composable and easier to test.
 Default parameters and named arguments increase flexibility and readability.
 Encapsulating repeated logic (e.g., parsing and validation) simplifies the main flow.
 Separating main program logic from helper functions clarifies responsibilities and
 makes maintenance and debugging easier.


 References:
 1) Python documentation - Defining Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
 2) Python documentation - Data Structures: https://docs.python.org/3/tutorial/datastructures.html
 3) "Fluent Python" (L. Ramalho) - chapters on functions and data model
 4) "Clean Code" concepts applied to Python - articles and tutorials
 5) Official Python style guide (PEP 8) - https://peps.python.org/pep-0008/
 6) Various online tutorials on unit testing and pure functions
 --------------------------------------------------
"""

"""
Url del repositorio de github:
https://github.com/Ernesto356/homework.git
"""