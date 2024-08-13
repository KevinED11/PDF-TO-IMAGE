from pdf2image import convert_from_path
from enum import StrEnum, IntEnum
from pathlib import Path


class Format(StrEnum):
    PNG = "PNG"
    JPEG = "JPEG"


class DPIQuality(IntEnum):
    DPI_300 = 300
    DEFAULT_DPI_200 = 200


# Ruta del archivo PDF
pdf_path = Path("/home/kevind/Documentos/datos-personales/firma-autografa-digit.pdf")
# Opciones para alta calidad
DPI = 300  # Resolución en puntos por pulgada

# Convertir PDF a una lista de imágenes
images = convert_from_path(pdf_path=str(pdf_path), dpi=DPIQuality.DPI_300)

# Guardar cada página del PDF como una imagen PNG
[
    image.save(f"pagina_{i + 1}.{Format.PNG}", format=Format.PNG)
    for i, image in enumerate(images)
]
