from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para almacenar los elementos
elements = []

@app.route('/get_elements', methods=['GET'])
def get_elements():
    return jsonify(elements)

@app.route('/add_element', methods=['POST'])
def add_element():
    data = request.get_json()
    if 'element' in data:
        elements.append(data['element'])
        return jsonify({'message': 'Elemento añadido exitosamente!'}), 201
    else:
        return jsonify({'error': 'Elemento no proporcionado'}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000, debug=True)