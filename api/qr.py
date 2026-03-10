import os
import segno

def generar_qr(data, nombre, hex_color="#000000"):
    """
    Genera un código QR con un color personalizado y lo guarda en /tmp.
    """

    folder_path = "/tmp"   # directorio temporal permitido
    
    file_name = f"qr_base_{nombre}.png"
    base_path = os.path.join(folder_path, file_name)

    qr = segno.make_qr(data, error='h')
    qr.save(base_path, scale=15, dark=hex_color, light="#ffffff")

    return base_path
