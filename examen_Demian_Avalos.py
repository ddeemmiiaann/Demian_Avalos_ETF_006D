# La sala de cine CineMax requiere un programa en Python para administrar 
# su cartelera de películas y la disponibilidad de cupos por función. 
# Todo el comportamiento del sistema debe organizarse en funciones bien definidas. 
# El programa incluye un menú interactivo, 
# validaciones de entrada y una separación clara entre la lógica de cada función y las decisiones del programa principal.
# 1. Datos que debe manejar el sistema
# El sistema trabaja con dos diccionarios relacionados, 
# ambos identificados por el mismo código de película como clave. 
# Estos diccionarios deben existir desde que el programa inicia y permanecer disponibles durante toda la ejecución.

# titulo, genero, duración(minutos), clasificación, idioma, es 3D
import time
peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}

#precios(pesos), cupos 
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}
def cup_gen(genero):
    totalC=0
    genie=genero.lower()
    for key, value in peliculas.items():
        gen=value[1]
        if gen.lower()==genie:
            totalC=cartelera[key][1]
            print("Buscando")
            time.sleep(1)
            print("="*30)
            print(f"{value[0]} cupos disponibles {totalC}")
            print("="*30)
            time.sleep(1)
def busqueda_precio(P_min,P_max):
    peliculas_encontradas=[]
    if P_min>=0 and P_max>0:
        for ke, val in cartelera.items():
            nam=peliculas[ke][0]
            if P_min<=val[0]<=P_max:
                if cartelera[ke][1]!=0:
                    tex_l=f"{nam}--{ke}"
                    peliculas_encontradas.append(tex_l)
    peliculas_encontradas.sort()
    time.sleep(1)
    print("======PELICULAS ENCONTRADAS======")
    for i in peliculas_encontradas:
        print(i)
    print("="*33)
    time.sleep(1)
def actualizar_precio(codigo, precio_nuevo):
    if codigo in peliculas:
        cartelera[codigo][0]=precio_nuevo
        return True
    else:
        return False
def val_txt(txt):
    if len(txt)>0:
        return True
    else:
        return False
def val_clas(clas):
    clasi=["A","B","C"]
    clasif=clas.upper()
    if clasif in clasi:
        return True
    else:
        return False
def agregar_pelicula(cod, tit, gen, dur,clas, idi, dim, pre, cup):
    peliculas[cod]=[tit,gen,dur,clas,idi,dim]
    cartelera[cod]=[pre,cup]
def val_dimen(dim):
    if dim.lower()=="s":
        return True
    else:
        return False
def eliminar_pelicula(pel):
    if pel in peliculas:
        del peliculas[pel]
        del cartelera[pel]
        return True
    else:
        return False





def menuP():
    print("========== MENÚ PRINCIPAL ==========\n"
    "1. Cupos por género\n"
    "2. Búsqueda de películas por rango de precio\n"
    "3. Actualizar precio de película\n"
    "4. Agregar película\n"
    "5. Eliminar película\n"
    "6. Salir\n"
    "=====================================")
def manu():
    while True:
        try:
            menuP()
            op=int(input("Que le gustaria hacer?\n"))
            match op:
                case 1:
                    genero=input("Que genero está buscando?\n")
                    cup_gen(genero)
                case 2:
                    while True:
                        try:
                            p_min=int(input("Cual es el precio minimo que busca?\n"))
                            p_max=int(input("Cual es el precio maximo que busca?\n"))
                            if p_min>=0 and p_max>0:
                                busqueda_precio(p_min,p_max)
                                break
                            else:
                                print("Los valores de precio deben ser mayor a 0")
                            
                        except ValueError:
                            print("El precio debe ser un numero entero")
                case 3:
                    while True:
                        try:
                            code=input("Cual es el codigo de la pelicula que desea actualizar?\n").strip().upper()
                            pres=int(input("Cual sera el nuevo precio de la pelicula?\n"))
                            if pres>0:
                                check=actualizar_precio(code, pres)
                                if check==True:
                                    print("El precio fue actualizado correctamente")
                                else:
                                    print("El codigo de pelicula no coincide con algun codigo en nuestro sistema")
                            else:
                                print("El precio debe ser un numero mayor a 0")
                            seguir=input("Desea seguir actualizar otro precio? (s/n)\n")
                            if seguir!="s":
                                break
                        except ValueError:
                            print("El precio de la pelicula debe ser un numero entero positivo")
                case 4:
                    cod=input("Cual es el codigo de pelicula que quiere agregar?\n").strip().capitalize()
                    if not val_txt(cod):
                        print("El cofigo no puede estar vacio")
                        continue
                    if cod in peliculas:
                        print("El codigo ya se encuentra en existencia")
                        continue
                    tit=input("Cual es el titulo de la pelicula?\n").strip().capitalize()
                    if not val_txt(tit):
                        print("El titulo de la pelicula no puede estar vacio")
                        continue
                    gen=input("Cual es el genero de la pelicula?\n").strip().capitalize()
                    if not val_txt(gen):
                        print("El genero no puede estar vacio")
                        continue
                    try:
                        dur=int(input("Cual es la duración de la pelicula?\n"))
                        if dur<=0:
                            print("La pelicula debe durar más de 0 minutos")
                            continue
                    except ValueError:
                        print("La duración de la pelicula debe ser un numero entero")
                        continue
                    clas=input("Cual es la clasificación de la pelicula? (A,B,C)\n")
                    if not val_clas(clas):
                        print("La clasificación debe ser A, B o C")
                        continue
                    idi=input("Cual es el idioma de la pelicula?\n").strip().capitalize()
                    if not val_txt(idi):
                        print("El idioma no puede estar vacio")
                        continue
                    dim=input("La pelicula tiene 3D? (s/n)\n")
                    if not val_txt(dim):
                        print("El campo no puede esta vacio")
                        continue
                    val_dimen(dim)
                    try:
                        pre=int(input("Cual es el precio de la pelicula?\n"))
                        if pre<=0:
                            print("El precio debe ser mayor o igual a 0")
                            continue
                    except ValueError:
                        print("El precio debe ser un numero entero mayor a 0")
                        continue
                    try:
                        cup=int(input("Cuantos cupos tiene la pelicula?\n"))
                        if cup<0:
                            print("No puede haber menos de 0 cupos")
                            continue
                    except ValueError:
                        print("Los cupos deben ser un numero entero mayor o igual a 0")
                        continue
                    agregar_pelicula(cod, tit, gen, dur, clas, idi, dim, pre, cup)
                    print("Pelicula agregada correctamente")
                case 5:
                    el=input("Cual es el codigo de la pelicula que desea eliminar?\n").upper()
                    comprovacion=eliminar_pelicula(el)
                    if comprovacion==True:
                        print("Pelicula eliminada correctamente")
                    else: 
                        print("EL codigo no existe en nuestro sistema")
                    
                case 6:
                    print("Programa Finalizado")
                    break
                case _:
                    print("ERROR: Escoja una de las opciones en pantalla")
        except Exception as e:
            print(f"ERROR: Escoja una de las opciones en pantalla {e}")

manu()




