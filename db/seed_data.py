# -*- coding: utf-8 -*-
"""
Precarga la base de datos con un catálogo amplio de productos del
supermercado (estilo Bodega Aurrera), organizado por categoría y con
marcas reales del mercado mexicano.
"""
import random

try:
    from db.database import crear_tabla, contar_productos, insertar_producto
except ImportError:
    from database import crear_tabla, contar_productos, insertar_producto


CATALOGO = {
    "Frutas y Verduras": [
        ("Manzana", "1 kg", 28, 55, ["Granel", "Del Monte", "Fresh Del Monte"]),
        ("Platano", "1 kg", 16, 24, ["Granel"]),
        ("Jitomate", "1 kg", 18, 32, ["Granel"]),
        ("Aguacate", "1 kg", 45, 90, ["Granel"]),
        ("Cebolla", "1 kg", 18, 28, ["Granel"]),
        ("Lechuga", "1 pza", 14, 22, ["Granel"]),
        ("Uva sin semilla", "500 g", 35, 60, ["Dole", "San Miguel"]),
        ("Piña", "1 pza", 30, 45, ["Dole", "Fresh Del Monte"]),
        ("Zanahoria", "1 kg", 15, 22, ["Green Giant", "Granel"]),
        ("Elote amarillo", "500 g", 20, 30, ["Green Giant"]),
        ("Fresa", "500 g", 35, 55, ["Driscoll's"]),
        ("Zarzamora", "170 g", 40, 60, ["Driscoll's"]),
        ("Frambuesa", "170 g", 45, 65, ["Driscoll's"]),
    ],
    "Lacteos, Huevo y Refrigerados": [
        ("Leche entera", "1 L", 24, 30, ["Alpura", "Lala", "Santa Clara"]),
        ("Leche deslactosada", "1 L", 26, 33, ["Lala", "Alpura"]),
        ("Bebida de almendra", "946 ml", 45, 60, ["Silk", "Almond Breeze"]),
        ("Leche evaporada", "360 ml", 22, 28, ["Nestlé Carnation"]),
        ("Queso panela", "400 g", 55, 75, ["Nochebuena", "La Villita"]),
        ("Queso crema", "190 g", 32, 42, ["Philadelphia", "Bionda"]),
        ("Queso amarillo", "220 g", 45, 60, ["Fud", "Nochebuena"]),
        ("Crema acida", "450 g", 30, 40, ["Alpura", "Lala"]),
        ("Yogurt griego", "150 g", 15, 22, ["Danone", "Oikos", "Chobani"]),
        ("Yogurt bebible", "1 L", 30, 40, ["Yoplait", "Activia"]),
        ("Yogurt para niños", "4 pack", 28, 38, ["Danonino"]),
        ("Mantequilla", "90 g", 40, 55, ["Gloria", "Lurpak"]),
        ("Margarina", "90 g", 20, 28, ["Primavera", "Imperial"]),
        ("Huevo blanco", "18 pza", 48, 65, ["San Juan", "El Calvario", "Bachoco"]),
    ],
    "Abarrotes y Despensa": [
        ("Aceite vegetal", "1 L", 38, 52, ["Capullo", "Nutrioli", "1-2-3"]),
        ("Mayonesa", "390 g", 35, 48, ["Hellmann's", "McCormick"]),
        ("Catsup", "397 g", 28, 38, ["Heinz", "Clemente Jacques"]),
        ("Chiles en lata", "220 g", 15, 22, ["Herdez", "La Costeña"]),
        ("Atun en lata", "140 g", 16, 24, ["Tuny", "Dolores"]),
        ("Verduras enlatadas", "400 g", 14, 20, ["San Marcos", "Herdez"]),
        ("Sopa enlatada", "300 g", 20, 30, ["Campbell's"]),
        ("Pasta para sopa", "200 g", 12, 18, ["La Moderna", "Barilla"]),
        ("Sazonador en polvo", "165 g", 18, 26, ["Knorr", "Yemina"]),
        ("Salsa para pasta", "340 g", 30, 42, ["Prego", "Ragú"]),
        ("Arroz", "1 kg", 24, 34, ["Verde Valle", "Schettino"]),
        ("Frijol", "1 kg", 26, 38, ["Verde Valle", "Isadora", "Verde Campo"]),
        ("Cereal de hojuelas", "500 g", 45, 65, ["Kellogg's", "Nestlé"]),
        ("Galletas", "170 g", 18, 28, ["Gamesa", "Marinela", "Oreo", "Ritz"]),
        ("Avena", "1 kg", 30, 42, ["Quaker"]),
        ("Harina de maiz", "1 kg", 20, 28, ["Maseca"]),
        ("Mezcla para hot cakes", "800 g", 35, 48, ["Hot Cakes Pronto"]),
        ("Harina de trigo", "1 kg", 22, 30, ["Tres Estrellas"]),
    ],
    "Carnes, Pescados y Salchichoneria": [
        ("Jamon de pavo", "250 g", 45, 65, ["Fud", "San Rafael", "Peñaranda"]),
        ("Salchicha", "500 g", 30, 45, ["Zwan", "Chimex", "Fud"]),
        ("Tocino", "200 g", 40, 55, ["Fud", "Kir"]),
        ("Pechuga de pollo", "1 kg", 75, 110, ["Bachoco", "PILGRIM'S"]),
        ("Muslo de pollo", "1 kg", 55, 80, ["Bachoco"]),
        ("Carne molida de res", "1 kg", 120, 170, ["SuKarne"]),
        ("Filete de tilapia", "1 kg", 110, 160, ["Neptuno", "Marina Azul"]),
        ("Camaron congelado", "400 g", 130, 190, ["Grupo Mar"]),
    ],
    "Panaderia y Tortilleria": [
        ("Pan de caja blanco", "680 g", 32, 42, ["Bimbo", "Wonder", "Oroweat"]),
        ("Pan integral", "680 g", 38, 50, ["Bimbo", "Oroweat"]),
        ("Panque", "435 g", 25, 35, ["Marinela", "Tía Rosa"]),
        ("Tortilla de maiz", "1 kg", 18, 26, ["Milpa Real", "Maseca"]),
        ("Tortilla de harina", "10 pza", 20, 30, ["Tortillinas Tía Rosa"]),
    ],
    "Bebidas y Botanas": [
        ("Agua natural", "1.5 L", 12, 18, ["Ciel", "Bonafont", "Epura"]),
        ("Agua mineral", "600 ml", 14, 20, ["Peñafiel"]),
        ("Refresco de cola", "600 ml", 16, 24, ["Coca-Cola", "Pepsi"]),
        ("Refresco sabor mandarina", "600 ml", 15, 22, ["Jarritos"]),
        ("Bebida electrolitica", "630 ml", 20, 28, ["Electrolit"]),
        ("Jugo de naranja", "1 L", 24, 34, ["Del Valle", "Jumex"]),
        ("Jugo de arandano", "1 L", 35, 48, ["Ocean Spray"]),
        ("Te helado", "500 ml", 18, 25, ["Arizona", "Lipton"]),
        ("Cafe soluble", "170 g", 65, 95, ["Nescafé", "Los Portales"]),
        ("Cafe en grano", "400 g", 110, 160, ["Punta del Cielo"]),
        ("Te en bolsitas", "25 pza", 30, 45, ["Twinings", "Lipton"]),
        ("Papas fritas", "170 g", 22, 32, ["Sabritas", "Barcel"]),
        ("Totopos", "280 g", 20, 30, ["Totis", "Doritos"]),
        ("Papas onduladas", "128 g", 25, 35, ["Pringles"]),
        ("Botana de maiz", "150 g", 15, 24, ["Guerrero"]),
    ],
    "Cervezas, Vinos y Licores": [
        ("Cerveza clara", "6 pack 355 ml", 85, 120, ["Corona", "Victoria", "Tecate"]),
        ("Cerveza obscura", "355 ml", 18, 26, ["Modelo", "Dos Equis"]),
        ("Cerveza importada", "355 ml", 22, 32, ["Heineken"]),
        ("Ron", "750 ml", 220, 320, ["Bacardí"]),
        ("Tequila", "750 ml", 350, 550, ["Don Julio"]),
        ("Whisky", "750 ml", 400, 600, ["Jack Daniel's"]),
        ("Vino tinto", "750 ml", 180, 280, ["Casillero del Diablo", "Concha y Toro"]),
    ],
    "Cuidado Personal y Belleza": [
        ("Pasta dental", "100 ml", 28, 42, ["Colgate", "Oral-B", "Sensodyne"]),
        ("Enjuague bucal", "500 ml", 55, 75, ["Listerine"]),
        ("Shampoo", "400 ml", 45, 65, ["Pantene", "Head & Shoulders", "Sedal"]),
        ("Acondicionador", "400 ml", 45, 65, ["L'Oréal", "Garnier"]),
        ("Jabon de tocador", "3 pack", 30, 42, ["Dove", "Palmolive"]),
        ("Desodorante", "150 ml", 38, 55, ["Rexona", "Axe", "Secret"]),
        ("Crema corporal", "400 ml", 50, 70, ["Nivea"]),
        ("Toallas femeninas", "10 pza", 25, 35, ["Saba", "Kotex"]),
        ("Pañales", "paquete", 220, 320, ["Huggies", "Pampers"]),
        ("Jabon para bebe", "200 ml", 40, 55, ["Johnson's Baby"]),
    ],
    "Limpieza del Hogar": [
        ("Detergente en polvo", "1 kg", 75, 100, ["Ariel", "Ace"]),
        ("Jabon en barra", "400 g", 18, 26, ["Zote"]),
        ("Suavizante de telas", "850 ml", 45, 60, ["Suavitel", "Downy", "Ensueño"]),
        ("Jabon liquido para trastes", "750 ml", 28, 40, ["Salvo", "Axion"]),
        ("Limpiador multiusos", "1 L", 30, 42, ["Fabuloso", "Pine-Sol"]),
        ("Desinfectante", "500 ml", 25, 35, ["Lysol"]),
        ("Cloro", "1 L", 18, 26, ["Cloralex"]),
        ("Papel higienico", "4 rollos", 48, 68, ["Regio", "Pétalo", "Elite"]),
        ("Servilletas", "1 paquete", 18, 28, ["Kleenex", "Suavel"]),
    ],
    "Mascotas": [
        ("Alimento para perro adulto", "3 kg", 180, 280, ["Dog Chow", "Pedigree", "Ganador"]),
        ("Alimento para perro premium", "3 kg", 350, 480, ["Pro Plan", "Royal Canin"]),
        ("Alimento para gato", "1.5 kg", 90, 140, ["Cat Chow", "Whiskas"]),
    ],
}


