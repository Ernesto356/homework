"""
 Portada:
 Name: Jesus Ernesto Sanchez Luevano
 Matricula: 2530192
 Grupo: IM 1-1


 """

"""
 RESUMEN EJECUTIVO (6-10 líneas)
Una cadena en Python es una secuencia de texto (tipo 'str') y es inmutable: 
las operaciones que modifican una cadena producen una nueva cadena. Las operaciones básicas 
incluyen concatenación, medición de longitud, segmentación, búsqueda, reemplazo y división.
Validar y normalizar la entrada (eliminar, mayúsculas/minúsculas) es esencial para evitar 
comparaciones incorrectas y datos malformados (por ejemplo, correos electrónicos y contraseñas). 
Este archivo contiene seis problemas que muestran la creación, normalización, validación y operaciones
comunes con cadenas, junto con casos de prueba y documentación.
"""


"""
 PRINCIPIOS Y MEJORES PRÁCTICAS
- Las cadenas son inmutables: las operaciones crean nuevas cadenas.
- Normalice la entrada usando strip() y lower() antes de comparar.
- Evite los números mágicos para los índices; documente las porciones.
- Prefiera los métodos de cadena integrados a las implementaciones manuales.
- Validación: primero compruebe si hay vacíos (después de strip()), luego aplique las reglas de formato.
- Use nombres de variable claros (lower_snake_case) y mensajes de salida en inglés.

 """

 
""" 
 Problem 1: Full name formatter
 Description:
 Given a full name string, normalize and return Title Case and initials.
 Inputs:
   - full_name (string)
 Outputs:
   - Formatted name: "<Name In Title Case>"
   - Initials: "X.X.X."
 Validations:
   - Not empty after strip()
   - At least two words
 Test cases:
   1) Normal: "juan carlos tovar"
   2) Border: " ana  lopez " (two words with extra spaces)
   3) Error: "   " (only spaces)
 """

full_name = input("insert your full name: ").strip()

name = full_name.split()


if not full_name or len(name) < 2:
    print("Error, your name cannot be null or only one")

else:
    print (f"your name is: {full_name.title()}")
    
    initials = ""
    for word in name: 
        initials=initials+word[0].upper()+"."

    print(f"initials: {initials}")

print("\n---------------------------------------")

"""
 Problem 2: Simple email validator
 Description:
 Validate basic email structure: exactly one '@', at least one '.' after '@', and no spaces.
 Inputs:
   - email_text (string)
 Outputs:
   - "Valid email: true/false" and if true "Domain: <domain_part>"
 Validations:
   - Not empty after strip()
   - Exactly one '@'
   - No spaces
 Test cases:
   1) Normal: "user@example.com"
   2) Border: "user@sub.example.co"
   3) Error: " user@@example .com " or "userexample.com"
 ---------------------------"""

email = input("Insert a email : ").strip()

if not email: 
    print("Error, the email cannot be null")
else:
    if " " in email: 
        print("error, The email cannot contain blank spaces.")
    elif email.count("@") != 1:
        print("Error the gmail need contain only one @")
    else:
        at_index = email.find("@")
        domain = email[at_index +1: ]
        if "." in domain:
            print("Valid email")
            print(f"domain: {domain}")
        else:
            print("the domain need one '.'")
print("\n---------------------------------------")
"""
 Problem 3: Palindrome checker (ignoring spaces and case)
 Description:
 Check whether a phrase is a palindrome ignoring spaces and case.
 Inputs:
   - phrase (string)
 Outputs:
   - "Is palindrome: true/false" and optionally normalized version
 Validations:
   - Not empty after strip()
   - At least 3 characters after removing spaces
 Test cases:
   1) Normal: "Anita lava la tina"
   2) Border: "aba"
   3) Error: "  " or "ab"

"""

phrase = input("insert a phrase : ").strip()
if not phrase:
    print("the phrase cannot be null")
else:
    phrase_normal = phrase.lower().replace(" ", "")
    if len(phrase_normal)<3:
        print("Is palindrome: false")
    else: 
        reversed_text = phrase_normal[::-1]
        if reversed_text == phrase_normal:
            print("the phrase is a palindrome")
        else:
            print("the phrase not is a palindrome")
print("\n---------------------------------------")

# ---------------------------
# Problem 4: Sentence word stats (lengths and first/last word)
# Description:
# Given a sentence, normalize spaces and return word count, first, last, shortest, longest words.
# Inputs:
#   - sentence (string)
# Outputs:
#   - Word count, First word, Last word, Shortest word, Longest word
# Validations:
#   - Not empty after strip()
#   - At least one word after split()
# Test cases:
#   1) Normal: "  The quick brown fox  "
#   2) Border: "Hello"
#   3) Error: "    "
# ---------------------------

sentence = input("write a sentence : ").strip()
if not sentence:
    print("the sentence cannot be null")
else:
    sentence_list = sentence.split()
    print(f"words: {len(sentence_list)}")
    print(f"first word: {sentence_list[0]}")
    print(f"last word: {sentence_list[-1]}")

    shortest_word = sentence_list[0]
    longest_word = sentence_list[0]

    for word in sentence_list:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word
    print(f"shortest word: {shortest_word}")
    print(f"longest word : {longest_word}")
print("\n----------------------------------------")
"""
 Problem 5: Password strength classifier
 Description:
 Classify password as weak, medium, or strong based on documented rules.
 Suggested rules (documented in comments):
   - Weak: length < 8 OR only lower-case letters OR very simple (e.g., "password")
   - Medium: length >= 8 and (has letters and digits) but missing either symbols or mixed case
   - Strong: length >= 8 AND has upper, lower, digit, and symbol (non-alnum)
 Inputs:
   - password_input (string)
 Outputs:
   - "Password strength: weak/medium/strong"
 Validations:
   - Not empty
 Test cases:
   1) Normal: "Str0ng!Pass"
   2) Border: "Password1" (no symbol)
   3) Error: "" (empty)
 """

password = input("insert your password: ").strip()
if not password:
    print("error the password cannot be null")
else:
    len_password = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for i in password:
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True
        if i.isdigit():
            has_digit = True
        if not i.isalnum():
            has_symbol = True
    if len_password > 8 and has_upper and has_lower and has_symbol and has_digit:
        print(f"the password {password} is strong")
    elif len_password > 8 and (has_upper and has_lower) or (has_lower and has_digit) or (has_upper and has_digit) and not has_symbol:
        print(f"password {password} is medium")
    else:
        print(f"the password {password} is weak")
    
print("\n ---------------------------------")
"""
 Problem 6: Product label formatter (fixed-width text)
 Description:
 Given product_name and price_value produce a single-line label exactly 30 characters long.
 Format: Product: <NAME> | Price: $<PRICE>
 If shorter -> pad spaces to the right; If longer -> truncate to 30 chars.
 Inputs:
   - product_name (string)
   - price_value (string or number)
 Outputs:
   - "Label: '<30-char-text>'"
 Validations:
   - product_name not empty after strip()
   - price_value convertible to positive number
 Test cases:
   1) Normal: ("Notebook", 12.5)
   2) Border: (long name) -> truncation
   3) Error: ("   ", "abc")
 
 """

try : 
    name_product = input("product : ").strip()
    price_product = float(input("price : "))

    if not name_product:
        print("Error, name product cannot be null")
    else:
        name_product = str(name_product)
        label = f"Product: {name_product} | Price: ${price_product}"
        
        if len(label) > 30:
            label = label[:30]
        elif len(label) < 30:
            label = label + (" " * (30 - len(label)))
        print(f"label  {label}.")
except:
    print("Error, invalid price ")