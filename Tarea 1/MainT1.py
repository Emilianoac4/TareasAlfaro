# Generado por Emiliano Alfaro Chacón
# Fecha de inicio 16/02/2022
# Fecha de finalización
# Versión 3.10.2

# string_work, detecta si el valor de entrada es un string
# devolviendolo con mayúsculas y minúsculas invertidas
def string_work(nombre):
    if isinstance(nombre, str) is True:
        # isalpha detecta si el valor de nombre es un string
        if nombre.isalpha() is True:
            # Inversión de mayúsculas y minúsculas
            inversion = nombre.swapcase()
            print(f"Nombre invertido: {inversion}")
            return(inversion)  # Retorno de la inversión

        else:
            print("Entrada desconocida N°Error 1")
            # N°Error 1 se muestra si la entrada posee caracteres inválidos
            return("N°Error 1")
    else:
        print("N°Error 3")
        return("N°Error 3")

# num_to_str, detecta si el valor de entrada es
# numérico retornando dicho valor en prosa.


def num_to_str(nombre):
    if isinstance(nombre, int) is True or isinstance(nombre, float) is True:
        # Verifica que el valor se encuentre entre 0 y 99:
        if nombre in range(0, 99):

            # Lista de nombres de números:
            list = ["Cero", "Uno", "Dos", "Tres", "Cuatro",
                    "Cinco", "Seis", "Siete", "Ocho", "Nueve"]
            # Lista de nombres de excepciones:
            list_deci = ["Diez", "Once", "Doce", "Trece",
                         "Catorce", "Quince", "Veinte"]
            # Lista de nombres de decenas:
            list_decenas = ["0", "Dieci", "Veinti", "Treinta", "Cuarenta",
                            "Cincuenta", "Sesenta",
                            "Setenta", "Ochenta", "Noventa"]
            # Lista de salida final unidades:
            list_final = []
            # Lista de salida final de decenas:
            list_f_decenas = []
            # Lista de números para realizar una comparación
            comparacion = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

            # Toma la entrada nombre e introduce sus caracteres en una lista:
            lista_nombre = [int(a) for a in str(nombre)]

            # Si se introduce un número de un digito
            # introduce un 0 en la primera posición de la lista
            if int(len(lista_nombre)) == 1:
                lista_nombre.insert(0, 0)

            # Ciclo determinado por el largo de nombre
            for n in range(0, len(lista_nombre)):
                # Ciclo que recorre 10 diferentes posiciones:
                for y in range(0, 10):
                    # Compara las posiciones de las diferentes listas
                    if lista_nombre[n] == comparacion[y]:
                        # Introduce el valor dado por
                        # la posición n de list_final:
                        list_final.append(list[y])
                        # Introduce el valor dado por
                        # la posición y en list_f_decenas:
                        list_f_decenas.append(list_decenas[y])
            # Caso excepción valor 0
            if list_f_decenas[0] == "0":
                return(list_final[1])
            # Caso excepción valor 10
            elif list_f_decenas[0] == "Dieci" and list_final[1] == "Cero":
                return(list_deci[0])
            # Caso excepción valor 11
            elif list_f_decenas[0] == "Dieci" and list_final[1] == "Uno":
                return(list_deci[1])
            # Caso excepción valor 12
            elif list_f_decenas[0] == "Dieci" and list_final[1] == "Dos":
                return(list_deci[2])
            # Caso excepción valor 13
            elif list_f_decenas[0] == "Dieci" and list_final[1] == "Tres":
                return(list_deci[3])
            # Caso excepción valor 14
            elif list_f_decenas[0] == "Dieci" and list_final[1] == "Cuatro":
                return(list_deci[4])
            # Caso excepción valor 15
            elif list_f_decenas[0] == "Dieci" and list_final[1] == "Cinco":
                return(list_deci[5])
            # Caso excepción valor 20
            elif list_f_decenas[0] == "Veinti" and list_final[1] == "Cero":
                return(list_deci[6])
            # Caso excepción valor 30
            elif list_f_decenas[0] == "Treinta" and list_final[1] == "Cero":
                return(list_decenas[3])
            # Caso excepción valor 40
            elif list_f_decenas[0] == "Cuarenta" and list_final[1] == "Cero":
                return(list_decenas[4])
            # Caso excepción valor 50
            elif list_f_decenas[0] == "Cincuenta" and list_final[1] == "Cero":
                return(list_decenas[5])
            # Caso excepción valor 60
            elif list_f_decenas[0] == "Sesenta" and list_final[1] == "Cero":
                return(list_decenas[6])
            # Caso excepción valor 70
            elif list_f_decenas[0] == "Setenta" and list_final[1] == "Cero":
                return(list_decenas[7])
            # Caso excepción valor 80
            elif list_f_decenas[0] == "Ochenta" and list_final[1] == "Cero":
                return(list_decenas[8])
            # Caso excepción valor 90
            elif list_f_decenas[0] == "Noventa" and list_final[1] == "Cero":
                return(list_decenas[9])

            else:
                # Retorno del nombre de todos los casos generales
                return(list_f_decenas[0]+"_y_"+list_final[1])

        else:
            # N°2Error 2 determina si el número no se encuentra entre 0 y 99
            print("Entrada desconocida N°Error 2")
            return("N°Error 4")
    else:

        return("N°Error 2")
