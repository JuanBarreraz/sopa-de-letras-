# Sopa-de-letras
 ## GRUPO LOS ABBES
 ## Proyecto_sopa de letras en python
 En este repositorio se encuentra el paso a paso utilizado para crear una sopa de letras en Python, donde el usuario puede acomodar la sopa de letras a su gusto. El usuario puede controlar el número de columnas y filas de la sopa de letras, además de escoger entre generar la sopa de letras con palabras de la base de datos o usar palabras ingresadas por él.
 - ## Primer paso
   El primer paso fue importar 2 librerías que nos ayudarían al desarrollo de la sopa de letras más adelante y crear la lista de palabras que iban a estar por defecto en la sopa de letras. 
```python
import random
import string

# Lista de palabras que se usan automático
auto = ["Humano", "persona", "gente", "hombre", "mujer", "bebé", "niño", "niña", "don", "doña", 
    "señor", "señora", "dama", "individuo", "salud", "cuerpo", "pierna", "pie", "talón", 
    "cabeza", "cara", "boca", "labio", "diente", "ojo", "nariz", "barba", "cuello", 
    "amor", "padre", "madre", "hijo", "hija", "abuelo", "abuela", "nieto", "nieta", 
    "tío", "tía", "ser", "vida", "muerte", "campo", "bosque", "selva", "desierto", 
    "costa", "playa", "río", "lago", "mar", "océano", "cerro", "monte", "luz", "animal", 
    "perro", "gato", "vaca", "cerdo", "caballo", "yegua", "oveja", "mono", "ratón", 
    "rata", "tigre", "conejo", "dragón", "ciervo", "rana", "león", "pájaro", "pez", 
    "calamar", "pulpo", "bicho", "mosca", "mosquito", "cucaracha", "caracol", 
    "lombriz", "lagarto", "serpiente", "alimento", "comida", "bebida", "vegetal", 
    "planta", "pasto", "flor", "fruta", "semilla", "árbol", "hoja", "raíz", "hongo", 
    "ciruela", "pino", "nuez", "arroz", "avena", "verdura", "tiempo", "clima", 
    "cielo", "este", "oeste", "sur", "norte", "ayer", "hoy", "día", "mes", "año", 
    "siglo", "calor", "agua", "hielo", "fuego", "aire", "tierra", "metal", "sal", 
    "barro", "lodo", "peso", "metro", "gramo", "kilo", "medida", "sociedad", 
    "equipo", "país", "gobierno", "estado", "campaña", "club", "congreso", 
    "consejo", "partido", "obligación", "derecho", "permiso", "prohibición", 
    "ley", "economía", "consumo", "empresa", "hotel", "cuenta", "dinero", 
    "billete", "cambio", "máquina", "precio", "valor", "hogar", "silla", 
    "mesa", "cama", "panel", "puerta", "ropa", "manga", "cuello", "zapato", 
    "gafas", "voz", "texto", "color", "blanco", "negro", "campo", "ronda", "campo", "veloz", "flor", "abeja", "huerto", "azul", "gota", "fuego", 
    "ágil", "viento", "línea", "calle", "vela", "cinta", "mar", "azúcar", "arte", "papel", 
    "llama", "fruta", "melón", "silla", "mesa", "traje", "gota", "parque", "risa", "risueño", 
    "grano", "llave", "botón", "gente", "piedra", "risa", "paz", "arte", "mano", "forma", 
    "tubo", "tela", "lienzo", "verde", "playa", "arena", "piedra", "llama", "mundo", "veloz", 
    "aire", "onda", "rana", "grano", "blusa", "gota", "taza", "carro", "azúcar", "nuez", 
    "niño", "coral", "gota", "raya", "sonrisa", "risa", "luz", "rayo", "bruma", "limón", 
    "rama", "vino", "grano", "golpe", "gota", "onda", "onda", "orilla", "campo", "rayo", 
    "grano", "gafas", "pista", "rata", "puma", "rama", "hilo", "miel", "luz", "lupa", 
    "río", "duna", "luz", "duna", "dibujo", "anillo", "onda", "globo", "balsa", "ruta", 
    "pulso", "rosa", "buena", "cama", "silla", "coral", "pestaña", "musgo", "luz", "mago"
]
```
- ## Segundo paso
  Después de crear la lista de palabras, se procedió a crear el código en Python, como se muestra a continuación.
