import os
import resend

def enviar_correo(nombre_original, correo_destino, pdf_path, qr_path):
    """
    Envía un correo electrónico con los archivos PDF e imagen QR adjuntos usando Resend.
    """
    resend.api_key = os.getenv("RESEND_API_KEY")
    if not resend.api_key:
        raise ValueError("RESEND_API_KEY no está configurada en las variables de entorno.")

    nombre = nombre_original.replace(" ", "_")

    # Leemos los archivos para adjuntar
    with open(pdf_path, "rb") as f:
        pdf_data = list(f.read())
    with open(qr_path, "rb") as f:
        image_data = list(f.read())

    params = {
        "from": "Arturo Maldonado <noreply@arturomaldonadoportafolio.space>",
        "to": correo_destino,
        "subject": "Tu Código QR solicitado",
        "html": f"""
            <h3>¡Hola {nombre_original}!</h3>
            <p>Adjunto encontrarás el código QR en formato imagen y el documento PDF que generaste.</p>
            <p>Saludos,<br>Arturo Maldonado</p>
        """,
        "attachments": [
            {
                "filename": f"qr_pdf_{nombre}.pdf",
                "content": pdf_data,
            },
            {
                "filename": f"qr_imagen_{nombre}.png",
                "content": image_data,
            }
        ]
    }

    return resend.Emails.send(params)