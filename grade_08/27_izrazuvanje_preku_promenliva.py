import sys
import os

# --- 1. SETUP PATH ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# --- 2. IMPORTS ---
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN
from manim import (
    Scene, VGroup, MathTex, Text, NumberLine, Line, Arrow, Dot, Circle, 
    SurroundingRectangle, DashedLine, Brace,
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN
)

class KT_2_27_Visual(TextbookScene):
    """
    Визуелизација: x = 1 + A
    КОРЕКЦИЈА: Компактен распоред за да се гледа целиот израз.
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Изразување преку променлива", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Дефиниција на A (Креваме повисоко) ---
        eq_A = self.get_math(r"A = \frac{1}{53} + \frac{1}{71} - \frac{1}{89}", size=42, color=MK_BLUE)
        # КОРЕКЦИЈА: UP * 2.5 наместо 2.0
        eq_A.move_to(UP * 2.5)
        
        box_A = SurroundingRectangle(eq_A, color=MK_BLUE, buff=0.2)
        label_A = self.get_text("Дадено", size=20, color=MK_BLUE).next_to(box_A, LEFT)

        # --- ЧЕКОР 2: Бараниот израз x ---
        eq_x = self.get_math(r"x = \frac{54}{53} + \frac{72}{71} - \frac{90}{89}", size=42)
        # КОРЕКЦИЈА: Намален buff од 1.0 на 0.7
        eq_x.next_to(eq_A, DOWN, buff=0.7)

        # --- ЧЕКОР 3: Разложување ---
        decomp_1 = self.get_math(r"\left(1 + \frac{1}{53}\right)", size=42)
        plus_1 = self.get_math("+", size=42)
        decomp_2 = self.get_math(r"\left(1 + \frac{1}{71}\right)", size=42)
        minus_1 = self.get_math("-", size=42)
        decomp_3 = self.get_math(r"\left(1 + \frac{1}{89}\right)", size=42)
        
        decomp_line = VGroup(decomp_1, plus_1, decomp_2, minus_1, decomp_3).arrange(RIGHT, buff=0.2)
        # КОРЕКЦИЈА: Намален buff од 1.0 на 0.8
        decomp_line.next_to(eq_x, DOWN, buff=0.8)
        
        # Стрелки (Подесени за новиот распоред)
        arrow_1 = Arrow(eq_x[0][2:6].get_bottom(), decomp_1.get_top(), color=MK_GRAY, buff=0.1, stroke_width=3)
        arrow_2 = Arrow(eq_x[0][7:11].get_bottom(), decomp_2.get_top(), color=MK_GRAY, buff=0.1, stroke_width=3)
        arrow_3 = Arrow(eq_x[0][12:].get_bottom(), decomp_3.get_top(), color=MK_GRAY, buff=0.1, stroke_width=3)

        # --- ЧЕКОР 4: Групирање ---
        integers = self.get_math(r"(1 + 1 - 1)", size=42, color=MK_RED)
        
        fractions = self.get_math(r"+ \left(\frac{1}{53} + \frac{1}{71} - \frac{1}{89}\right)", size=42)
        fractions[0][2:].set_color(MK_BLUE)
        
        final_line = VGroup(integers, fractions).arrange(RIGHT, buff=0.2)
        # КОРЕКЦИЈА: Намален buff од 0.8 на 0.6
        final_line.next_to(decomp_line, DOWN, buff=0.6)
        
        brace_A = Brace(fractions[0][2:], DOWN, color=MK_BLUE)
        text_A = self.get_math("= A", size=36, color=MK_BLUE).next_to(brace_A, DOWN, buff=0.1)

        # --- ЧЕКОР 5: Резултат ---
        result = self.get_math("x = 1 + A", size=60, color=MK_BLACK)
        result_box = SurroundingRectangle(result, color=MK_RED, buff=0.2)
        
        # Го ставаме резултатот лево од Brace-от за да заштедиме вертикален простор
        # или малку подолу ако има место. Со новите подесувања ќе има место долу.
        result_group = VGroup(result_box, result)
        result_group.next_to(text_A, DOWN, buff=0.4)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(eq_A, box_A, label_A)
        self.add(eq_x)
        self.add(arrow_1, arrow_2, arrow_3)
        self.add(decomp_line)
        self.add(final_line)
        self.add(brace_A, text_A)
        self.add(result_group)