```python
# Se permite elegir el modo de armar la sopa de letras
print("\n\nHola, bienvenido a este programa generador de sopas de letras hecho en Python; a continuación podrá elegir la sopa de letras que más se ajusta a sus necesidades:")
z = int(input("\nElija cómo desea hacer su sopa de letras: \n 1 - Usted inserta las palabras que desea sean incluídas. \n 2 - Las palabras son elegidas por el programa. \n Escriba el número de la opción que le guste: "))

def check_overlap(word, sopa, fila, col, direccion):
    # Verifica si la palabra puede colocarse en la sopa sin sobreponerse.
    for i in range(len(word)):
        if direccion == 'horizontal' and sopa[fila][col + i] != ' ' and sopa[fila][col + i] != word[i]:
            return False
        elif direccion == 'vertical' and sopa[fila + i][col] != ' ' and sopa[fila + i][col] != word[i]:
            return False
    return True

a = False
b = 0
c = False
blabla = []
find = []
```

Primero, se creó la opción para el usuario sobre cómo crear su sopa de letras, ya sea tomando palabras aleatorias o seleccionándolas de la lista preexistente en el programa. Seguido, creamos la función que permite que las palabras ingresadas se puedan colocar en la sopa de letras sin superponerse sobre otras. Después, se generan las filas y columnas en base a las palabras. Para ello, se utilizan strings y listas vacías para generar las filas y columnas.

- ## Tercer paso
  En esta parte, se crea el código en el cual el usuario puede elegir el tamaño de la sopa de letras, limitado por un mínimo de 10x10 y un máximo de 30x30.
```python
# Se permite al usuario elegir el tamaño de la sopa de letras
size = int(input("Elija el tamaño de su sopa de letras (Ej: si ingresa el número 15, se creará una sopa de letras de 15 filas y 15 columnas)\nTenga en cuenta que el mínimo es de 10 y el máximo es 30. Valor: "))
while a == False:
    if size < 10:
        size = int(input("Recuerde que el mínimo es de 10, vuelva a intentarlo. \tValor: "))
    elif size > 30:
        size = int(input("Recuerde que el máximo es de 30, vuelva a intentarlo. \tValor: "))
    else:
        a = True

# Se introducen las palabras que serán utilizadas en la sopa de letras
cantidad = int(input("¿Cuántas palabras desea ingresar en su sopa de letras?: "))
if z==1:    
    while b < cantidad:
        c = input('Inserte una palabra que quiere incluir sin tildes; tenga en cuenta el límite ingresado. Palabra: ')
        find.append(c)
        words = list(c.upper())
        if len(words) <= size:
            blabla.append(words)
            b = b + 1
        else:
            print("La palabra es demasiado larga para acomodar en la sopa de letras.")
elif z==2:
    while b < cantidad:
        c = random.choice(auto)
        find.append(c)
        words = list(c.upper())
        blabla.append(words)
        b = b + 1
letras = string.ascii_uppercase  # Obtiene todas las letras mayúsculas del alfabeto
sopa = [[' ' for _ in range(size)] for _ in range(size)]
```
Por otra parte, creamos con condicionales la opción para que el usuario pueda poner las palabras que quiere en la sopa de letras o, por el contrario, tomarlas de la lista que ya proporcionamos aleatoriamente. Hacemos que todas las letras de las palabras ingresadas aparezcan en mayúscula.
 ```python
# Se introducen las palabras que serán utilizadas en la sopa de letras
cantidad = int(input("¿Cuántas palabras desea ingresar en su sopa de letras?: "))
if z==1:    
    while b < cantidad:
        c = input('Inserte una palabra que quiere incluir sin tildes; tenga en cuenta el límite ingresado. Palabra: ')
        find.append(c)
        words = list(c.upper())
        if len(words) <= size:
            blabla.append(words)
            b = b + 1
        else:
            print("La palabra es demasiado larga para acomodar en la sopa de letras.")
elif z==2:
    while b < cantidad:
        c = random.choice(auto)
        find.append(c)
        words = list(c.upper())
        blabla.append(words)
        b = b + 1
letras = string.ascii_uppercase  # Obtiene todas las letras mayúsculas del alfabeto
sopa = [[' ' for _ in range(size)] for _ in range(size)]
``` 
 - ## Cuarto paso
   Ya en este punto, se utilizó un código que organiza las palabras tanto en vertical como en horizontal, y al mismo tiempo, genera letras al azar para rellenar la sopa de letras.
  ``` python
   # Colocar palabras horizontal y verticalmente sin sobreponerse
for palabra in blabla:
    direccion = random.choice(['horizontal', 'vertical'])
    c = False  # Reiniciar c a False antes de intentar colocar cada palabra
    if direccion == 'horizontal':
        while c == False:
            fila = random.randint(0, size - 1)
            col = random.randint(0, size - len(palabra))
            if check_overlap(palabra, sopa, fila, col, direccion):
                for i in range(len(palabra)):
                    sopa[fila][col + i] = palabra[i]
                c = True
    else:
        while c == False:
            fila = random.randint(0, size - len(palabra))
            col = random.randint(0, size - 1)
            if check_overlap(palabra, sopa, fila, col, direccion):
                for i in range(len(palabra)):
                    sopa[fila + i][col] = palabra[i]
                c = True

# Rellenar el resto de la sopa con letras aleatorias
for fila in range(size):
    for col in range(size):
        if sopa[fila][col] == ' ':
            sopa[fila][col] = random.choice(letras)
``` 
- ## Quinto paso
  Por último, hacemos que la sopa de letras se genere en la terminal por fila y columna.
