
vuelo = {
    "Aerolinea": "Avianca",
    "Vuelo": "AV3102",
    "Origen": "CTG",
    "Destino": "MDE",
    "Tipo_Maleta": ['Cabina', 'Mano', 'Bodega']
 }
for key, value in vuelo.items():
    print(f"{key}: {value}")

for tipo in vuelo["Tipo de Maleta"]:
    print(tipo)
