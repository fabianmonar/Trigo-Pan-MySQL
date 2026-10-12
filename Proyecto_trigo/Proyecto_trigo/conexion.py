import mysql.connector

def get_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # <--- acá va tu pass, ej: "1234" o "root"
        database="trigo_db"
    )