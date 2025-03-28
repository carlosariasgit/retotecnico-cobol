import csv

def procesar_transacciones(archivo_csv):
    balance = 0
    transaccion_max = {"id": None, "monto": 0}
    conteo_transacciones = {"Crédito": 0, "Débito": 0}

    # Leer el archivo CSV
    with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            tipo = fila["tipo"]
            monto = float(fila["monto"])
            transaccion_id = fila["id"]

            # Calcular balance
            if tipo == "Crédito":
                balance += monto
                conteo_transacciones["Crédito"] += 1
            elif tipo == "Débito":
                balance -= monto
                conteo_transacciones["Débito"] += 1

            # Verificar transacción de mayor monto
            if monto > transaccion_max["monto"]:
                transaccion_max["id"] = transaccion_id
                transaccion_max["monto"] = monto

    # Retornar los resultados
    return balance, transaccion_max, conteo_transacciones


def generar_reporte(balance, transaccion_max, conteo_transacciones):
    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {transaccion_max['id']} - {transaccion_max['monto']:.2f}")
    print(f"Conteo de Transacciones: Crédito: {conteo_transacciones['Crédito']} Débito: {conteo_transacciones['Débito']}")


# Punto de entrada del programa
if __name__ == "__main__":
    archivo_csv = "transacciones.csv"  # Nombre del archivo CSV
    balance, transaccion_max, conteo_transacciones = procesar_transacciones(archivo_csv)
    generar_reporte(balance, transaccion_max, conteo_transacciones)