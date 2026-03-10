import os
import resend

def enviar_correo(nombre_original, correo_destino, pdf_path, qr_path, url_para_qr):
    """
    Envía un correo al usuario y una notificación al administrador.
    """
    resend.api_key = os.getenv("RESEND_API_KEY")
    if not resend.api_key:
        raise ValueError("RESEND_API_KEY no está configurada.")

    nombre = nombre_original.replace(" ", "_")

    # Leemos los archivos para adjuntar
    with open(pdf_path, "rb") as f:
        pdf_data = list(f.read())
    with open(qr_path, "rb") as f:
        image_data = list(f.read())

    # 1. Correo para el Usuario
    params_user = {
        "from": "Arturo Maldonado <noreply@arturomaldonado.space>",
        "to": correo_destino,
        "subject": "Tu Código QR solicitado",
        "html": f"""
            <h3>¡Hola {nombre_original}!</h3>
            <p>Adjunto encontrarás el código QR en formato imagen y el documento PDF que generaste.</p>
            <p>Saludos,<br>Arturo Maldonado</p>
        """,
        "attachments": [
            {"filename": f"qr_pdf_{nombre}.pdf", "content": pdf_data},
            {"filename": f"qr_imagen_{nombre}.png", "content": image_data}
        ]
    }
    resend.Emails.send(params_user)

    # 2. Correo para el Administrador
    params_admin = {
        "from": "Sistema QR <noreply@arturomaldonado.space>",
        "to": "20arturomaldonado@umes.edu.gt",
        "subject": f"Nuevo QR: {nombre_original}",
        "html": f"""
            <h3>Aviso de generación de QR</h3>
            <p><strong>Usuario:</strong> {nombre_original}</p>
            <p><strong>Correo:</strong> {correo_destino}</p>
            <p><strong>Enlace/Texto:</strong> {url_para_qr}</p>
        """
    }
    return resend.Emails.send(params_admin)