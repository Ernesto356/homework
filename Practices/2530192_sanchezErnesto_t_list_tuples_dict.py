"""
0000000_SanchezLuevanoJesusErnesto.py
Matricula: 0000000
Group: A


-----------------------------------------------------------------------------
Resumen ejecutivo (6-10 líneas):
Este archivo demuestra el uso de listas, tuplas y diccionarios de Python.
Una lista es una colección ordenada y mutable (se pueden añadir o eliminar elementos).
Una tupla es ordenada e inmutable (útil para registros fijos como coordenadas).
Un diccionario asigna claves a valores para realizar búsquedas rápidas (p. ej., nombre -> precio).
El documento contiene 6 pequeños programas que muestran usos prácticos, entradas, salidas, validaciones y 3 casos de prueba por problema.
--------------------------------------------------------------------------------
Principios y mejores prácticas (notas breves):
- Use listas cuando necesite añadir o eliminar elementos con frecuencia.
- Use tuplas para datos que no deben cambiar (coordenadas, constantes).
- Use diccionarios para búsquedas con clave (p. ej., id -> registro).
- Evite modificar una lista mientras la itera; es preferible crear una nueva lista. 
- Utilice claves descriptivas ("nombre", "precio", "calidades"). Redacte mensajes legibles.

Template for each problem (will appear before code of each problem):
Problem X: <short title>
Description: 2-4 lines explaining what the program does.
Inputs:
- ...
Outputs:
- ...
Validations:
- ...
Test cases:
1) Normal: ...
2) Border: ...
3) Error: ...

"""

"""
-----------------------------------------------------------------------------
Problem 1: Shopping list basics (list operations)
Description:
Work with a list of product names (strings). Create initial list from a
comma-separated string, add a new item to the end, show total items and
check whether a search item exists (boolean is_in_list).
Inputs:
- initial_items_text (string) e.g. "apple,banana,orange"
- new_item (string)
- search_item (string)
Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false
Validations:
- initial_items_text not empty after strip()
- new_item and search_item not empty after strip()
Test cases:
1) Normal: "apple, banana, orange", new_item="pear", search_item="banana"
2) Border: initial_items_text=" " (empty) -> treat as empty list
3) Error: new_item=" " -> "Error: invalid input"
"""

initial_list = input("Insert the products: ").strip()
new_item = input("Insert the new Item: ").strip()
search_Item = input("Enter the item to search for: ").strip()

if not new_item or not search_Item:
    print("Error the values cannot be null")
else:
    if initial_list == "":
        items = []
    else:
        items = [item.strip() for item in initial_list.split(",") if item.strip()]
    

    items.append(new_item)
    quantity = len(items)
    found_item = search_Item in items

    print(f"""
    item List : {items}
    Total Items : {quantity}
    found item : {found_item}
    """)


print("\n--------------------------------------------")
"""
-----------------------------------------------------------------------------
Problem 2: Points and distances with tuples
Description:
Represent two 2D points as tuples, compute Euclidean distance and midpoint.
Inputs:
- x1, y1, x2, y2 (floats)
Outputs:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)
Validations:
- Ensure inputs can be converted to float
Test cases:
1) Normal: 0,0 and 3,4 -> distance 5.0 midpoint (1.5,2.0)
2) Border: same point -> distance 0.0
3) Error: non-numeric input -> "Error: invalid input"

"""
point_A = input("Insert the fisrt coordinates: ")
point_B = input("Insert the second coordinates: ")

try:
    point_A_numbers = tuple([float(n) for n in point_A.split(",")])
    point_B_numbers = tuple([float(n) for n in point_B.split(",")])

    distance = ((point_A_numbers[0]-point_B_numbers[0])**2 + (point_A_numbers[1]-point_B_numbers[1])**2)**0.5
    midpoint = ((point_A_numbers[0] + point_B_numbers[0])/2 , (point_A_numbers[1] + point_B_numbers[1])/2)
    print(f"""
    point A: {point_A_numbers}
    point B : {point_B_numbers}
    distance : {distance}
    midpoint : {midpoint}
    """)
except:
    print("Error invalid Input")

"""    
Problem 3: Product catalog with dictionary
Description:
Manage a small catalog mapping product name -> unit price. Read product
name and quantity, compute total, or return error if product not found.
Inputs:
- product_name (string)
- quantity (int)
Outputs:
- If exists: "Unit price:", "Quantity:", "Total:"
- If not: "Error: product not found"
Validations:
- product_name not empty
- quantity > 0 and convertible to int
Test cases:
1) Normal: "apple", 2
2) Border: quantity = 1
3) Error: product not in catalog
"""
print("\n--------------------------------------------")

products = {
    "sabritas" : 16.5,
    "arroz" : 23.5,
    "frijoles" :20.4 
}
product_name = input("Enter the product you wish to purchase: ").strip().lower()
quantity_product = input("how many products? : ").strip().lower()

try:
    quantity_product = int(quantity_product)
    if product_name == "":
        print("Invalid input the name product cannot be null")
    else:
        if product_name in products :
            unit_price =  products[product_name]
            total_price = quantity_product * unit_price

            print(f"""
            unit Price {unit_price}
            quantity_product {quantity_product}
            total {total_price}
            """)
        else: 
            print("Sorry the product not exist")
        
        

        
