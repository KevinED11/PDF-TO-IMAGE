from pdf2image import convert_from_path
from enum import StrEnum, IntEnum
from pathlib import Path
from PIL import Image


class Format(StrEnum):
    PNG = "PNG"
    JPEG = "JPEG"


class DPIQuality(IntEnum):
    DPI_300 = 300
    DEFAULT_DPI_200 = 200


# Ruta del archivo PDF
pdf_path = Path(
    "/home/kevind/Documentos/datos-personales/firmas_autografas/firma-autografa-digit.pdf"
)

# Convertir PDF a una lista de imágenes
images = convert_from_path(pdf_path=str(pdf_path), dpi=DPIQuality.DPI_300)

# Guardar cada página del PDF como una imagen PNG
for i, image in enumerate(images):
    image.save(f"pagina_{i + 1}.{Format.PNG}", format=Format.PNG)

new_image = Image.open("pagina_1.PNG").convert("RGBA")
data_image = new_image.getdata()


class Channel(IntEnum):
    R = 0
    G = 1
    B = 2
    A = 3


TRANSPARENT_PIXEL = (255, 255, 255, 0)
new_data_image = []

for pixel in data_image:
    if (
        pixel[Channel.R] > 200
        and pixel[Channel.G] > 200
        and pixel[Channel.B] > 200
        and pixel[Channel.A] > 0
    ):
        new_data_image += [TRANSPARENT_PIXEL]
        continue

    new_data_image += [pixel]

new_image.putdata(new_data_image)
new_image.save("pagina_1_transparent.PNG", format=Format.PNG)
