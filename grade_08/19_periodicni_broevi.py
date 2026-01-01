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

class KT_2_19_Visual(TextbookScene):
    """
    Визуелизација на формулата за периодични броеви.
    Верзија 3: Поправена кирилица во Braces.
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Претворање на периодичен број", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Оригиналниот број ---
        orig_num = self.get_math(r"2{,}5\overline{14}", size=48)
        orig_label = self.get_text("Даден број:", size=24, color=MK_GRAY)
        top_group = VGroup(orig_label, orig_num).arrange(RIGHT, buff=0.2)
        top_group.move_to(UP * 2.0)

        # --- ЧЕКОР 2: Дропката ---
        
        # БРОИТЕЛ: 2514 - 25
        n1 = self.get_math("2514", size=48)
        minus = self.get_math("-", size=48)
        n2 = self.get_math("25", size=48, color=MK_BLUE)
        
        numerator = VGroup(n1, minus, n2).arrange(RIGHT, buff=0.2)
        
        # ИМЕНИТЕЛ: 990
        d1 = self.get_math("99", size=48, color=MK_RED)
        d2 = self.get_math("0", size=48, color=MK_BLUE)
        
        denominator = VGroup(d1, d2).arrange(RIGHT, buff=0.1)
        
        # Дробна црта
        line = Line(LEFT, RIGHT, color=BLACK).match_width(numerator).scale(1.1)
        
        fraction = VGroup(numerator, line, denominator).arrange(DOWN, buff=0.2)
        fraction.move_to(ORIGIN)

        # --- ЧЕКОР 3: Објаснувања (Annotations) ---

        # ЛЕВО: Објаснување за 2514
        lbl_left = self.get_text("Целиот број\n(без запирка)", size=20, color=MK_BLACK)
        lbl_left.next_to(numerator, LEFT, buff=1.5)
        arr_left = Arrow(lbl_left.get_right(), n1.get_left(), color=MK_BLACK, buff=0.1)

        # ДЕСНО: Објаснување за 25
        lbl_right = self.get_text("Делот пред\nпериодата", size=20, color=MK_BLUE)
        lbl_right.next_to(numerator, RIGHT, buff=1.5)
        arr_right = Arrow(lbl_right.get_left(), n2.get_right(), color=MK_BLUE, buff=0.1)

        # ДОЛУ: Објаснување за именителот (со Braces + Text)
        
        # За 99 (Периода)
        brace_99 = Brace(d1, DOWN, color=MK_RED)
        # КОРИСТИМЕ self.get_text НАМЕСТО brace.get_text
        text_99 = self.get_text("Цифри во периода\n(пишуваме 9)", size=16, color=MK_RED)
        text_99.next_to(brace_99, DOWN, buff=0.1)
        
        # За 0 (Претпериода)
        brace_0 = Brace(d2, DOWN, color=MK_BLUE)
        text_0 = self.get_text("Цифри пред периода\n(пишуваме 0)", size=16, color=MK_BLUE)
        # Го поместуваме малку десно и долу за да не се преклопува
        text_0.next_to(brace_0, DOWN, buff=0.1).shift(DOWN*0.4 + RIGHT*0.5)
        
        # Стрелка од текстот до заградата за 0 (за појасно)
        arrow_0 = Arrow(text_0.get_top(), brace_0.get_bottom(), color=MK_BLUE, buff=0.05).scale(0.5)

        # --- ЧЕКОР 4: Резултат ---
        final_eq = self.get_math(r"= \frac{2489}{990}", size=48)
        final_eq.next_to(fraction, RIGHT, buff=3.5)
        
        big_arrow = Arrow(fraction.get_right() + RIGHT*0.2, final_eq.get_left(), color=MK_BLACK)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(top_group)
        self.add(fraction)
        
        self.add(lbl_left, arr_left)
        self.add(lbl_right, arr_right)
        
        self.add(brace_99, text_99)
        self.add(brace_0, text_0, arrow_0)
        
        self.add(big_arrow, final_eq)