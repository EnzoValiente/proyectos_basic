#Administrador de recetas
import os
from pathlib import Path

'''
bievenida al usuario // la ruta de acceso donde se encuentran las recetas // cuantas recetas hay en esa carpeta
elegir 1 opcion : 1: leer receta / 2: crear receta (crear categoria- nombre-contenido) / 3:crear categoria / 4: eliminar receta
5: eliminar categoria / finalizar el programa

'''

usuario = input('Coloque su nombre: ').title()
print(f'Bienvenido {usuario}')


opcion = {1:'Leer Receta', 2:'Crear Receta', 3:'Crear Categoria', 4:'Eliminar Receta', 5:'Eliminar Categoria', 6:'Salir'}
print(f'----------------Bienvenido al menu----------------')
mi_ruta = Path(Path.home(), 'Recetas')

def mostrar_carpetas(ruta):
    print('Categorias: ')
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for i in ruta_categorias.iterdir():
        carpeta_str = str(i.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(i)
        contador += 1
    return lista_categorias

def contar_recetas(ruta):
    contador = 0
    for i in Path(ruta).glob('**/*.txt'):
        contador += 1
    return contador

def mostrar_recetas(ruta):
    print('Recetas: ')
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for i in ruta_recetas.glob('*.txt'):
        receta_str = str(i.name)
        print(f'[{contador}] - {receta_str}')
        lista_recetas.append(i)
        contador += 1
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input(f'\nElige una receta: ')
    return lista[int(eleccion_receta) - 1]

def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('\nElige una categoria: ')
    return lista[int(eleccion_correcta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False

    while not existe:
        print('Escribe el nombre de tu receta: ')
        nombre_receta = input() + '.txt'
        print('Escribe tu nueva receta: ')
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada')
            existe = True
        else:
            print('Ya existe esa receta')

def crear_categoria(ruta):
    existe = False

    while not existe:
        print('Escribe el nombre de tu categoria: ')
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu nueva categoria {nombre_categoria} ha sido creada')
            existe = True
        else:
            print('Ya existe esa categoria')

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta.name} ha sido eliminada')

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoria {categoria.name} ha sido eliminada')

def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input('\nPresione V para volver al menu: ')


def opcion_elegida():
    bucle = False
    while bucle == False:
        claves = list(opcion.keys())
        print(f'1- Leer receta\n2- Crear receta\n3- Crear categoria\n4- Eliminar receta\n5- Eliminar categoria\n6- Salir')
        elegir_opcion = int(input(f'Elige la categoria {usuario}: '))
        if elegir_opcion == claves[0]:
            os.system('cls')
            print(f'Elegiste la opcion 1: Leer receta')
            mis_categorias = mostrar_carpetas(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            mis_recetas = mostrar_recetas(mi_categoria)
            if len(mis_recetas) < 1:
                print("no hay recetas en esta categoría.")
            else:
                mi_receta = elegir_recetas(mis_recetas)
                leer_receta(mi_receta)
            volver_inicio()
        if elegir_opcion == claves[1]:
            os.system('cls')
            print(f'Elegiste la opcion 2: Crear receta')
            mis_categorias = mostrar_carpetas(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            crear_receta(mi_categoria)
            volver_inicio()
        if elegir_opcion == claves[2]:
            os.system('cls')
            print(f'Elegiste la opcion 3: Crear categoria')
            crear_categoria(mi_ruta)
            volver_inicio()
        if elegir_opcion == claves[3]:
            os.system('cls')
            print(f'Elegiste la opcion 4: Eliminar receta')
            mis_categorias = mostrar_carpetas(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            mis_recetas = mostrar_recetas(mi_categoria)
            if len(mis_recetas) < 1:
                print("no hay recetas en esta categoría.")
            else:
                mi_receta = elegir_recetas(mis_recetas)
                eliminar_receta(mi_receta)
            volver_inicio()
        if elegir_opcion == claves[4]:
            os.system('cls')
            mis_categorias = mostrar_carpetas(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            eliminar_categoria(mi_categoria)
            print(f'Elegiste la opcion 5: Eliminar categoria')
            mostrar_carpetas(mi_ruta)
            volver_inicio()
        if elegir_opcion == claves[5]:
            os.system('cls')
            print(f'Elegiste la opcion 6: Salir del menu')
            break





opcion_elegida()









