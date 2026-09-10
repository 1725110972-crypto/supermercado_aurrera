# -*- coding: utf-8 -*-
"""
Sistema de Productos del Supermercado (Aurrera)
------------------------------------------------
Framework: Flask
Base de datos: SQLite3
"""
from flask import Flask, render_template, request

from db.database import crear_tabla, obtener_productos
from db.seed_data import poblar_base_de_datos
from tda.lista_ordenada import ListaOrdenada

app = Flask(__name__)

REGLAS = {
    "categoria": "Categoria",
    "nombre": "Nombre del producto",
    "precio": "Precio",
    "fecha_caducidad": "Fecha de caducidad",
    "unidad_medida": "Unidad de medida",
    "cantidad_inventario": "Cantidad en inventario",
    "marca": "Marca",
    "codigo_barras": "Codigo de barras",
}


def construir_clave(criterio, subcriterio):
    if criterio == "categoria" and subcriterio in REGLAS:
        return lambda p: (p["categoria"], p[subcriterio])
    if criterio in REGLAS:
        return lambda p: p[criterio]
    return lambda p: p["categoria"]


@app.route("/")
def index():
    crear_tabla()
    poblar_base_de_datos()
    return render_template("index.html", reglas=REGLAS)


@app.route("/lista")
def lista():
    crear_tabla()
    criterio = request.args.get("criterio", "categoria")
    subcriterio = request.args.get("subcriterio", "")
    precio_min = request.args.get("precio_min", "")
    precio_max = request.args.get("precio_max", "")
    precio_exacto = request.args.get("precio_exacto", "")

    productos = obtener_productos()
    clave = construir_clave(criterio, subcriterio)

    lista_ordenada = ListaOrdenada(clave)
    for producto in productos:
        lista_ordenada.insertar(producto)

    resultado = lista_ordenada.obtener_todos()

    if criterio == "precio" and precio_exacto:
        resultado = lista_ordenada.buscar_por_valor(float(precio_exacto))
    elif criterio == "precio" and precio_min and precio_max:
        resultado = lista_ordenada.buscar_por_rango(float(precio_min), float(precio_max))

    return render_template("lista.html", productos=resultado, criterio=criterio, reglas=REGLAS)


if __name__ == "__main__":
    crear_tabla()
    poblar_base_de_datos()
    app.run(host="0.0.0.0", port=8080, debug=True)
