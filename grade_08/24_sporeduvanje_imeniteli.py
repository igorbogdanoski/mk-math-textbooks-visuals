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
# ТЕМА: Споредување со исти именители
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

class KT_2_24_Visual(TextbookScene):
    """
    Визуелизација: Споредување со исти именители.
    a=11/10, b=101/100, c=1001/1000 -> Сите во xx/1000
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Споредување со исти именители", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Оригинални дропки ---
        eq_a = self.get_math(r"a = \frac{11}{10}", size=48)
        eq_b = self.get_math(r"b = \frac{101}{100}", size=48)
        eq_c = self.get_math(r"c = \frac{1001}{1000}", size=48)
        
        originals = VGroup(eq_a, eq_b, eq_c).arrange(RIGHT, buff=1.5)
        originals.move_to(UP * 2.5)

        # --- ЧЕКОР 2: Трансформација (Стрелки надолу) ---
        arrow_a = Arrow(UP, DOWN, color=MK_GRAY).next_to(eq_a, DOWN, buff=0.1)
        label_a = self.get_text("x100", size=20, color=MK_RED).next_to(arrow_a, RIGHT, buff=0.1)
        
        arrow_b = Arrow(UP, DOWN, color=MK_GRAY).next_to(eq_b, DOWN, buff=0.1)
        label_b = self.get_text("x10", size=20, color=MK_RED).next_to(arrow_b, RIGHT, buff=0.1)
        
        arrow_c = Arrow(UP, DOWN, color=MK_GRAY).next_to(eq_c, DOWN, buff=0.1)
        label_c = self.get_text("x1", size=20, color=MK_RED).next_to(arrow_c, RIGHT, buff=0.1)

        # --- ЧЕКОР 3: Нови дропки (Ист именител 1000) ---
        new_a = self.get_math(r"a = \frac{1100}{1000}", size=48)
        new_a.next_to(arrow_a, DOWN, buff=0.1)
        
        new_b = self.get_math(r"b = \frac{1010}{1000}", size=48)
        new_b.next_to(arrow_b, DOWN, buff=0.1)
        
        new_c = self.get_math(r"c = \frac{1001}{1000}", size=48)
        new_c.next_to(arrow_c, DOWN, buff=0.1)

        # Боење
        # Броители (Сино) - тие се различни
        new_a[0][2:6].set_color(MK_BLUE)
        new_b[0][2:6].set_color(MK_BLUE)
        new_c[0][2:6].set_color(MK_BLUE)
        
        # Именители (Црвено) - тие се исти
        new_a[0][7:].set_color(MK_RED)
        new_b[0][7:].set_color(MK_RED)
        new_c[0][7:].set_color(MK_RED)

        new_fractions_group = VGroup(new_a, new_b, new_c)

        # --- ЧЕКОР 4: Споредба ---
        
        # 1001 < 1010 < 1100
        comp_num = self.get_math(r"1001 < 1010 < 1100", size=42, color=MK_BLUE)
        comp_num.next_to(new_fractions_group, DOWN, buff=0.5)
        
        # Текст за правилото
        rule_text = self.get_text("Поголем броител = Поголема дропка", size=24, color=MK_BLACK)
        rule_text.next_to(comp_num, DOWN, buff=0.3)
        
        # Финален заклучок
        final_res = self.get_math(r"c < b < a", size=60, color=MK_BLACK)
        final_box = SurroundingRectangle(final_res, color=MK_BLACK, buff=0.3)
        final_group = VGroup(final_box, final_res).next_to(rule_text, DOWN, buff=0.5)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(originals)
        self.add(arrow_a, label_a, arrow_b, label_b, arrow_c, label_c)
        self.add(new_a, new_b, new_c)
        self.add(comp_num, rule_text)
        self.add(final_group)