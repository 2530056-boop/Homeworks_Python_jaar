# --------------------------------------------------
# Cover page
# Name: jesus Adrian Ramos Rodriguez
# Matricula: 2530056
# --------------------------------------------------

# --------------------------------------------------
# RESUMEN EJECUTIVO
# --------------------------------------------------

# 1. ¿Qué es un string?
# Un string (cadena de texto) en Python es un tipo de dato inmutable, lo que significa
# que no puede modificarse una vez creado; las operaciones generan una nueva cadena.

# 2. Operaciones básicas:
# Se pueden realizar operaciones esenciales como concatenación (+), obtener su longitud (len()),
# extraer sub-cadenas (slicing []), buscar patrones o sub-cadenas, y reemplazar texto específico.

# 3. Importancia de la validación/normalización:
# Es crucial validar y normalizar el texto de entrada (correos, nombres, contraseñas) para
# asegurar la integridad de los datos, prevenir errores de formato, y mejorar la seguridad
# (ej. verificar la estructura de un correo o la longitud de una contraseña).

# 4. Contenido del documento:
# Este documento cubre la descripción de problemas, el diseño de entradas y salidas esperadas,
# las validaciones aplicadas a los datos, y el uso práctico de métodos de string de Python
# (ej. .lower(), .strip(), .split(), .find()) con casos de prueba y su código fuente.

# --------------------------------------------------
# --------------------------------------------------
# 5. PRINCIPIOS Y BUENAS PRÁCTICAS CON STRINGS EN PYTHON
# --------------------------------------------------

# 1. Inmutabilidad:
# Los strings son inmutables. Recuerda que cualquier método o modificación (ej. .replace())
# no altera la cadena original, sino que siempre devuelve una *nueva* cadena de texto.

# 2. Normalización de Entrada:
# Es una buena práctica de programación normalizar el texto de entrada. Usar .strip()
# (para eliminar espacios al inicio/final) y .lower() (para minúsculas) antes de
# cualquier comparación es clave para evitar errores de coincidencia.

# 3. Índices y Slicing:
# Evita los "números mágicos" en los índices o el slicing (ej. [0:5]). Siempre documenta
# con comentarios qué representa el índice o la sub-cadena que estás extrayendo.

# 4. Usar Métodos Incorporados:
# Aprovecha los métodos nativos de string de Python (.split(), .find(), .join(), .isdigit(), etc.)
# en lugar de reescribir lógica básica. Esto hace el código más eficiente y legible.

# 5. Diseño de Validaciones:
# Diseña las validaciones de manera clara y secuencial:
# a) Primero: Comprueba que el string no esté vacío (len() > 0 o simplemente 'if mi_string:').
# b) Segundo: Verifica el formato específico (ej. uso de '@' en correos).

# 6. Legibilidad y Mantenimiento:
# Utiliza nombres de variables claros (ej. 'nombre_usuario' en lugar de 'n') y asegúrate
# de que los mensajes de error sean descriptivos y comprensibles para el usuario.
# --------------------------------------------------
# Problem 1: Full name formatter (name + initials)
# Description:
# Given a full name in a single string, normalize spacing and case,
# return the name in Title Case and the initials (e.g. "J.C.T.").
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - prints "Formatted name: <Name In Title Case>"
# - prints "Initials: <X.X.X.>"
#
# Validations:
# - Not empty after strip()
# - Must contain at least two words
#

#7.1 Problem 1: Full name formatter (name + initials)

print ("\nWelcome to full name formatter  ")
full_name= input ("\n Please provide your full name: ").strip().lower()
words= full_name.split()
if full_name == ""or len(words)<2:
    print("Error, you must enter your full name")
else:
    print("great now here¨s your formatted name ")
    initials=""
    for w in words:
        initials += w[0].upper()+"."
    print(initials)
    
# --------------------------------------------------
# 6. CASOS DE PRUEBA (TEST CASES)
# --------------------------------------------------

