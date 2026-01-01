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
    SurroundingRectangle, DashedLine, Brace,  # <--- ДОДАДЕНО Е BRACE
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN
)

# ==========================================
# ТЕМА: Претворање децимален број во дропка
# ==========================================

class KT_2_17_Visual(TextbookScene):
    """
    Визуелизација на конверзија: 4,75 -> 475/100 -> 19/4
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Претворање децимален број во дропка", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Оригиналниот број ---
        decimal_num = self.get_math("4{,}75", size=60)
        decimal_num.move_to(UP * 1.5)
        
        # Означување на децималите
        # decimal_num[0] е целиот израз. [2:] се цифрите после запирката (7 и 5)
        brace = Brace(decimal_num[0][2:], direction=UP, color=MK_BLUE)
        brace_text = self.get_text("2 децимални места", size=24, color=MK_BLUE).next_to(brace, UP)

        # --- ЧЕКОР 2: Конверзија во дропка ---
        # Стрелка надолу
        arrow = Arrow(UP, DOWN, color=MK_BLACK).next_to(decimal_num, DOWN, buff=0.5)
        
        # Дропка 475/100 (Визуелна конструкција за да ги обоиме нулите)
        
        # Броител
        num_tex = self.get_math("475", size=60)
        
        # Именител (1 и 00)
        denom_1 = self.get_math("1", size=60)
        denom_00 = self.get_math("00", size=60, color=MK_BLUE) # Нулите сини
        denom_group = VGroup(denom_1, denom_00).arrange(RIGHT, buff=0.1)
        
        # Линија за дропка
        frac_line = Line(LEFT, RIGHT, color=BLACK, stroke_width=4).match_width(VGroup(num_tex, denom_group)).scale(1.1)
        
        # Групирање на дропката
        fraction_visual = VGroup(num_tex, frac_line, denom_group).arrange(DOWN, buff=0.2)
        fraction_visual.next_to(arrow, DOWN, buff=0.5)

        # Текст за нулите
        zeros_text = self.get_text("2 нули", size=24, color=MK_BLUE)
        zeros_text.next_to(denom_00, RIGHT, buff=0.5)
        zeros_arrow = Arrow(zeros_text.get_left(), denom_00.get_right(), color=MK_BLUE, buff=0.1)

        # --- ЧЕКОР 3: Кратење ---
        # Стрелка десно
        arrow_right = Arrow(LEFT, RIGHT, color=MK_BLACK).next_to(fraction_visual, RIGHT, buff=2.0)
        div_text = self.get_math(r":25", size=28, color=MK_RED).next_to(arrow_right, UP)
        
        # Финална дропка 19/4
        final_fraction = self.get_math(r"\frac{19}{4}", size=60, color=MK_RED).next_to(arrow_right, RIGHT)
        
        # Рамка
        box = SurroundingRectangle(final_fraction, color=MK_RED, buff=0.2)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(decimal_num, brace, brace_text)
        self.add(arrow)
        self.add(fraction_visual, zeros_text, zeros_arrow)
        self.add(arrow_right, div_text, final_fraction, box)