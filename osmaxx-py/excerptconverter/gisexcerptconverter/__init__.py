from excerptconverter.baseexcerptconverter import BaseExcerptConverter
from .gis_excerpt_converter import GisExcerptConverter

BaseExcerptConverter.available_converters.append(GisExcerptConverter)
