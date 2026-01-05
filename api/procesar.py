import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Importar módulos locales
from api.qr import generar_qr
from api.pdf import generar_pdf
from api.mail import enviar_correo

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route('/procesar', methods=['POST'])
def procesar():
    qr_path = None
    pdf_path = None
    try:
        # 1. Recibir datos
        datos = request.json
        nombre_original = datos.get('nombre')
        correo = datos.get('correo')
        url_para_qr = datos.get('url_qr')

        if not all([nombre_original, correo, url_para_qr]):
            return jsonify({"status": "error", "message": "Faltan datos requeridos"}), 400

        nombre_limpio = nombre_original.replace(" ", "_")

        # 2. Generar QR
        qr_path = generar_qr(url_para_qr, nombre_limpio)

        # 3. Generar PDF
        pdf_path = generar_pdf(nombre_limpio, qr_path)

        # 4. Enviar Correo
        enviar_correo(nombre_original, correo, pdf_path, qr_path)

        print(f"✅ Éxito: Procesado para {nombre_original}")
        return jsonify({"status": "ok", "message": "Proceso completado"}), 200

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500
    
    finally:
        # Limpieza de archivos temporales
        if qr_path and os.path.exists(qr_path):
            os.remove(qr_path)
        if pdf_path and os.path.exists(pdf_path):
            os.remove(pdf_path)

if __name__ == '__main__':
    # Asegurarse de que el puerto sea el correcto (5000 por defecto en Flask)
    app.run(host='0.0.0.0', port=5000, debug=True)
