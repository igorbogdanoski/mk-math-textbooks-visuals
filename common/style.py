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
MK_GREEN = "#228B22"
MK_ORANGE = "#ED8121"

# --- LATEX КОНФИГУРАЦИЈА (БЕЗБЕДНА) ---

# Unicode-compatible LaTeX template for Cyrillic (XeLaTeX)
my_template = TexTemplate()
my_template.tex_compiler = "xelatex"
my_template.output_format = ".xdv"
my_template.add_to_preamble(r"\usepackage{amsmath}")
my_template.add_to_preamble(r"\usepackage{amssymb}")
my_template.add_to_preamble(r"\usepackage{xcolor}")  # За бои
my_template.add_to_preamble(r"\usepackage{fontspec}")
my_template.add_to_preamble(r"\setmainfont{Arial}")  # Arial supports Cyrillic

class TextbookScene(Scene):
    """
    Основна класа за сите лекции.
    """
    def construct(self):
        pass

    def get_text(self, text_str, color=MK_BLACK, size=24, is_bold=False):
        # За кирилица користиме Text() со Arial, тоа работи без LaTeX
        font_weight = "BOLD" if is_bold else "NORMAL"
        return Text(
            text_str, 
            font="Arial", 
            color=color, 
            font_size=size, 
            weight=font_weight
        )

    def get_math(self, tex_str, color=MK_BLACK, size=48):
        # За формули користиме MathTex со нашиот темплејт
        return MathTex(
            tex_str, 
            color=color, 
            font_size=size,
            tex_template=my_template
        )