# El siguiente código procesa el nombre completo del usuario, verifica que haya al menos dos
# palabras y luego genera las iniciales en mayúsculas separadas por puntos.

# | Categoría | Escenario | Entrada (full_name) | Salida Esperada | Razón/Verificación |
# | :--- | :--- | :--- | :--- | :--- |
# | 1. Normal | Básico (Dos palabras) | juan perez | J.P. | Funcionamiento estándar; genera iniciales. |
# | 1. Normal | Nombre compuesto | Ana Maria Lopez | A.M.L. | Maneja más de dos palabras. |
# | 1. Normal | Mayúsculas/Minúsculas | PEDRO picapiedra | P.P. | Confirma normalización por .lower() y .upper(). |
# | 1. Normal | Espacios extra |      luis gomez    | L.G. | Confirma la limpieza de espacios por .strip(). |
# | 2. Frontera | Mínimo de palabras | uno dos | U.D. | Prueba el límite de la condición (len(words) >= 2). |
# | 2. Frontera | Palabras de 1 char | a b c | A.B.C. | Confirma que funciona al tomar el índice w[0]. |
# | 2. Frontera | Caracteres No-ASCII | ñoñito álvarez | Ñ.Á. | Confirma el manejo de letras especiales/acentuadas. |
# | 3. Error | Cadena vacía | (Enter) | Error, you must enter... | Prueba la condición full_name == "". |
# | 3. Error | Solo espacios | "      " | Error, you must enter... | Prueba el resultado de .strip() que deja la cadena vacía. |
# | 3. Error | Una sola palabra | Ricardo | Error, you must enter... | Prueba la condición len(words) < 2. |

# --------------------------------------------------

# --------------------------------------------------
# Problem 2: Simple email validator (structure + domain)
# Description:
# Validate a basic email structure: exactly one '@', at least one '.' after '@',
# and no spaces.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - prints "Valid email: true" or "Valid email: false"
# - if valid, prints "Domain: <domain_part>"
#
# Validations:
# - Not empty after strip()
# - '@' appears exactly once
# - No spaces present
#
# Test cases:
# | Categoría | Escenario | Entrada (email_text) | Salida Esperada | Razón/Verificación |
# | :--- | :--- | :--- | :--- | :--- |
# | 1. Normal | Email estándar | user@example.com | true, domain "example.com" | Contiene 1 @ y un punto después. |
# | 1. Normal | Email con subdominio | user.name@sub.domain.co | true, domain "sub.domain.co" | Maneja múltiples puntos tras el @. |
# | 2. Frontera | Sin espacios | user123@correo.mx | true | Verifica ausencia de espacios. |
# | 2. Frontera | Punto casi al final | test@domain.com | true | Cumple estructura mínima del dominio. |
# | 3. Error | Doble @ | user@@example.com | false | Violación: más de un @. |
# | 3. Error | Espacios incluidos | " user@ex .com " | false | strip limpia, pero quedan espacios internos. |
# | 3. Error | Cadena vacía | (Enter) | false | Falla validación de vacío. |

# --------------------------------------------------
# 7.2 Problem 2: Simple email validator (structure + domain)
# --------------------------------------------------

# Mensaje de bienvenida para el usuario
print("\nwelcome to simple email validator")

# Inicia un ciclo infinito hasta que el usuario dé un email válido
while True:

    # Solicita email y elimina espacios al inicio y final
    email_text = input("\nplease give your email: ").strip()

    # Validación 1: verificar si el email está vacío
    if email_text == "":
        print("invalid email try again")

    # Validación 2: email válido si:
    # - Tiene exactamente un '@'
    # - Contiene ".com" (aunque esta condición está escrita incorrectamente en tu código original)
    if email_text.count("@") == 1 and "." "com" in email_text:
        print("\nValid email")   # Mensaje de éxito
        break                    # Rompe el ciclo cuando el email es válido

    # Validación repetida: vuelve a indicar que está vacío
    if email_text == "":
        print("invalid email try again.")




