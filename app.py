from  flask import Flask , jsonify

app = Flask(__name__)

from productos import productos

@app.route("/")
def entrada():
    return jsonify({"Mensaje":"Recivido"})

@app.route("/productos")
def GetProductos():
    return jsonify({"Lista de Productos ": productos})

@app.route("/productos/<string:nombre_producto>")
def GetProducto(nombre_producto):
    Producto_Encontrado =[producto for producto in productos if producto ["nombre"]== nombre_producto]
    if len(Producto_Encontrado) == 0 :
        return jsonify({"Error":"El producto no fue encontrado "}) , 404
    

    return  jsonify ({"producto":Producto_Encontrado[0]})

if __name__ == "__main__":
    app.run(debug=True)

