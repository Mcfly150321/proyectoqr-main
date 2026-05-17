let qrCode = null;

document.addEventListener('DOMContentLoaded', () => {
    // Inputs
    const urlInput = document.getElementById('url_qr');
    const dotsShape = document.getElementById('dots_shape');
    const cornersShape = document.getElementById('corners_shape');
    const cornersDotShape = document.getElementById('corners_dot_shape');
    const colorQr1 = document.getElementById('color_qr_1');
    const colorQr2 = document.getElementById('color_qr_2');
    const bgColor = document.getElementById('bg_color');
    const qrSize = document.getElementById('qr_size');
    const btnDescargar = document.getElementById('btnDescargar');

    function getOptions(size = 300) {
        const data = urlInput.value || "https://ejemplo.com";
        const dots = dotsShape.value;
        const corners = cornersShape.value;
        const cornersDot = cornersDotShape.value;
        const c1 = colorQr1.value;
        const c2 = colorQr2.value;
        const bg = bgColor.value;

        return {
            width: size,
            height: size,
            type: "svg",
            data: data,
            margin: Math.floor(size * 0.05), // margen proporcional al 5%
            dotsOptions: {
                type: dots,
                gradient: {
                    type: 'linear',
                    rotation: Math.PI / 4,
                    colorStops: [{ offset: 0, color: c1 }, { offset: 1, color: c2 }]
                }
            },
            backgroundOptions: {
                color: bg
            },
            cornersSquareOptions: {
                type: corners,
                gradient: {
                    type: 'linear',
                    rotation: Math.PI / 4,
                    colorStops: [{ offset: 0, color: c1 }, { offset: 1, color: c2 }]
                }
            },
            cornersDotOptions: {
                type: cornersDot,
                gradient: {
                    type: 'linear',
                    rotation: Math.PI / 4,
                    colorStops: [{ offset: 0, color: c1 }, { offset: 1, color: c2 }]
                }
            }
        };
    }

    function updateQR() {
        const options = getOptions(300);

        if (!qrCode) {
            qrCode = new QRCodeStyling(options);
            document.getElementById("canvas").innerHTML = "";
            qrCode.append(document.getElementById("canvas"));
        } else {
            qrCode.update(options);
        }
    }

    // Listeners
    const inputs = [urlInput, dotsShape, cornersShape, cornersDotShape, colorQr1, colorQr2, bgColor, qrSize];
    inputs.forEach(input => {
        input.addEventListener('input', updateQR);
        input.addEventListener('change', updateQR);
    });

    btnDescargar.addEventListener('click', () => {
        const size = parseInt(qrSize.value) || 1000;
        
        // Generamos una instancia de alta resolución separada
        const downloadOptions = getOptions(size);
        const tempQrCode = new QRCodeStyling(downloadOptions);
        
        // Descargar forzando resolución limpia
        tempQrCode.download({ name: "mi_qr_personalizado", extension: "png" });
    });

    // Initial render
    updateQR();

    // Trigger animations for panels
    const panels = document.querySelectorAll('.card');
    panels.forEach((panel, index) => {
        panel.style.opacity = '0';
        panel.style.transform = 'translateY(20px)';
        panel.style.transition = `all 0.8s ease-out ${index * 0.2}s`;
        
        setTimeout(() => {
            panel.style.opacity = '1';
            panel.style.transform = 'translateY(0)';
        }, 100);
    });
});
