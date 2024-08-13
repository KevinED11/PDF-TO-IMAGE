from pdf2image import convert_from_path
from enum import StrEnum, IntEnum
from pathlib import Path
from PIL import Image, ImageFile


class Format(StrEnum):
    PNG = "PNG"
    JPEG = "JPEG"


class ColorFormat(StrEnum):
    RGB = "RGB"
    RGBA = "RGBA"


class Channel(IntEnum):
    R = 0
    G = 1
    B = 2
    A = 3


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


def get_image(file_name: str) -> ImageFile:
    return Image.open(file_name)


def get_images(files_names: list[str]) -> list[ImageFile]:
    return [get_image(file_name) for file_name in files_names]


def convert_image(image_file: ImageFile, color_format: ColorFormat) -> Image:
    return image_file.convert(color_format)


def convert_images(images: list[ImageFile], color_format: ColorFormat) -> list[Image]:
    return [convert_image(image_file, color_format) for image_file in images]


def get_image_data(image_file: ImageFile) -> list:
    return image_file.getdata()


def get_images_data(image_files: list[ImageFile]) -> list[list]:
    return [get_image_data(image_file) for image_file in image_files]


FILE_NAME = "pagina_1.PNG"
FILES_NAMES = [FILE_NAME]
new_image: Image = Image.open(FILE_NAME).convert(ColorFormat.RGBA)
NEW_IMAGES = [new_image]
data_image = new_image.getdata()
DATA_IMAGES = [data_image]


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
