import mysql.connector
from conexion import get_conexion

class Trigo:
    def guardar(self, provincia_id, anio, produccion):
        con = get_conexion()
        cur = con.cursor()
        # Insertamos en tu tabla real trigo_db.trigo
        cur.execute("""
            INSERT INTO trigo (cultivo, anio, campania, provincia, provincia_id, produccion_tm, superficie_sembrada_ha, superficie_cosechada_ha)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, ('Trigo', anio, f"{anio}/{anio+1}", f"Prov_{provincia_id}", provincia_id, produccion, 1000, 900))
        con.commit()
        print("Alta OK")
        cur.close()
        con.close()

    @staticmethod
    def eliminar(id_a_borrar):
        # Como tu tabla no tiene ID, borramos por provincia_id para la demo
        con = get_conexion()
        cur = con.cursor()
        cur.execute("DELETE FROM trigo WHERE provincia_id = %s LIMIT 1", (id_a_borrar,))
        con.commit()
        print(f"Baja OK - filas: {cur.rowcount}")
        cur.close()
        con.close()

    @staticmethod
    def modificar(prov_id, nueva_prod):
        con = get_conexion()
        cur = con.cursor()
        cur.execute("UPDATE trigo SET produccion_tm = %s WHERE provincia_id = %s", (nueva_prod, prov_id))
        con.commit()
        print(f"Modificacion OK - filas: {cur.rowcount}")
        cur.close()
        con.close()

    @staticmethod
    def buscar_por_anio(anio):
        con = get_conexion()
        cur = con.cursor()
        cur.execute("SELECT provincia, anio, produccion_tm FROM trigo WHERE anio = %s LIMIT 10", (anio,))
        for r in cur.fetchall():
            print(r)
        cur.close()
        con.close()

    @staticmethod
    def buscar_por_provincia(prov_id):
        con = get_conexion()
        cur = con.cursor()
        cur.execute("SELECT provincia, anio, produccion_tm FROM trigo WHERE provincia_id = %s LIMIT 10", (prov_id,))
        for r in cur.fetchall():
            print(r)
        cur.close()
        con.close()

    @staticmethod
    def consultar_view():
        con = get_conexion()
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM vista_perdidas_provincia LIMIT 10")
        except:
            # Si no existe la vista, mostramos un resumen que es lo mismo que pide la vista
            cur.execute("SELECT provincia, AVG(pct_perdida) as perdida_prom FROM trigo GROUP BY provincia LIMIT 10")
        for r in cur.fetchall():
            print(r)
        cur.close()
        con.close()

while True:
    print("\n1-Alta 2-Baja 3-Modificar 4-Buscar Año 5-Buscar Provincia 6-VER VIEW 7-Salir")
    op = input("Opcion: ").strip()
    if op == "1":
        id_p = int(input("id_provincia (provincia_id): "))
        an = int(input("anio: "))
        pr = float(input("prod (produccion_tm): "))
        Trigo().guardar(id_p, an, pr)
    elif op == "2":
        Trigo.eliminar(int(input("provincia_id a borrar: ")))
    elif op == "3":
        Trigo.modificar(int(input("provincia_id: ")), float(input("nueva prod: ")))
    elif op == "4":
        Trigo.buscar_por_anio(int(input("anio: ")))
    elif op == "5":
        Trigo.buscar_por_provincia(int(input("provincia_id: ")))
    elif op == "6":
        Trigo.consultar_view()
    elif op == "7":
        break