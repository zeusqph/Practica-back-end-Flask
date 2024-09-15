import mysql.connector
from mysql.connector import Error
def get_db_connection():

    """Establece una conexión a la base de datos MySQL."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="productos"
        )
        if connection.is_connected():
            print("Conexión a la base de datos MySQL establecida.")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def fetch_productos ():

    connection = get_db_connection()
    if connection is None:
        return [("no se pudo conectar a la base de datos")]

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos_table")
        productos = cursor.fetchall()
        cursor.close()
        return productos
    
    except Error as e:
        print(f"Error al consultar la consulta {e}")
        return [("error al conectarse a la base de datos")]
    
    finally:
        connection.close()

def fetch_producto_by_name(nombre_producto):
    """Obtiene un producto específico de la base de datos por nombre."""
    connection = get_db_connection()
    if connection is None:
        return None  # Retorna None si no se pudo conectar

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos_table WHERE nombre = %s", (nombre_producto,))
        producto = cursor.fetchone()
        cursor.close()
        return producto
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None
    finally:
        connection.close()

