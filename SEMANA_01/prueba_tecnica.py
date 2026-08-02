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
    if num > 0:
        return "positivo"
    elif num < 0:
        return "negativo"
    else:
        return "cero"
    
# 2. Par o impar
def even_odd(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"
    
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
    while True:
        try:
            id_code = int(input("\n\tIngrese su ID estudiantil: "))
            return id_code
        except ValueError:
            print("\n\tDebe ingresar un numero valido. Intente nuevamente.")

# Procesa fecha de nacimiento y código de estudiante
def process_birth_date_id(birth_date_id):
    # ejemplo "1enero2000100032300"
    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    for month in months:
        if month in birth_date_id.lower():
            month_found = month
            remnant = birth_date_id.lower().replace(month, "", 1)
            return month_found, remnant

    return None, None

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
        print("\t7. Volver al menú principal\n")
        
        option = input("\t\tSeleccione una opción: ")
        
        if option == "1":
            num = ask_integer_num()
            print(f"\n\tEl número {num} es {pos_neg_zero(num)}")

        elif option == "2":
            num = ask_integer_num()
            print(f"\tEl número {num} es {even_odd(num)}")

        elif option == "3":
            num = ask_integer_num("Ingrese un número entero: ")
            if fibonacci(num):
                print(f"\tEl número {num} SÍ pertenece a la secuencia Fibonacci")
            else:
                print(f"\tEl número {num} NO pertenece a la secuencia Fibonacci") 

        elif option == "4":
            num = ask_integer_num("Ingrese un número entero: ")
            if prime(num):
                print(f"\tEl número {num} SÍ es primo")
            else:
                print(f"\tEl número {num} NO es primo")

        elif option == "5":
            print("\n\tIngrese los límites del intervalo:")
            start = ask_integer_num("Límite inicial: ")
            end = ask_integer_num("Límite final: ")
            if abs(start - end) <= 1:
                print("\tNo hay números intermedios entre los límites ingresados")
            else:
                result = sum_lim(start, end)
                print(f"\tLa suma de los números entre {start} y {end} es: {result}")
                
        elif option == "6":
            num = ask_integer_num("Ingrese un número entero: ")
            result = elevate_cube_square(num)
            if num % 2 == 0:
                print(f"\t{num} es par, elevado al cubo: {num}³ = {result}")
            else:
                print(f"\t{num} es impar, elevado al cuadrado: {num}² = {result}")

        elif option == "7":
            break
        else:
            print("\n\t❌ Opción no válida, por favor ingrese una opcion del 1 al 7")

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
        print("\t7. Volver al menú principal\n")
        
        option = input("\n\t\tSeleccione una opción: ")
        if option == "6":
            birth_input = input("\nIngrese su fecha de nacimiento + codigo (ej: 1enero2000100032300): ")
            month, remnant = process_birth_date_id(birth_input)
            
            if month:
                print(f"\n\tMes encontrado: {month}")
                print(f"\tCodigo restante: {remnant}")
                
                # Vocales y consonantes
                vowels = "aeiou"
                consonants = "bcdfghjklmnpqrstvwxyz"
                vowels_found = []
                consonants_found = []
                
                for vow in month.lower():
                    if vow in vowels:
                        vowels_found.append(vow)
                    elif vow in consonants:
                        consonants_found.append(vow)
                
                print(f"\n\tVocales en '{month}': {', '.join(vowels_found) if vowels_found else 'ninguna'}")
                print(f"\tConsonantes en '{month}': {', '.join(consonants_found) if consonants_found else 'ninguna'}")
                
                # Posición en el abecedario
                print(f"\n\tPosicion en el abecedario:")
                for vow in month.lower():
                    if vow.isalpha():
                        position = ord(vow) - ord('a') + 1
                        print(f"    '{vow}' = posicion {position}")

                print(f"\n\tDesea realizar operaciones con el codigo restante?: {remnant}")
                continue_choice = input("\ty/n (yes/no): ").lower()
                if continue_choice == 'n':
                    print("\n\tRegresando al menú de estudiante...")
                    continue
                elif continue_choice == 'y':
                    print(f"\n\tProcesando el codigo restante: {remnant}")
                    try:
                        num = int(remnant)
                        print("\n\t--- Aplicando funciones al numero restante ---")
                        print(f"\tEl numero {num} es {pos_neg_zero(num)}")
                        print(f"\tEl numero {num} es {even_odd(num)}")
                                        
                        if fibonacci(num):
                            print(f"\tEl numero {num} SI pertenece a Fibonacci")
                        else:
                            print(f"\tEl numero {num} NO pertenece a Fibonacci")
                                            
                        if prime(num):
                            print(f"\tEl numero {num} SI es primo")
                        else:
                            print(f"\tEl numero {num} NO es primo")
                                            
                        result = elevate_cube_square(num)
                        if num % 2 == 0:
                            print(f"\t{num} es par, elevado al cubo: {num} = {result}")
                        else:
                            print(f"\t{num} es impar, elevado al cuadrado: {num} = {result}")
                                            
                    except ValueError:
                        print(f"\tEl codigo restante no es un numero valido para operaciones")
                else:
                    print(f"\n\tOpcion no valida, regresando al menu de estudiante")
            else:
                print(f"\n\tNo se encontro un mes valido en el formato ingresado")
      
        elif option == "7":
            break
            
        else:
            student_id_input = input("\n\tIngrese su codigo de estudiante: ")
            
            try:
                num = int(student_id_input)
                
                if option == "1":
                    print(f"\tEl codigo {num} es {pos_neg_zero(num)}")
                    
                elif option == "2":
                    print(f"\tEl codigo {num} es {even_odd(num)}")
                    
                elif option == "3":
                    if fibonacci(num):
                        print(f"\tEl codigo {num} SI pertenece a Fibonacci")
                    else:
                        print(f"\tEl codigo {num} NO pertenece a Fibonacci")
                        
                elif option == "4":
                    if prime(num):
                        print(f"\tEl codigo {num} SI es primo")
                    else:
                        print(f"\tEl codigo {num} NO es primo")
                        
                elif option == "5":
                    result = elevate_cube_square(num)
                    if num % 2 == 0:
                        print(f"\t{num} es par, elevado al cubo: {num} = {result}")
                    else:
                        print(f"\t{num} es impar, elevado al cuadrado: {num} = {result}")
                        
                else:
                    print("\n\tOpcion no valida")
                    
            except ValueError:
                print("\t\nEl codigo ingresado no es un numero valido")

# Menú principal
def main_menu():
    print ("\t\t-- OPERACIONES CON NÚMEROS O ID ESTUDIANTIL --")
    while True:
        print("\n\t\t\t=== MENÚ PRINCIPAL ===")
        print("\n\t1. Operaciones con números")
        print("\t2. Funciones con información del estudiante")
        print("\t3. Salir del programa")
        
        option = input("\n\t\tSeleccione una opción: ")
        
        if option == "1":
            numbers_menu()
        elif option == "2":
            student_menu()
        elif option == "3":
            print("\n\n\t\tHasta pronto!\n")
            break
        else:
            print("\n\t❌ Opción no válida, por favor ingrese una nuevamente.\n")

if __name__ == "__main__":
    main_menu()