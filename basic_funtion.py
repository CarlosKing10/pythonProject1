

def create_json_books():
    code = int(input("ingrese el codigo del libro: "))
    tittle = input("Titulo: ")
    name_autor = input("Nombre del autor: ")
    fecha_publicacion = input("Fecha de publicacion: ")
    editorial = input("Editorial: ")
    pages = input("N° de páginas: ")

    book = {
        "code": code,
        "tittle": tittle,
        "name_autor": name_autor,
        "Fecha_publicacion": fecha_publicacion,
        "editorial": editorial,
        "page": pages,
    }
    return book


def create_json_update_books():
    print("Menu de opciones ")
    print("1. Modificar todo el documento")
    print("2. Modificar solo un elemento del documento")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        tittle = input("Titulo: ")
        name_autor = input("Nombre del autor: ")
        Fecha_publicacion = input("Fecha de publicación: ")
        editorial = input("Editorial: ")
        pages = input("N° de páginas: ")

        book = {
            "tittle": tittle,
            "name_autor": name_autor,
            "Fecha_publicacion": Fecha_publicacion,
            "editorial": editorial,
            "page": pages,
        }
        return book
    elif opcion == "2":
        indice = input("Ingrese el valor de indice a modificar: ")
        valor = input("Ingrese el valor a modificar: ")
        book = {indice: valor}
        return book


def delete_json_books():
    print("Desea eliminar el registro?: 1.Si 2.No")
    opcion = input("Digite la opcion: ")