# --------------------------------------------------
# Problem 3: Palindrome checker (ignoring spaces and case)
# Description:
# Determine if a phrase is a palindrome ignoring spaces and case.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - prints "Is palindrome: true" or "Is palindrome: false"
# - optional: prints normalized phrase
#
# Validations:
# - Not empty after strip()
# - Normalized length at least 3 characters
#
# Test cases:
# | Categoría | Escenario | Entrada (phrase) | Salida Esperada | Razón/Verificación |
# | :--- | :--- | :--- | :--- | :--- |
# | 1. Normal | Palíndromo clásico | Anita lava la tina | true | Ignora espacios y mayúsculas. |
# | 1. Normal | Palíndromo simple | aba | true | Longitud mínima válida. |
# | 2. Frontera | Palabra con espacios extremos | "  oso  " | true | strip elimina espacios laterales. |
# | 2. Frontera | Frase con mayúsculas | "NeuQ" | false | Se normaliza y compara reversed. |
# | 3. Error | Solo espacios | "    " | invalid | strip deja cadena vacía. |
# | 3. Error | Muy corta | " a " | invalid | Normalizada queda con menos de 3 chars. |
# | 3. Error | Cadena vacía | "" | invalid | No cumple validación inicial. |

# --------------------------------------------------
# 7.3 Problem 3: Palindrome checker (ignoring spaces and case)
# --------------------------------------------------

# Ciclo que se repite hasta que el usuario escriba un palíndromo válido
while True:

    # Solicita una frase y elimina espacios al inicio y final
    phrase = input("Write a phrase: ").strip()

    # Validación 1: la cadena no debe estar vacía
    if phrase == "":
        print("Is palindrome: false")

    else:
        # Normalización:
        # - Convertir todo a minúsculas
        # - Quitar todos los espacios internos
        normalized = phrase.lower().replace(" ", "")

        # Validación 2: asegurar que la frase tenga al menos 3 caracteres útiles
        if len(normalized) < 3:
            print("Is palindrome: false")

        else:
            # Comparación: un palíndromo es igual al reverso de sí mismo
            if normalized == normalized[::-1]:
                print("Is palindrome: true")
                break  # Termina el ciclo si sí es palíndromo
            else:
                print("Is palindrome: false")




# --------------------------------------------------
# Problem 4: Sentence word stats (lengths and first/last word)
# Description:
# Given a sentence, normalize spaces, split into words and return stats:
# word count, first word, last word, shortest and longest words.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - prints "Word count: <n>"
# - prints "First word: <...>"
# - prints "Last word: <...>"
# - prints "Shortest word: <...>"
# - prints "Longest word: <...>"
#
# Validations:
# - Not empty after strip()
# - At least one word after split
#
# Test cases:
# | Categoría | Escenario | Entrada (sentence) | Salida Esperada | Razón/Verificación |
# | :--- | :--- | :--- | :--- | :--- |
# | 1. Normal | Oración estándar | "Hello world from Python" | count=4, first=Hello | Separación correcta con split(). |
# | 1. Normal | Una sola palabra | "single" | count=1 | Funciona con mínimo válido. |
# | 2. Frontera | Espacios extra | "   hola   mundo  " | count=2, first=hola | Limpia espacios mediante strip y split. |
# | 2. Frontera | Palabras cortas/largas | "a bb cccc" | shortest=a, longest=cccc | Verifica min/max correctamente. |
# | 3. Error | Solo espacios | "     " | invalid | split genera lista vacía. |
# | 3. Error | Cadena vacía | "" | invalid | Falla validación de entrada. |
# | 3. Error | Caracteres no alfabéticos | "   " | invalid | No hay palabras válidas. |

# --------------------------------------------------
# 7.4 Problem 4: Sentence word stats (lengths and first/last word)

print("\nBienvenido a Sentence Word Stats.")
sentence = input("Dame una oración: ").strip().lower()

# Validaciones
if sentence == "":
    print("Error: Debes escribir una oración con al menos 2 palabras.")
