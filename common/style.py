from manim import *

# --- ГЛОБАЛНИ ПОДЕСУВАЊА ---
config.background_color = WHITE
config.frame_width = 14
config.pixel_height = 1080
config.pixel_width = 1920

# --- БОИ ---
MK_BLUE = "#0055D4"
MK_RED = "#D40000"
MK_BLACK = "#000000"
MK_GRAY = "#555555"
MK_GREEN = "#228B22"   # Forest Green - одлична за точни одговори
MK_ORANGE = "#ED8121"  # Стандардна Manim портокалова за истакнување

class TextbookScene(Scene):
    """
    Основна класа за сите лекции.
    """
    def construct(self):
        pass

    def get_text(self, text_str, color=MK_BLACK, size=24, is_bold=False):
        """
        Креира текст објект кој поддржува кирилица (користи Arial).
        """
        font_weight = "BOLD" if is_bold else "NORMAL"
        return Text(
            text_str, 
            font="Arial", 
            color=color, 
            font_size=size, 
            weight=font_weight
        )

    def get_math(self, tex_str, color=MK_BLACK, size=48):
        """
        Креира математичка формула (LaTeX).
        """
        return MathTex(
            tex_str, 
            color=color, 
            font_size=size
        )