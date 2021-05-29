from PIL import Image, ImageDraw, ImageFont

def is_hebrew(st):
    if len(st) == 0:
        return False
    if len(st) == 1:
        return "\u0590" <= st <= "\u05EA"
    return any(is_hebrew(ch) for ch in st)

class AnimText:
    def __init__(
        self,
        text: str,
        *,
        x: int = 0,
        y: int = 0,
        font_path: str = None,
        font_size: int = 12,
        typewriter_effect: bool = False,
        colour: str = "#ffffff",
    ):
        self.x = x
        self.y = y
        self.text = text
        self.typewriter_effect = typewriter_effect
        self.font_path = font_path
        self.font_size = font_size
        self.colour = colour
        self.is_hebrew = is_hebrew(self.text)

    def render(self, background: Image, frame: int = 0):
        draw = ImageDraw.Draw(background)
        _text = self.text
        if self.typewriter_effect:
            _text = _text[:frame]
        if self.font_path is not None:
            font = ImageFont.truetype(self.font_path, self.font_size)
            hebrew_args = dict(language='he',allign="right",direction="rtl") if self.is_hebrew else dict()
            draw.text((self.x, self.y), _text, font=font, fill=self.colour,**hebrew_args)
        else:
            draw.text((self.x, self.y), _text, fill=self.colour)
        return background

    def __str__(self):
        return self.text
