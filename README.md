# Reporte de Transacciones Bancarias

## Introducción
Esta aplicación procesa un archivo CSV con transacciones bancarias y genera un reporte que incluye:
- Balance final.
- Transacción de mayor monto.
- Conteo de transacciones por tipo.
- Generación del reporte: El resultado final se imprime en la terminal.


## Instrucciones de Ejecución
1. Clona este repositorio: `git clone https://github.com/tu-usuario/retotecnico-cobol`
2. Navega al directorio del proyecto: `cd retotecnico-cobol`
3. Coloca el archivo `transacciones.csv` en el directorio raíz del proyecto.
4. Ejecuta la aplicación: `python main.py`

## Enfoque y Solución
La lógica del programa se implementa en Python utilizando estructuras simples como bucles y diccionarios para calcular los valores requeridos. La biblioteca `csv` permite procesar el archivo de entrada.

## Estructura del Proyecto
- `main.py`: Código fuente de la aplicación.
- `transacciones.csv`: Archivo de entrada con las transacciones.
- `README.md`: Documentación del proyecto.

## Documentación y Calidad del Código
El código está documentado con comentarios para explicar los pasos clave y las decisiones tomadas. Se privilegia la legibilidad y simplicidad para facilitar su comprensión.

Notas adicionales
- Asegúrate de tener Python instalado en tu máquina (versión 3.6 o superior).
- Puedes reemplazar  con tu propio archivo CSV, siempre que tenga el formato indicado.

Estructura del archivo CSV.

id,tipo,monto
1,Crédito,100.00
2,Débito,50.00
3,Crédito,200.00
4,Débito,75.00
5,Crédito,150.00
