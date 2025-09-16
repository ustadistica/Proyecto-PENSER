import os
import pandas as pd

# ================
# Configuración de rutas
# ================
# Carpeta base del proyecto (la raíz donde está Proyecto-PENSER)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Carpeta de datos procesados
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")

# Archivos de entrada y salida
INPUT_FILE = "DATA_DEPURADA_SANTO_TOMAS_ESTUDIO_PENSER_MAYO_2025.xlsx"
OUTPUT_FILE = "DATA_DEPURADA_SANTO_TOMAS_ESTUDIO_PENSER_MAYO_2025.csv"

def main():
    input_path = os.path.join(DATA_DIR, INPUT_FILE)
    output_path = os.path.join(DATA_DIR, OUTPUT_FILE)

    try:
        # Leer archivo Excel
        print(f" Leyendo archivo: {input_path}")
        df = pd.read_excel(input_path)

        # Mostrar información básica
        print(" Datos cargados correctamente")
        print(df.head())

        # Guardar como CSV
        df.to_csv(output_path, index=False, encoding="utf-8-sig")
        print(f" Archivo convertido y guardado en: {output_path}")

    except FileNotFoundError:
        print(f" ERROR: No se encontró el archivo {input_path}")
    except Exception as e:
        print(f"ERROR al procesar el archivo: {e}")

if __name__ == "__main__":
    main()