except:    
    print("Error Invalid Inputs")

print("\n---------------------------------")

"""
Problem 4: Student grades with dict and list
Description:
Maintain dictionary student -> list of grades. Compute average and
boolean is_passed (average >= 70.0).
Inputs:
- student_name (string)
Outputs:
- If exists: "Grades:", "Average:", "Passed:"
- If not: "Error: student not found"
Validations:
- student_name not empty
- Check student exists and grades list not empty
Test cases:
1) Normal: existing student with grades
2) Border: student with single grade = 70 -> passed
3) Error: student not in dict

"""

grades = {
    "josue" : [100, 100, 90],
    "maiki" : [100, 100 ,100],
    "jorgito" : [50, 50, 60]  
}

name_estudent = input("Insert the name : ").strip().lower()

if name_estudent == "":
    print("Erro invalid input")
else:
    if name_estudent in grades : 
        estudent_ratings = grades[name_estudent]
        average = sum(estudent_ratings) / len(estudent_ratings)
        passed = average >= 70
        print(f"""
                Estudent : {name_estudent}
                estudent ratings : {estudent_ratings}
                average : {average}
                passed : {passed}
""")
    else: 
        print("The estudent not found")

print("\n---------------------------------")
"""
Problem 5: Word frequency counter (list + dict)
Description:
Count frequency of each word in a sentence. Produce words list, freq dict
and the most common word (any if tie).
Inputs:
- sentence (string)
Outputs:
- "Words list:", "Frequencies:", "Most common word:"
Validations:
- sentence not empty after strip()
- Optionally remove simple punctuation by replacement
Test cases:
1) Normal: "Hello hello world"
2) Border: sentence with punctuation
3) Error: empty sentence
"""

sentence = input("Insert the sentence: ").strip().lower().replace(",", "")
words = {}
sentence = sentence.split()


if not sentence : 
    print("Error Invalid Input")

else:
    for word in sentence:
        words[word] = 0

    for word in sentence:
        if word in words:
            words[word] += 1
    
    frecuent = max(words, key=words.get)
    print(f"""
    words : {sentence}
    frecuencies : {words}
    most common : {frecuent}
""")

print("\n---------------------------------")


"""
Problem 6: Simple contact book (dictionary CRUD)
Description:
Implement a contact book supporting ADD, SEARCH, DELETE actions.
Inputs:
- action_text (string: "ADD","SEARCH","DELETE")
- name (string)
- phone (string for ADD)
Outputs:
- "Contact saved:" name, phone
- "Phone:" phone
- "Contact deleted:" name
- "Error: contact not found"
Validations:
- action_text normalized to uppercase and valid
- name and phone not empty where required
Test cases:
1) Normal: ADD new contact, SEARCH it, DELETE it
2) Border: ADD existing contact (update)
3) Error: SEARCH non-existing
"""

contacts = {
    "josue" : "8340000000",
    "maiki" : "1234567890",
    "amgel": "24680121416"
}

def add(data, name, number):
    if name in data : 
        data[name] = number
        return "Los datos fueron cambiados con exito"
    else:
        data[name] = number
        return "Los datos fueorn agregados con exito"
    
def search_contact(data, name):
    if name in data:
        return data.get(name)
    else : 
        return ("Contact not found")
def delete_contact(data, name):
    if name in data:
        del data[name]
        return "Deleted contact"
    else:
        return "Contact not found"
while True:
    print("""
        Select A option: 
        1) ADD
        2) SEARCH
        3)DELETE
        0)EXIT
        """)
    option = input("Insert A option: ")
    if option == "0":
        break
    elif option == "1":
        print("\n----ADD----")
        name = input("Insert a name to yout contact : ").strip()
        number = input("Insert a number :").strip()
        if not name or not number :
            print("\n The values cannor be null")
            continue
        else:
            add_contact = add(contacts,name,number)
            print(add_contact)

    elif option == "2":
        print("---SEARCH---")
        name = input("Insert a name to search :").strip()
        if not name : 
            print("\n the name cannot be null")
        else:
            search = search_contact(contacts,name)
            print(f"number : {search}")
    
    elif option == "3":
        print("\n---Delete---")
        name = input("Insert a name to yout contact : ").strip()
        if not name : 
            print("\n the name cannot be null")
        else:
            delete = delete_contact(contacts,name)
            print(delete)

"""
-----------------------------------------------------------------------------
Conclusions (5-8 lines) - comments
Lists are flexible for dynamic collections where insert/delete are common.
Tuples are useful for fixed records (coordinates) and can be used as dict keys.
Dictionaries provide fast key-based access, ideal for catalogs and contact books.
Combining structures (e.g., dict of lists) is a common pattern for grouped data.
Always validate inputs and provide clear error messages for robustness.
-----------------------------------------------------------------------------


References (minimum 5) - comments
References:
1) Python documentation - Built-in Types: list, tuple, dict - https://docs.python.org/3/library/stdtypes.html
2) Python tutorial - Data Structures - https://docs.python.org/3/tutorial/datastructures.html
3) "Automate the Boring Stuff with Python" - Al Sweigart
4) "Think Python" - Allen B. Downey
5) Real Python - Python Lists and Dictionaries tutorials - https://realpython.com
"""

"""
Url del repositorio de github:
https://github.com/Ernesto356/homework.git
"""