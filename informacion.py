
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para ver la información del usuario
@app.route('/ver_informacion', methods=['GET'])
def ver_informacion():
    info = {
        'nombre': 'Kevin Estuardo Palacios Quiñonez',
        'carnet': '201902278'
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
