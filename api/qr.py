import os
import segno

def generar_qr(data, nombre):
    """
    Genera un código QR y lo guarda en /tmp (permitido en Vercel).
    """

    folder_path = "/tmp"   # directorio temporal permitido
    
    file_name = f"qr_base_{nombre}.png"
    base_path = os.path.join(folder_path, file_name)

    qr = segno.make_qr(data, error='h')
    qr.save(base_path, scale=15, dark="#24d900", light="#ffffff")

    return base_path
