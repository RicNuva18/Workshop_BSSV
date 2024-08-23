from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para almacenar los elementos
elements = []

@app.route('/v2/delete_element', methods=['DELETE'])
def delete_element():
    data = request.get_json()
    if 'index' in data:
        index = int(data['index'])
        if 0 <= index < len(elements):
            removed_element = elements.pop(index)
            return jsonify({'message': 'Elemento eliminado exitosamente!', 'removed_element': removed_element}), 200
        else:
            return jsonify({'error': 'Índice fuera de rango'}), 400
    else:
        return jsonify({'error': 'Índice no proporcionado'}), 400


@app.route('/v2/get_elements', methods=['GET'])
def get_elements():
    return jsonify(elements)

@app.route('/v2/add_element', methods=['POST'])
def add_element():
    data = request.get_json()
    if 'element' in data:
        elements.append(data['element'])
        return jsonify({'message': 'Elemento añadido exitosamente!'}), 201
    else:
        return jsonify({'error': 'Elemento no proporcionado'}), 400
    
@app.route('/v2/get_element', methods=['GET'])
def get_element():
    index = request.args.get('index', type=int)
    if index is not None:
        if 0 <= index < len(elements):
            return jsonify({'element': elements[index]}), 200
        else:
            return jsonify({'error': 'Índice fuera de rango'}), 400
    else:
        return jsonify({'error': 'Índice no proporcionado'}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000, debug=True)