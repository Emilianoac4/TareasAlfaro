# Errores Flake8

#Generado por Emiliano Alfaro Chacón

def string_work (nombre):
    if isinstance(nombre, str) == True:
        # isalpha detecta si el valor de nombre es un string
        if nombre.isalpha() == True:
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