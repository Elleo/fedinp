import textwrap
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

class Display:

    def __init__(self, *args, **kwargs):
        options = RGBMatrixOptions()
        options.hardware_mapping = "adafruit-hat"
        options.rows = 32
        options.cols = 64
        options.gpio_slowdown = 5
        options.brightness = 50
        self.matrix = RGBMatrix(options = options)
        self.font = graphics.Font()
        self.font.LoadFont("fonts/4x6.bdf") # tom-thumb.bdf")
        self.palette = [graphics.Color(0x33, 0x66, 0xbb), graphics.Color(0xaa, 0x33, 0x55), graphics.Color(0xee, 0xdd, 0), graphics.Color(0xee, 0xdd, 0), graphics.Color(0xee, 0xdd, 0)]

    def show_text(self, text):
        self.matrix.Clear()
        lines = textwrap.wrap(text, 16)
        line_num = 1
        for line in lines[-5:]:
            x = int((64 - len(line) * 4) / 2) + 1 # center
            graphics.DrawText(self.matrix, self.font, x, line_num * 8 - 2, self.palette[line_num - 1], line)
            line_num += 1
