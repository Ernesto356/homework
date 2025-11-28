"""
 Portada:
 Nombre: Jesus Ernesto Sanchez Luevano
 Matricula: 2530192
 Grupo: 1-1 IM
 """


"""
Resumen ejecutivo:
This Python file contains solutions to six small programming problems focusing on
use of int, float and bool types, input validation, and clear output messages.
It explains numeric types (int and float), booleans and their derivation from
comparisons, and why range validation and avoiding division by zero are important.
Each problem includes: Description, Inputs, Outputs, Validations and three test cases.

What this document covers: problem descriptions, design of inputs/outputs,
validations, and use of integers, floats and booleans to make decisions.
"""
"""
 Principles and good practices (short notes):
 - Use int for counters and quantities without fractions; use float for
 measurements and rates that can have decimals.
 - Store intermediate results in variables to avoid duplicating complex
 expressions and to improve readability.
 - Always validate inputs before processing (e.g., non-negative checks,
 correct text values) and avoid division by zero.
 - Use descriptive variable names in lower_snake_case and constants in
 UPPER_SNAKE_CASE when needed.
 - Document what true and false mean in each context (printed as 'true' or 'false').
 
 """

"""

 Problem 1: Temperature converter and range flag
 Description: Convert Celsius (float) to Fahrenheit and Kelvin. Determine
 whether the temperature is "high" (>= 30.0 C).

 Inputs:
 - temp_c (float)

 Outputs:
 - "Fahrenheit:" <temp_f>
 - "Kelvin:" <temp_k>
 - "High temperature:" true|false

 Validations:
 - temp_c must be convertible to float
 - Kelvin must be >= 0.0 (physical constraint)

 Test cases:
 1) Normal: temp_c = 25.0 => Fahrenheit: 77.0, Kelvin: 298.15, High temperature: false
 2) Border: temp_c = 30.0 => Fahrenheit: 86.0, Kelvin: 303.15, High temperature: true
 3) Error: temp_c = "abc" => prints "Error: invalid input"
"""
temp_c = input("Insert a temp in celsious:")

try:
    temp_c_number = float(temp_c)
    fahrenheit = temp_c_number * 9.0 / 5.0 + 32.0
    kelvin =  temp_c_number + 273.15
    high_temperature  = (temp_c_number >= 30)
    if kelvin > 0.0 or fahrenheit > -459.67 :
        print(f"{temp_c}C° => {kelvin}K°")
        print(f"{temp_c}C° => {fahrenheit}F°")
        print(f"high temperature => {high_temperature}")
    else:
        print("physical constraint")
except:
    print("Error invalid input")

print("\n------------------------------------")
"""
Problem 2: Work hours and overtime payment
Description: Calculate weekly pay. Up to 40 hours at hourly_rate; overtime
paid at 150% for hours over 40. Provide has_overtime boolean.
Inputs:
- hours_worked (float)
- hourly_rate (float)
Outputs:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false
Validations:
- hours_worked >= 0
- hourly_rate > 0
- otherwise print "Error: invalid input"
Test cases:
1) Normal: hours_worked=45.0, hourly_rate=10.0 => regular=400.0, overtime=75.0, total=475.0, has_overtime=true
2) Border: hours_worked=40.0, hourly_rate=12.5 => overtime=0.0, has_overtime=false
3) Error: hours_worked=-5, hourly_rate=10 => Error
"""

hours_worked = input("Insert the hours worked: ")
hourly_rate =  input("Insert the hourly rate: ")

try : 
    hours_worked = float(hours_worked)
    hourly_rate = float(hourly_rate)

    if hourly_rate >= 0 or hourly_rate > 0 : 
        minimun_hours = min(hours_worked , 40.0)
        maximum_hours = max(0.0, hours_worked - 40)

        regular_pay = minimun_hours * hourly_rate
        overtime_pay = maximum_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = (hours_worked > 40.0)
        print(f"Regular Pay: {regular_pay}")
        print(f"overtime Pay: {overtime_pay}")
        print(f"total Pay: {total_pay}")
        print(f"has overtime: {has_overtime}")


    else:
        print("Error invalid input")

