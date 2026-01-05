import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

def generar_pdf(nombre, qr_path):
    """
    Crea un documento PDF con la imagen del QR adjunta.
    Retorna la ruta absoluta del PDF generado (en /tmp para Vercel).
    """

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(200, 10, text="Su link esta listo",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    if os.path.exists(qr_path):
        pdf.image(qr_path, x=50, y=50, w=100)

    # Directorio temporal válido en Vercel
    folder_temp = "/tmp"

    file_name = f"qr_pdf_{nombre}.pdf"
    output_filename = os.path.join(folder_temp, file_name)

    pdf.output(output_filename)

    return output_filename
