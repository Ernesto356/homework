"""
PORTADA
Nombre: Jesus Ernesto Sanchez Luevano
Matrícula: 2530192
Grupo: 1-1 IM

"""
"""

 RESUMEN EJECUTIVO
================================================================
Este programa implementa un CRUD (Create, Read, Update, Delete),
es decir, un sistema que permite crear, leer, actualizar y eliminar
elementos en memoria. Se utiliza un diccionario donde cada clave es
el ID del ítem y el valor es otro dict con name, price y quantity.
Se eligió diccionario porque permite accesos más rápidos por ID.
Cada operación está implementada como una función, lo cual mejora
la organización y la claridad del código.
El programa incluye un menú principal y funciones para crear,
leer, actualizar, eliminar y listar ítems.
"""

"""

 PROBLEM: In-memory CRUD manager with functions
================================================================
Descripción:
Programa que implementa un CRUD simple de ítems usando un diccionario
en memoria. Los ítems contienen id, name, price y quantity. El usuario
interactúa mediante un menú textual.
Inputs:
- Opción de menú.
- Para CREATE/UPDATE: item_id, name, price, quantity.
- Para READ/DELETE: item_id.
Outputs:
- Mensajes como: "Item created", "Item updated",
  "Item deleted", "Item not found", "Items list:", etc.
Validations:
- option válida (0–5)
- item_id no vacío
- price y quantity deben ser números válidos >= 0
- No permitir crear un ID duplicado
- En read/update/delete: si id no existe → "Item not found"
Test cases:
1) Normal:
   create -> read -> update -> delete → mensajes correctos.
2) Border:
   Crear con quantity = 0 o price = 0.0 → válido.
3) Error:
   option inválida, price no numérico, id vacío → "Error: invalid input"
================================================================
 DIAGRAMAS / TABLAS
================================================================
Diagrama de flujo (descripción):
- Usuario selecciona opción → validación → llama función CRUD →
  imprime resultado → regresa al menú.
Tabla de casos de prueba (descripción):
Caso | Entrada | Resultado esperado
Normal | Crear/leer/actualizar/eliminar | Mensajes correctos
Borde | quantity=0 | Aceptado
Error | price="abc" | Error: invalid input
================================================================"""

items = {}
 #Use la Estructura A, un diccionario cuya llave es el ID y cuyo valor es un dict con los atributos del ítem.
# Lo use porque se me hice mas facil (Bajo mi propia experiencia)
def create_item(data, id_item, name, price, quantity):

    if id_item in data:
        return False
    
    data[id_item] ={
        "name": name,
        "price" : price,
        "quantity":quantity
    }
    return True

def readItem(data, id_item):
    return data.get(id_item)

def itemUpdate(data, id_item, name, price,quantity):
    if id_item not in data:
        return False

    if name is not None:
        data[id_item]["name"] = name

    if price is not None:
        data[id_item]["price"] = price

    if quantity is not None:
        data[id_item]["quantity"] = quantity
    return True

def delete(data, id_item):
    if id_item in data:
        del data[id_item]
        return True
    
    return False

def list_items(data):
    if not data:
        print("Item List (empty)")
        return
    
    print("Item list")
    for item_id, info in data.items():
        print(f"""
    ID : {item_id} 
    NAME: {info["name"]}
    PRICE: {info["price"]}
    QUANTITY: {info["quantity"]}
    \n
""")

def main():
    while True:
        print("Options : \
            1) Create Item\
            2) Read Item by ID\
            3) Update Item by ID\
            4) Delete Item by ID\
            5) Lis All Items\
            0) Exit \n")
        option = input("Inser A Option: ").strip()
        if option not in {"1","2","3","4","5","0"}:
            print("Error -> Invalid Input")
            continue
        
        if option == "0":
            print("Good Bye")
            exit()

        if option == "1":
            print("\n--Create Item --\n")
            id_item = input("Insert the ID item :").strip()
            if not id_item :
                print("Error Invalid Input:")
                continue
            
            try:
                name = input("Insert Name : ").strip()
                price = float(input("Insert the price: "))
                quantity = int(input("Insert the quantity : "))

                if price < 0.0 or quantity < 0 or name == "":
                    print("Error the price o quantity cannot be null")
                    continue
                create = create_item(items,id_item,name,price,quantity)
                if create:
                    print("\nThe Item has been Created")
                else: 
                    print("\n Error: id already exists")
                
            except Exception as erro:
                print(f"Error Invalid Input: {erro}")
            
        elif option == "2":
            print("\n--Read Item--\n")
            id_item = input("Insert the Item :" ).strip()
            if not  id_item:
                print("Error Invalid Input")
                continue
            result = readItem(items,id_item)
            if result is None:
                print("Data not found")
            else:
                print(f"Data found : {result}")
        
        elif option == "3":
            print("\n--UPDATE--\n")
            id_item = input("Insert the ID to Update: ").strip()
            if not id_item:
                print("Erro Invalid value")
                continue

            try:
                new_name = input("Insert the new name: ")
                new_price = float(input("Insert the new price: "))
                new_quantity = int(input("Insert the new quantity: "))

                if(new_price < 0 or new_quantity < 0):
                    print("The values cannot by null")
                    continue

                update = itemUpdate(items,id_item,new_name,new_price,new_quantity)
                if update:
                    print("\n---Update---")
                else:
                    print("update failed")
            except Exception as erro:
                print(f"\n Error Invalid Input: {erro}")
            
        elif option == "4":
            print("\n--Delete--\n")
            id_item = input("Insert the Id to Delete: ")
            if not id_item:
                print("Erro invalid Input: ")
                continue
            result = delete(items, id_item)
            if result :
                print("the item was successfully deleted ")
            else:
                print("Item Not Found")
        
        elif option == "5":
            print("\n--Read All Items--\n")
            list_items(items)
            


if __name__ == "__main__":
    main() 
"""
================================================================
 CONCLUSIONES
================================================================
- Un CRUD permite administrar datos mediante operaciones básicas.
- Separar las funciones facilita el mantenimiento del código.
- El uso de diccionarios permite accesos rápidos por ID.
- El menú permite interacción sencilla y controlada con el usuario.
- La validación evita errores comunes y asegura la integridad de datos.

================================================================
 REFERENCIAS
================================================================
1. Python Official Documentation: https://docs.python.org/
2. Real Python – Dictionaries: https://realpython.com/python-dicts/
3. W3Schools Python Tutorial: https://www.w3schools.com/python/
================================================================"""

"""
Url del repositorio de github:
https://github.com/Ernesto356/homework.git
"""