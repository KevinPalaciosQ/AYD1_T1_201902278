from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para agregar una canción
@app.route('/agregar_cancion', methods=['POST'])
def agregar_cancion():
    data = request.get_json()
    if not all(key in data for key in ('nombre', 'artista', 'album')):
        return jsonify({'error': 'Faltan datos'}), 400
    
    cancion = {
        'nombre': data['nombre'],
        'artista': data['artista'],
        'album': data['album']
    }
    return jsonify({'mensaje': 'Canción agregada', 'cancion': cancion}), 201


if __name__ == '__main__':
    app.run(debug=True)