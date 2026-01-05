import os
import sys
from qr import generar_qr
from pdf import generar_pdf

def test_qr_generation():
    print("Probando generación de QR...")
    try:
        path = generar_qr("https://google.com", "test_user")
        if os.path.exists(path):
            print(f"✅ QR generado en: {path}")
            return path
        else:
            print("❌ Error: El archivo QR no existe.")
            return None
    except Exception as e:
        print(f"❌ Error en QR: {e}")
        return None

def test_pdf_generation(qr_path):
    print("Probando generación de PDF...")
    try:
        path = generar_pdf("test_user", qr_path)
        if os.path.exists(path):
            print(f"✅ PDF generado en: {path}")
            return path
        else:
            print("❌ Error: El archivo PDF no existe.")
            return None
    except Exception as e:
        print(f"❌ Error en PDF: {e}")
        return None

if __name__ == "__main__":
    qr = test_qr_generation()
    if qr:
        pdf = test_pdf_generation(qr)
        
        # Limpieza (opcional para ver los archivos)
        # os.remove(qr)
        # os.remove(pdf)
        print("\nPruebas locales completadas. Revisa las carpetas 'temp_files' y 'archivos_generados'.")
    else:
        print("Saltando prueba de PDF debido a fallo en QR.")