```python
# Mostrar la sopa de letras
print("\nSopa de letras:")
for fila in sopa:
    print(' '.join(fila))
print('Las palabras a buscar son:')
print(find)
```
- ## Sexto paso
 En este punto, debemos crear cómo interactuar con nuestra sopa de letras. Así que se inicia un bucle mientras 'j' sea igual a 'incomplete'. Este bucle permite al usuario intentar encontrar palabras hasta que todas las palabras hayan sido encontradas. El usuario ingresa las coordenadas (fila y columna) donde cree que se encuentra una palabra.
```python
  #Comprueba si hay o no una palabra
j = 'incomplete'
while j == 'incomplete':
    n='nada'
    h=0
    ox = int(input("Inserte la columna en la que cree hay una palabra (Empezando desde 0): "))
    oy = int(input("Inserte la fila en la que cree hay una palabra (Empezando desde 0): "))
    o= [oy, ox]
```
- Seguido de esto, se utiliza un bucle para comparar la posición ingresada por el usuario con las posiciones donde se encuentran las palabras en la sopa. Si la posición coincide con una de las posiciones de palabras, se elimina esa posición de la lista 'posiciones' y se imprime un mensaje. Si no hay coincidencias, se establece 'n' en 'nada'. Además, se imprime un mensaje si la posición ingresada es incorrecta. También se muestra la longitud actual de la lista 'posiciones'.
```python
    while h<len(posiciones):
        if o == posiciones[h]:
            del posiciones[h]
            print('Corecto, en esa posición había una palabra, encuentra las otras')
            n='found'
        else: n='nada'
        h=h+1
    if n=='nada':
        print('La posición es incorrecta, intente otra vez')
    print(len(posiciones))
```
- ## Septimo paso
  Ya para finalizar, verificamos si la lista de posiciones está vacía. Esto significa que todas las palabras han sido encontradas y se establece 'j' en 'complete', lo que finaliza el bucle principal. Luego, se imprime un mensaje de felicitación cuando el usuario ha encontrado todas las palabras.
```python
  if len(posiciones)<=0:
        j = 'complete'

if j == 'complete':
    print('Felicitaciones, ha acabado la sopa de letras')
```
