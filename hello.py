from flask import Flask                          #Importo flask desde la libreria Flask

"""
Para ejecutar la app de Flask necesitamos un servidor web.
Flask proporciona uno para desarrollo pero necesitamos
un par de variables de entorno.

- Linux/Mac
    export FLASK_APP=hello   (hello es el nombre del archivo sin extension)
    export FLASK_ENV=development  (pueder ser tambien production, elegimos development por ser desarrollo)

- Windows
    set FLASK_APP=hello        (Aplicacion de arranque)
    set FLASK_ENV=development  (Aplicacion que le dice si estas en modo produccion o desarrollo)
"""                                                      
                                                    
app = Flask(__name__)                            


@app.route('/')                                  # Creamos decorador que se llama 'route' es una funcion con el parametro en este caso cuando no haya ruta 'home' ('/')                                                                     
def hola():                                      # Creamos funcion que nos devuelva ese string
     return "Hola soy Flask y tu?"