def generar_codigo_barras(indice):
    return "750{:010d}".format(1000000 + indice)


def generar_productos():
    random.seed(42)
    productos = []
    indice = 0
    dias_caducidad_por_categoria = {
        "Frutas y Verduras": (5, 20),
        "Lacteos, Huevo y Refrigerados": (10, 45),
        "Panaderia y Tortilleria": (5, 25),
        "Carnes, Pescados y Salchichoneria": (5, 30),
        "Bebidas y Botanas": (90, 400),
        "Abarrotes y Despensa": (120, 500),
        "Cervezas, Vinos y Licores": (200, 700),
        "Cuidado Personal y Belleza": (300, 900),
        "Limpieza del Hogar": (300, 900),
        "Mascotas": (200, 500),
    }

    for categoria, items in CATALOGO.items():
        rango_dias = dias_caducidad_por_categoria.get(categoria, (30, 200))
        for item in items:
            nombre_generico, unidad_medida, precio_min, precio_max, marcas = item
            for marca in marcas:
                indice += 1
                precio = round(random.uniform(precio_min, precio_max), 2)
                dias = random.randint(*rango_dias)
                mes = min(9 + (dias // 30), 12)
                dia = min(1 + (dias % 28), 28)
                anio = 2026 if mes <= 12 else 2027
                fecha_caducidad = f"{anio}-{mes:02d}-{dia:02d}"
                cantidad_inventario = random.randint(15, 250)

                productos.append({
                    "categoria": categoria,
                    "nombre": f"{nombre_generico} {marca}",
                    "precio": precio,
                    "fecha_caducidad": fecha_caducidad,
                    "unidad_medida": unidad_medida,
                    "cantidad_inventario": cantidad_inventario,
                    "marca": marca,
                    "codigo_barras": generar_codigo_barras(indice),
                })
    return productos


PRODUCTOS_INICIALES = generar_productos()


def poblar_base_de_datos():
    crear_tabla()
    if contar_productos() == 0:
        for producto in PRODUCTOS_INICIALES:
            insertar_producto(producto)
        print(f"Se insertaron {len(PRODUCTOS_INICIALES)} productos de ejemplo.")
    else:
        print("La base de datos ya tiene productos, no se vuelve a poblar.")


if __name__ == "__main__":
    poblar_base_de_datos()
