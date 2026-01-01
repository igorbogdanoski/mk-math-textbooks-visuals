import sys
import os

# --- 1. SETUP PATH ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# --- 2. IMPORTS ---
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE
from manim import (
    Scene, VGroup, MathTex, Text, NumberLine, Line, Arrow, Dot, Circle, 
    SurroundingRectangle, DashedLine, Brace,
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN,
    FadeOut, Write, Create, Indicate, TransformFromCopy, Wait
)

# ==========================================
# ТЕМА: Полиномно делење
# ==========================================

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

class KT_2_28_Visual(TextbookScene):
    """
    Визуелизација на полиномно делење: (3x+1) : (x-1)
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Полиномно делење", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ПОСТАВКА НА ДЕЛЕЊЕТО ---
        # Користиме класичен распоред за делење
        #   3x + 1 | x - 1
        #          |-------
        #            3
        
        dividend = self.get_math("3x + 1", size=48)
        divisor = self.get_math("x - 1", size=48)
        
        # Вертикална линија
        v_line = Line(UP, DOWN, color=BLACK).scale(0.8)
        # Хоризонтална линија (за под делителот)
        h_line = Line(LEFT, RIGHT, color=BLACK).match_width(divisor).scale(1.2)
        
        # Позиционирање
        v_line.move_to(UP * 1.0)
        dividend.next_to(v_line, LEFT, buff=0.2)
        divisor.next_to(v_line, RIGHT, buff=0.2).align_to(dividend, UP)
        h_line.next_to(divisor, DOWN, buff=0.1)
        
        setup_group = VGroup(dividend, v_line, divisor, h_line)
        setup_group.move_to(UP * 1.5)

        # --- ЧЕКОР 1: Наоѓање на количникот ---
        # 3x : x = 3
        quotient = self.get_math("3", size=48, color=MK_BLUE)
        quotient.next_to(h_line, DOWN, buff=0.1)
        
        # Стрелка за објаснување
        arrow_div = Arrow(dividend[0][0:2].get_top(), quotient.get_left(), color=MK_BLUE, path_arc=1.0, stroke_width=2)
        label_div = self.get_text("3x : x = 3", size=18, color=MK_BLUE).next_to(arrow_div, UP)

        # --- ЧЕКОР 2: Множење ---
        # 3 * (x-1) = 3x - 3
        product = self.get_math("3x - 3", size=48)
        product.next_to(dividend, DOWN, buff=0.8).align_to(dividend, RIGHT)
        
        # Знак минус (за одземање)
        minus_sign = self.get_math("-", size=48, color=MK_RED).next_to(product, LEFT, buff=0.2)
        
        # Линија за одземање
        sub_line = Line(LEFT, RIGHT, color=BLACK).match_width(product).scale(1.2)
        sub_line.next_to(product, DOWN, buff=0.1)

        # --- ЧЕКОР 3: Остаток ---
        # (3x+1) - (3x-3) = 4
        remainder = self.get_math("4", size=48, color=MK_RED)
        remainder.next_to(sub_line, DOWN, buff=0.2).align_to(product, RIGHT)
        
        # Ознака за остаток
        label_rem = self.get_text("Остаток", size=20, color=MK_RED).next_to(remainder, RIGHT, buff=0.5)
        arrow_rem = Arrow(label_rem.get_left(), remainder.get_right(), color=MK_RED)

        # --- ЧЕКОР 4: Финален запис ---
        final_eq = self.get_math(r"\frac{3x+1}{x-1} = 3 + \frac{4}{x-1}", size=48)
        final_box = SurroundingRectangle(final_eq, color=MK_BLACK, buff=0.2)
        final_group = VGroup(final_box, final_eq).move_to(DOWN * 2.5)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(setup_group)
        self.add(quotient, arrow_div, label_div)
        self.add(product, minus_sign, sub_line)
        self.add(remainder, label_rem, arrow_rem)
        self.add(final_group)