from manim import *

# --- ГЛОБАЛНИ ПОДЕСУВАЊА ЗА КНИГИ ---
config.background_color = WHITE
config.frame_width = 14
config.pixel_height = 1080
config.pixel_width = 1920

# --- БОИ (Прилагодени за печатење/бела позадина) ---
MK_BLUE = "#0055D4"
MK_RED = "#D40000"
MK_BLACK = "#000000"
MK_GRAY = "#555555"

class TextbookScene(Scene):
    """
    Основна класа за сите лекции.
    """
    def construct(self):
        pass

    def get_text(self, text_str, color=MK_BLACK, size=24, is_bold=False):
        # Користиме sans-serif фонт кој обично има добра кирилица
        font_weight = "BOLD" if is_bold else "NORMAL"
        return Text(
            text_str, 
            font="Arial",  # Или "Segoe UI" на Windows
            color=color, 
            font_size=size, 
            weight=font_weight
        )

    def get_math(self, tex_str, color=MK_BLACK, size=48):
        return MathTex(tex_str, color=color, font_size=size)