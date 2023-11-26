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

# Mostrar la sopa de letras
print("\nSopa de letras:")
for fila in sopa:
    print(' '.join(fila))
print('Las palabras a buscar son:')
print(find)