else:
    words = sentence.split()

    if len(words) < 2:
        print("Error: La oración debe tener al menos 2 palabras.")
    else:
        words_count = len(words)
        first_word = words[0]
        last_word = words[-1]
        shortest_word = min(words, key=len)
        longest_word = max(words, key=len)

        print("\n--- Resultados ---")
        print("Oración ingresada:", sentence)
        print("Cantidad de palabras:", words_count)
        print("Primera palabra:", first_word)
        print("Última palabra:", last_word)
        print("Palabra más corta:", shortest_word)
        print("Palabra más larga:", longest_word)



# --------------------------------------------------
# Problem 5: Password strength classifier
# Description:
# Classify password as weak / medium / strong using documented rules.
#
# Rules (documented here):
# - Weak: length < 8 OR all lowercase OR all digits
# - Medium: length >= 8 and (has letters and digits) but missing one of the strong requirements
# - Strong: length >= 8 AND has_upper AND has_lower AND has_digit AND has_symbol
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - prints "Password strength: weak/medium/strong"
#
# Validations:
# - Not empty
# - Use len() for length checks
#
# Test cases:
# | Categoría | Escenario | Entrada (password) | Salida Esperada | Razón/Verificación |
# | :--- | :--- | :--- | :--- | :--- |
# | 1. Normal | Contraseña fuerte | P@ssw0rd | strong | Cumple upper, lower, digit, symbol y largo >= 8. |
# | 1. Normal | Contraseña media | Python123 | medium | Falta símbolo. |
# | 2. Frontera | Todo minúsculas | password | weak | Largo válido pero sin upper/digits/symbol. |
# | 2. Frontera | Todo números | 12345678 | weak | Solo dígitos. |
# | 2. Frontera | Largo justo | Abc123!@ | strong | Justo 8 caracteres. |
# | 3. Error | Vacía | "" | invalid | No pasa validación inicial. |
# | 3. Error | Solo espacios | "   " | invalid | strip la vacía. |

# --------------------------------------------------
# 7.5 Problem 5: Password strength classifier

password = input("\nSet a password: ")

# Validación de vacío
if password == "":
    print("Error: password can't be empty.")
