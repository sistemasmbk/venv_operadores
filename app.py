from flask import Flask, jsonify, request
from flask_cors import CORS
from bus.bus_operadores import Bus
from vo.accion_operador import Accion_operador

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

@app.route('/operadores',methods=['POST'])
def insert_operador():
    b = Bus()
    contenido = request.json
    return jsonify(b.crear_operadores(contenido['clave'],contenido['nombre']))

@app.route('/operadores',methods=['PUT'])
def update_operador():
    b = Bus()
    contenido = request.json
    return jsonify(b.modificar_nombre_operador(contenido['clave'],contenido['nombre']))

@app.route('/operadores/delete',methods=['POST'])
def delete_operador():
    b = Bus()
    accion = Accion_operador()
    accion.clave_usuario = request.json['clave_usuario']
    accion.nombre_usuario = request.json['nombre_usuario']
    print(request.json['operador'])
    accion.operador.clave = request.json['operador']['clave']
    accion.operador.nombre = request.json['operador']['nombre']
    return jsonify(b.eliminar_operadores(accion))

# @app.route('/operadores/<string:clave>',methods=['DELETE'])
# def delete_operador(clave):
#     b = Bus()
#     return jsonify(b.eliminar_operadores(clave))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
