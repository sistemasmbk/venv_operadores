from flask import Flask, jsonify
from flask_cors import CORS
from bus.bus_operadores import Bus

app = Flask(__name__)
CORS(app)

@app.route('/')
def principal():
    return {"mensaje":"Hola Mundo"}

@app.route('/operadores',methods=['GET'])
def select_operadores():
    b = Bus() 
    return jsonify(b.obtener_operadores_todos())

@app.route('/operadores/<string:clave>',methods=['GET'])
def select_operador_pornumero(clave):
    b = Bus()
    return jsonify(b.obtener_operadores_por_clave(clave))

@app.route('/',methods=['POST'])
def insert_operador():
    return "Editar Operador"

@app.route('/del_operador')
def del_operador():
    return "Eliminar Operador"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
