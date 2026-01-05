from flask import Flask, request, jsonify, send_from_directory
import os
import segno
import resend
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from flask_cors import CORS

def generar_qr(data, nombre):
    """
    Genera un código QR y lo guarda en una carpeta temporal.
    Retorna la ruta absoluta del archivo generado.
    """
    # Directorios
    folder_path = os.path.join(os.getcwd(), "temp_files")
    os.makedirs(folder_path, exist_ok=True)
    
    file_name = f"qr_base_{nombre}.png"
    base_path = os.path.join(folder_path, file_name)

    # Generar QR
    qr = segno.make_qr(data, error='h')
    qr.save(base_path, scale=15, dark="#24d900", light="#ffffff")
    
    return base_path