"""Демонстратор стратегии: автоматический выбор стратегии."""

from abc import ABC, abstractmethod
from pathlib import Path
# from typing import Self


class ImageDecoder(ABC):
    @staticmethod
    @abstractmethod
    def decode(path_to_image: str):
        pass


class PNGDecoder(ImageDecoder):
    @staticmethod
    def decode(path_to_image: str):
        return 'PNG Image'


class JPEGDecoder(ImageDecoder):
    @staticmethod
    def decode(path_to_image: str):
        return 'JPEG Image'


class TIFFDecoder(ImageDecoder):
    @staticmethod
    def decode(path_to_image: str):
        return 'TIFF Image'


class Image:
    @classmethod
    # def open(cls, image_path: str | Path) -> Self:
    def open(cls, image_path: str | Path):
        ext = Path(image_path).suffix
        match ext.lower():
            case '.png':
                decoder = PNGDecoder
            case '.jpg' | '.jpeg':
                decoder = JPEGDecoder
            case '.tiff':
                decoder = TIFFDecoder
            case _:
                raise ValueError(f"couldn't open {ext} type")
        byterange = decoder.decode(image_path)
        return cls(byterange)

    def __init__(self, byterange):
        self._byterange = byterange

    def __str__(self):
        return f'{self._byterange}'


pic1 = 'image1.png'
pic2 = 'image2.jpg'
pic3 = 'image3.tiff'

print(Image.open(pic2))
print(Image.open(pic3))
print(Image.open(pic1))
