from MainT1 import string_work
from MainT1 import num_to_str


# Testeo de inversión entre mayúsculas y minúsculas
def test_string_work():
    # Contiene minúsculas
    input = "abcdefghijklmnopqrstuvwxyz"
    # Contiene mayúsculas
    output = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Recorre en razón a la cantidad de letras
    for x in range(26):
        # Compara si el valor retornado corresponde con el valor en output
        assert string_work(input[x]) == output[x]


# Testeo de número en el valor ingresado
def test_string_work_numero():
    input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(10):
        # Verifica si lo retornado corresponde con el error esperado.
        assert string_work(input[x]) == "N°Error 3"


# Testeo de Strings con números y símbolos
def test_string_work_simb():
    simbol = ["ABC12", "ABC!", "ABC1!"]
    for x in range(3):
        # Verifica si lo retornado corresponde con el error esperado.
        assert string_work(simbol[x]) == "N°Error 1"


# Testeo de retorno de nombres
def test_num():
    # Lista con nombres de números
    list = [
        'Cero', 'Uno', 'Dos', 'Tres',
        'Cuatro', 'Cinco', 'Seis', 'Siete',
        'Ocho', 'Nueve', 'Diez', 'Once',
        'Doce', 'Trece', "Catorce", 'Quince',
        'Dieci_y_Seis', 'Dieci_y_Siete', 'Dieci_y_Ocho', 'Dieci_y_Nueve',
        'Veinte', 'Veinti_y_Uno', 'Veinti_y_Dos', 'Veinti_y_Tres',
        'Veinti_y_Cuatro', 'Veinti_y_Cinco', 'Veinti_y_Seis', 'Veinti_y_Siete',
        'Veinti_y_Ocho', 'Veinti_y_Nueve', 'Treinta', 'Treinta_y_Uno',
        'Treinta_y_Dos', 'Treinta_y_Tres', 'Treinta_y_Cuatro',
        'Treinta_y_Cinco',
        'Treinta_y_Seis', 'Treinta_y_Siete', 'Treinta_y_Ocho',
        'Treinta_y_Nueve',
        'Cuarenta', 'Cuarenta_y_Uno', 'Cuarenta_y_Dos', 'Cuarenta_y_Tres',
        'Cuarenta_y_Cuatro', 'Cuarenta_y_Cinco', 'Cuarenta_y_Seis',
        'Cuarenta_y_Siete',
        'Cuarenta_y_Ocho', 'Cuarenta_y_Nueve', 'Cincuenta', 'Cincuenta_y_Uno',
        'Cincuenta_y_Dos', 'Cincuenta_y_Tres', 'Cincuenta_y_Cuatro',
        'Cincuenta_y_Cinco',
        'Cincuenta_y_Seis', 'Cincuenta_y_Siete', 'Cincuenta_y_Ocho',
        'Cincuenta_y_Nueve',
        'Sesenta', 'Sesenta_y_Uno', 'Sesenta_y_Dos', 'Sesenta_y_Tres',
        'Sesenta_y_Cuatro', 'Sesenta_y_Cinco', 'Sesenta_y_Seis',
        'Sesenta_y_Siete',
        'Sesenta_y_Ocho', 'Sesenta_y_Nueve', 'Setenta', 'Setenta_y_Uno',
        'Setenta_y_Dos', 'Setenta_y_Tres', 'Setenta_y_Cuatro',
        'Setenta_y_Cinco',
        'Setenta_y_Seis', 'Setenta_y_Siete', 'Setenta_y_Ocho',
        'Setenta_y_Nueve',
        'Ochenta', 'Ochenta_y_Uno', 'Ochenta_y_Dos', 'Ochenta_y_Tres',
        'Ochenta_y_Cuatro', 'Ochenta_y_Cinco', 'Ochenta_y_Seis',
        'Ochenta_y_Siete',
        'Ochenta_y_Ocho', 'Ochenta_y_Nueve', 'Noventa', 'Noventa_y_Uno',
        'Noventa_y_Dos', 'Noventa_y_Tres', 'Noventa_y_Cuatro',
        'Noventa_y_Cinco',
        'Noventa_y_Seis', 'Noventa_y_Siete', 'Noventa_y_Ocho',
        'Noventa_y_Nueve']
    # Recorre la totalidad de la lista
    for n in range(99):
        input_string = (n)
        # Compara si el valor númerico dado retorna el número esperado
        assert num_to_str(input_string) == list[n]


# Verifica que al ingresar un string se retorne el error esperado
def test_num_error():

    input_string = "abcdefghijklmnopqrstuvwxyz"

    for x in range(26):
        # Verifica si lo retornado corresponde con el error esperado.
        assert num_to_str(input_string[x]) == "N°Error 2"


# Verifica que al ingresar valores flotantes,
# que excedan el rango o negativos se genere el error esperado.
def test_num_rango():

    input = [1.1, 100, -1]

    for x in range(3):
        # Verifica si lo retornado corresponde con el error esperado.
        assert num_to_str(input[x]) == "N°Error 4"