except : 
    print("Error invalid input")

print("\n------------------------------------")
"""
Problem 3: Discount eligibility with booleans
Description: Determine discount eligibility if the customer is a student or
a senior or the purchase_total >= 1000. Apply 10% discount if eligible.
Inputs:
- purchase_total (float)
- is_student_text (string: "YES" or "NO")
- is_senior_text (string: "YES" or "NO")
Outputs:
- "Discount eligible:" truefalse
- "Final total:" <final_total>
Validations:
- purchase_total >= 0.0
- is_student_text and is_senior_text must be "YES" or "NO" (case-insensitive)
Test cases:
1) Normal: purchase_total=1200.0, YES, NO => eligible true, final_total=1080.0
2) Border: purchase_total=1000.0, NO, NO => eligible true, final_total=900.0
3) Error: is_student_text="Y" => Error
"""

purcharse_total = input("Insert the purchase total: ")
is_student = input("Are you a student? (YES/NO): ")
is_senior = input("Are your a senior? (YES/NO): ")
try: 
    purcharse_total_number  = float(purcharse_total)
    if purcharse_total_number <= 0.0:
        print("Error the purchae total cannot be 0 or negative")
        exit()
    total = 0.0
    discount_eligible = (purcharse_total_number >= 1000 or is_student.lower() == "yes" or is_senior.lower() == "yes")
    
    if discount_eligible:
        total = purcharse_total_number - (purcharse_total_number*0.10)
        print (f"Discount eligible : {discount_eligible}")
        print(f"final total : {total}")
    else:
        print (f"Discount eligible : {discount_eligible}")
        print(f"final total : {purcharse_total_number}")
except Exception as error: 

    print(error)


print("\n--------------------------------------------------------")
"""
Problem 4: Basic statistics of three integers
Description: Read three integers and compute sum, average (float), max, min,
and a boolean all_even indicating whether all three are even.
Inputs:- n1 (int), n2 (int), n3 (int)
Outputs:- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false
Validations:- All values must be convertible to int
Test cases:1) Normal: 2,4,6 => Sum:12 Average:4.0 Max:6 Min:2 All even:true
2) Border: 1,2,3 => check odd/even
3) Error: "a",2,3 => Error
"""

number_1 = input("Insert the number One: ")
number_2 = input("Insert the number Two: ")
number_3 = input("Insert the number Three: ")

try:
    number_1 = int(number_1)
    number_2 = int(number_2)
    number_3 = int(number_3)

    sum_numbers = number_1 + number_2 + number_3
    average_numbers = sum_numbers / 3
    maximum_numbers = max(number_1, number_2, number_3)
    minimum_numbers = min(number_1, number_2, number_3)
    all_even = (number_1 % 2 == 0) and (number_2 % 2 == 0) and (number_3 % 2 == 0)

    print(f"Sum: {sum_numbers}")
    print(f"Average: {average_numbers}")
    print(f"Max: {maximum_numbers}")
    print(f"Min: {minimum_numbers}")
    print(f"All even: {all_even}")

except ValueError as error:
    print(f"Error: values must be integers. Details: {error}")
print("\n-----------------------------------")
"""
Problem 5: Loan eligibility (income and debt ratio)
Description: Determine loan eligibility based on monthly_income (float),
monthly_debt (float) and credit_score (int).
Inputs:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
Outputs:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false
Validations:
- monthly_income > 0.0
- monthly_debt >= 0.0
- credit_score >= 0
- otherwise print "Error: invalid input"
Test cases:
1) Normal: income=10000.0 debt=2000.0 score=700 => debt_ratio=0.2 Eligible:true
2) Border: income=8000.0 debt=3200.0 score=650 => debt_ratio=0.4 Eligible:true
3) Error: income=0 => Error (division by zero prevented)
"""

