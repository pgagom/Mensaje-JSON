# Importa las clases y funciones esenciales de Flask:
# - Flask: Clase principal para crear la aplicación web.
# - request: Objeto para acceder a datos de la solicitud HTTP (como formularios o JSON).
# - jsonify: Función para crear respuestas HTTP en formato JSON.
# - render_template: Función para renderizar archivos HTML desde la carpeta 'templates'.
from flask import Flask, request, jsonify, render_template

# Importa el módulo 'json' para trabajar con datos en formato JSON (lectura/escritura).
import json

# Importa el módulo 'os' para operaciones del sistema operativo (rutas, archivos, etc.).
import os

# Crea una instancia de la aplicación Flask.
# __name__ es una variable especial de Python que indica el nombre del módulo actual.
# Esto permite a Flask encontrar recursos como plantillas o archivos estáticos.
app = Flask(__name__)

# Define la ruta absoluta del archivo donde se guardarán los mensajes:
# 1. os.path.abspath(__file__): Ruta completa del archivo actual (server.py).
# 2. os.path.dirname(): Obtiene el directorio padre de la ruta (carpeta del proyecto).
# 3. os.path.join(): Une las partes de la ruta de forma compatible con cualquier sistema operativo.
# Resultado: "[Ruta_del_proyecto]/data/mensajes.json"
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "mensajes.json")

# Decorador que asocia la URL "/" con la función home().
# Responde solo a solicitudes GET (método por defecto).
@app.route("/")
def home():
    # Renderiza el archivo HTML 'index.html' ubicado en la carpeta 'templates'.
    # Flask automáticamente busca plantillas en dicha carpeta.
    return render_template("index.html")

# Decorador para la URL "/guardar", configurado para aceptar solo métodos POST.
# POST se usa para enviar datos al servidor (como formularios o JSON).
@app.route("/guardar", methods=["POST"])
def guardar_mensaje():
    # Obtiene el valor de la clave "mensaje" del cuerpo JSON de la solicitud.
    # Si no existe, devuelve una cadena vacía (""). Ejemplo: {"mensaje": "Hola Mundo"}.
    mensaje = request.json.get("mensaje", "")
    
    # Abre el archivo en modo escritura ("w"), lo que SOBREESCRIBE todo su contenido anterior.
    # 'with' asegura que el archivo se cierre automáticamente tras finalizar.
    with open(DATA_FILE, "w") as f:
        # Escribe el mensaje en el archivo como una lista de un elemento en formato JSON.
        # Ejemplo: Si mensaje = "Hola", el archivo contendrá ["Hola"].
        json.dump([mensaje], f)
    
    # Devuelve una respuesta vacía (cadena vacía) con código HTTP 200 (éxito por defecto).
    return ""

# Bloque condicional: Solo se ejecuta si el script es el programa principal.
# Evita que el servidor se inicie si el archivo es importado como módulo.
if __name__ == "__main__":
    # Inicia el servidor web de Flask con configuración específica:
    # - host='0.0.0.0': Hace que el servidor sea accesible desde cualquier dispositivo en la red.
    # - port=5000: Puerto donde escucha el servidor (http://localhost:5000).
    app.run(host='0.0.0.0', port=5000)