from enum import Enum
from typing import override

class TextType(Enum):
    NORMAL = "normal"
    ITALIC = "italic"
    BOLD = "bold"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text: str, text_type: Enum, url: str) -> None:
        self.text: str = text
        self.text_type: Enum = TextType(text_type)
        self.url: str = url

    @override
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    @override
    def __repr__(self) -> str:
        return(f"TextNode({self.text}, {self.text_type.value}, {self.url})")
