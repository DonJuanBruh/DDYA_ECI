''' Functions '''

# Pide numero entero
def ask_integer_num(message="Ingrese un número entero:"):
        while True:
            try:
                num = int(input(message))
                return num
            except ValueError:
                print("❌ Debe ingresar un número entero válido. Intente nuevamente.")

# 1. Positivo, negativo o cero
def pos_neg_zero(num):
    zero = "cero"
    positive = "positivo"
    negative = "negativo"
    if num > 0:
        return positive
    elif num < 0:
        return negative
    else:
        return zero
    
# 2. Par o impar
def even_odd(num):
    even = "par"
    odd = "impar"
    if num % 2 == 0:
        return even
    else:
        return odd
    
# 3. Hace parte de la secuencia de fibonacci
def fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0
    
# 4. Número primo
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 5. Suma intermedios de un intervalo
def sum_lim(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start + 1, end))

# 5. Elevar si es par al cubo o si es impar al cuadrado
def elevate_cube_square(num):
    if num % 2 == 0:
        return num ** 3
    else:
        return num ** 2

# Pide id estudiantil
def ask_IDcode():
    id = int(input("\t Ingrese su ID estudiantil:"))
    return id

# Menú de operaciones con números
def numbers_menu():
    while True:
        print("\n\t\t=== OPERACIONES CON NÚMEROS SIMPLES ===")
        print("\n\t1. Verificar si es positivo, negativo o cero")
        print("\t2. Verificar si es par o impar")
        print("\t3. Verificar si pertenece a Fibonacci")
        print("\t4. Verificar si es primo")
        print("\t5. Sumar números entre dos valores (límites)")
        print("\t6. Elevar al cuadrado (si es impar) o cubo (si es par)")
        print("\t7. Volver al menú principal")
        
        option = input("Seleccione una opción: ")
        
        if option == "1":
            num = ask_integer_num()
            print(f"El número {num} es {pos_neg_zero(num)}")
        elif option == "2":
            num = ask_integer_num()
            print(f"El número {num} es {even_odd(num)}")

        elif option == "7":
            break
        else:
            print("Opción no válida")

# Menú funciones para estudiante
def student_menu():
    while True:
        print("\n\t\t=== OPERACIONES CON CÓDIGO DE ESTUDIANTE ===")
        print("\n\t1. Verificar si es positivo, negativo o cero")
        print("\t2. Verificar si es par o impar")
        print("\t3. Verificar si pertenece a Fibonacci")
        print("\t4. Verificar si es primo")
        print("\t5. Elevar al cuadrado (si es impar) o cubo (si es par)")
        print("\t6. Procesar con fecha de nacimiento")
        print("\t7. Volver al menú principal")
        
        option = input("\n\t\tSeleccione una opción: ")
        student_id = input("\n\t\tIngrese su código de estudiante: ")

# Menú principal
def main_menu():
    print ("\t\t-- OPERACIONES CON NÚMEROS O ID ESTUDIANTIL --")
    while True:
        print("\n\t\t\t=== MENÚ PRINCIPAL ===")
        print("\n\t1. Operaciones con números")
        print("\t2. Funciones con información del estudiante")
        print("\t3. Apagar el programa")
        
        option = input("\n\t\tSeleccione una opción: ")
        
        if option == "1":
            numbers_menu()
        elif option == "2":
            student_menu()
        elif option == "3":
            print("\n\n\t\tHasta pronto!\n")
            break
        else:
            print("\n\tOpción no válida, por favor ingrese una nuevamente.\n")
    main_menu()