else:
    # Reglas
    has_digit  = any(c.isdigit() for c in password)
    has_upper  = any(c.isupper() for c in password)
    has_lower  = any(c.islower() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    weak = len(password) < 8

    medium = (
        len(password) >= 8 and
        has_digit and
        (has_upper or has_lower)
    )

    strong = (
        len(password) >= 8 and
        has_digit and
        has_symbol and
        (has_upper or has_lower)
    )

    # Clasificación
    if strong:
        print("Your password is strong.")
    elif medium:
        print("Your password is medium.")
    else:
        print("Your password is weak.")



# --------------------------------------------------
# Problem 6: Product label formatter (fixed-width text)
# Description:
# Create a one-line label "Product: <NAME> | Price: $<PRICE>" of exactly 30 chars.
# If shorter, pad with spaces to the right. If longer, truncate to 30 chars.
#
# Inputs:
# - product_name (string)
# - price_value (string or numeric)
#
# Outputs:
# - prints 'Label: "<30-character-label>"'
#
# Validations:
# - product_name not empty after strip()
# - price_value convertible to positive number
#
# Test cases:
# | Categoría | Escenario | Entrada (product_name, price) | Salida Esperada | Razón/Verificación |
# | :--- | :--- | :--- | :--- | :--- |
# | 1. Normal | Nombre normal | ("Notebook", 12.5) | Label de 30 chars | Formato estándar sin corte ni relleno extremo. |
# | 1. Normal | Precio entero | ("Mouse", 200) | Label de 30 chars | Conversión a float OK. |
# | 2. Frontera | Nombre largo | ("LongProductNameExceedingLimit", 1234.56) | Label truncado a 30 chars | Verifica recorte correcto. |
# | 2. Frontera | Largo exacto | ("ABC", 1) | 30 chars exactos | Ni rellena ni recorta. |
# | 3. Error | Nombre vacío | ("", 20) | invalid | Producto no puede ser cadena vacía. |
# | 3. Error | Precio negativo | ("Laptop", -5) | invalid | Precio debe ser >= 0. |
# | 3. Error | Precio no numérico | ("Mouse", "abc") | invalid | Error al convertir float. |

# --------------------------------------------------
product_name = input("Product name: ")
price_value = input("Price: ")

# Validación: nombre no vacío
if product_name.strip() == "":
    print("Error: product name can't be empty.")
    exit()

# Validación: precio numérico y positivo
try:
    price_num = float(price_value)
    if price_num <= 0:
        print("Error: price must be positive.")
        exit()
except:
    print("Error: price must be a valid number.")
    exit()

# Convertir precio a string
price_str = str(price_num)

# Crear etiqueta base
label = f"Product: {product_name} | Price: ${price_str}"

# Ajustar a exactamente 30 caracteres
if len(label) > 30:
    label = label[:30]                          # Recorta si es más largo
else:
    label = label + " " * (30 - len(label))     # Rellena con espacios si es corto

print(f"Label: '{label}'")

# --------------------------------------------------
# Test runner: run the 3 test cases for each problem
# (these are simple demonstrative tests; replace with your own)
# --------------------------------------------------
if __name__ == "__main__":
    print("=== Problem 1 Tests ===")
    # Normal
    problem1_full_name_formatter("juan carlos tovar")
    # Border
    problem1_full_name_formatter(" Ana Maria ")
    # Error
    problem1_full_name_formatter("singleword")

    print("\n=== Problem 2 Tests ===")
    problem2_email_validator("user@example.com")
    problem2_email_validator("user.name@sub.domain.co")
    problem2_email_validator("user@@example.com")

    print("\n=== Problem 3 Tests ===")
    problem3_palindrome_checker("Anita lava la tina")
    problem3_palindrome_checker("aba")
    problem3_palindrome_checker(" a ")

    print("\n=== Problem 4 Tests ===")
    problem4_sentence_word_stats("Hello world from Python")
    problem4_sentence_word_stats(" single ")
    problem4_sentence_word_stats("   ")

    print("\n=== Problem 5 Tests ===")
    problem5_password_strength("P@ssw0rd")
    problem5_password_strength("password")
    problem5_password_strength("")

    print("\n=== Problem 6 Tests ===")
    problem6_product_label_formatter("Notebook", 12.5)
    problem6_product_label_formatter("LongProductNameExceedingLimit", 1234.56)
    problem6_product_label_formatter("", -5)

# --------------------------------------------------
# 8. CONCLUSIONES
# --------------------------------------------------
# El manejo de strings es esencial en cualquier programa, ya que la mayoría
# de los datos ingresados o mostrados se manejan como texto. Comprender cómo
# manipularlos permite procesar información de forma correcta y eficiente.
# Funciones como lower(), strip(), split() o join() se usan según la necesidad:
# limpiar espacios, unificar mayúsculas/minúsculas o separar palabras.
# Normalizar el texto antes de compararlo evita errores por diferencias mínimas.
# Además, desarrollar buenas validaciones previene datos basura y fallos lógicos.
# También aprendí que los strings son inmutables, lo que implica crear nuevas
# versiones al modificarlos, y que el slicing permite obtener partes del texto
# de forma rápida y precisa.

# --------------------------------------------------
# 9. REFERENCIAS
# --------------------------------------------------
# References:
# 1) Python documentation – Built-in Types: Text Sequence Type — str
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python documentation – String Methods
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Real Python – "Strings and Character Data in Python"
#    https://realpython.com/python-strings/
# 4) W3Schools – Python Strings Tutorial
#    https://www.w3schools.com/python/python_strings.asp
# 5) GeeksforGeeks – "Input Validation in Python" y "String Manipulation"
#    https://www.geeksforgeeks.org/
# Repository URL:
# https://github.com/2530056-boop/Homeworks_Python_jaar.git
# --------------------------------------------------
