from crud import *
from basic_funtion import *


while True:
    print("Menu de opciones")
    print("1. Ver todos los libros")
    print("2. Buscar un libro por titulo")
    print("3. Agregar un libro")
    print("4. Modificar Registro")
    print("5. Eliminar un registro")
    print("6. Salir de sistema")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        read_books()
    elif opcion == "2":
        tittle = input("Ingrese el titulo del libro  a buscar: ")
        read_books(tittle)
    elif opcion == "3":
        book = create_json_books()
        create_books(book)
    elif opcion == "4":
        code = input("Ingrese el código del libro a modificar: ")
        book = create_json_update_books()
        update_books(code, book)
    elif opcion == "5":
        code = int(input("Ingrese el id del libro a Eliminar: "))
        book = delete_json_books()
        delete_books(book)
    elif opcion == "6":
        print("Saliendo del sistema")
        break