monthly_income = input("Insert the monthly income : ")
monthly_debt = input("Inser the monthly debt : ")
credit_score = input("Inser yout Credit Score: ")

try: 
    monthly_income = float(monthly_income)
    monthly_debt = float(monthly_debt)
    credit_score = float(credit_score)
    debt_radio = 0 
    
    if (monthly_income <= 0.0 ):
        print("Error, division by zero prevented")
    elif(monthly_debt <= 0.0 or credit_score <= 0):
        print("The values cannot by 0")
    else:
        debt_radio = monthly_debt / monthly_income
        elegible = (monthly_income >= 8000.0 and debt_radio <= 0.4 and credit_score >= 650)
        print (f"debt radio : {debt_radio}") 
        print(f"Elegible : {elegible}")


except ValueError as error:
    print(f"Error: {error}")

print("\n-----------------------------------")

"""
Problem 6: Body Mass Index (BMI) and category flag
Description: Compute BMI and booleans for underweight, normal, and overweight.
Inputs:
- weight_kg (float)
- height_m (float)
Outputs:
- "BMI:" <bmi_rounded>
- "Underweight:" true|false
- "Normal:" true|false
- "Overweight:" true|false
Validations:
- weight_kg > 0.0
- height_m > 0.0
Test cases:
1) Normal: weight=70, height=1.75 => BMI ~22.86 Normal:true
2) Border: weight=50, height=1.75 => BMI~16.33 Underweight:true
3) Error: height=0 => Error
"""

weight = input("Insert your weight in kg : ")
height = input("Insert your hright in M : ")
try: 
    weight_kg = float(weight)
    height_m = float(height)
    


    if(weight_kg > 0.0 or height_m > 0.0):
        bmi = weight_kg / (height_m * height_m)
        bmi = round(bmi , 2)
        is_underweight = bmi < 18.5
        is_normal = bmi >= 18.5 and bmi < 25.0
        overweight = bmi >= 25.0
        print(f"BMI : {bmi}")
        print(f"Underweight : {is_underweight}")
        print(f"Normal : {is_normal}")
        print(f"Overweight : {overweight}")
    else :
        print("Error weight or height cannot by 0 or less")
except:
    print("Error Invalid Input")
"""
Conclusiones:
- Los enteros y los números de punto flotante se combinan en cálculos reales: los de punto flotante 
para mediciones (tarifas, ponderaciones, horas) y los enteros para contadores/puntuaciones. 
Su combinación requiere prestar atención a la conversión y al redondeo.
- Las comparaciones (>, >=, ==, etc.) generan valores booleanos que permiten la lógica condicional
(ejemplos: has_overtime, discount_eligible, eligible).
- La validación de rangos (ingresos no negativos, divisores distintos de cero) evita errores en tiempo 
de ejecución, como la división por cero, y aplica restricciones de dominio realistas.
- Las condiciones lógicas compuestas utilizan y/o permiten reglas flexibles (reglas de préstamo, reglas de descuento)
que combinan múltiples requisitos.
- Estos patrones se repiten en nóminas, sistemas de descuento, aprobaciones de préstamos y calculadoras 
de salud, y son fundamentales para un software fiable.
"""
"""
References (minimum 5):
1) Python documentation - Built-in Types: Numeric Types — int, float, complex
https://docs.python.org/3/library/stdtypes.htmlumeric-types-int-float-complex
2) Python documentation - Boolean operations: https://docs.python.org/3/library/stdtypes.htmloolean-operations-and-or-not
3) Python tutorial - Input and Output: https://docs.python.org/3/tutorial/inputoutput.html
4) Real Python - Python Data Types: https://realpython.com/python-data-types/
5) W3Schools - Python Numbers: https://www.w3schools.com/python/python_numbers.asp
6) Any class lecture notes on input validation and simple algorithms.

"""

"""
Url del repositorio de github:
https://github.com/Ernesto356/homework.git
"""
