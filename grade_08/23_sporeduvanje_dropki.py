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

class KT_2_23_Visual(TextbookScene):
    """
    Визуелизација: Споредување со исти броители.
    КОРЕКЦИЈА: Подигнато нагоре за да се гледа финалното решение.
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Споредување со исти броители", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Оригинални дропки (Креваме повисоко: UP * 2.5) ---
        eq_a = self.get_math(r"a = \frac{3}{11}", size=48)
        eq_b = self.get_math(r"b = \frac{4}{15}", size=48)
        eq_c = self.get_math(r"c = \frac{6}{23}", size=48)
        
        originals = VGroup(eq_a, eq_b, eq_c).arrange(RIGHT, buff=1.5)
        originals.move_to(UP * 2.5)

        # --- ЧЕКОР 2: Трансформација ---
        arrow_a = Arrow(UP, DOWN, color=MK_GRAY).next_to(eq_a, DOWN, buff=0.1)
        label_a = self.get_text("x4", size=20, color=MK_BLUE).next_to(arrow_a, RIGHT, buff=0.1)
        
        arrow_b = Arrow(UP, DOWN, color=MK_GRAY).next_to(eq_b, DOWN, buff=0.1)
        label_b = self.get_text("x3", size=20, color=MK_BLUE).next_to(arrow_b, RIGHT, buff=0.1)
        
        arrow_c = Arrow(UP, DOWN, color=MK_GRAY).next_to(eq_c, DOWN, buff=0.1)
        label_c = self.get_text("x2", size=20, color=MK_BLUE).next_to(arrow_c, RIGHT, buff=0.1)

        # --- ЧЕКОР 3: Нови дропки ---
        new_a = self.get_math(r"a = \frac{12}{44}", size=48)
        new_a.next_to(arrow_a, DOWN, buff=0.1)
        
        new_b = self.get_math(r"b = \frac{12}{45}", size=48)
        new_b.next_to(arrow_b, DOWN, buff=0.1)
        
        new_c = self.get_math(r"c = \frac{12}{46}", size=48)
        new_c.next_to(arrow_c, DOWN, buff=0.1)

        # Боење
        new_a[0][2:4].set_color(MK_BLUE)
        new_b[0][2:4].set_color(MK_BLUE)
        new_c[0][2:4].set_color(MK_BLUE)
        
        new_a[0][5:].set_color(MK_RED)
        new_b[0][5:].set_color(MK_RED)
        new_c[0][5:].set_color(MK_RED)

        new_fractions_group = VGroup(new_a, new_b, new_c)

        # --- ЧЕКОР 4: Споредба ---
        
        # 46 > 45 > 44
        comp_denom = self.get_math(r"46 > 45 > 44", size=42, color=MK_RED)
        # Намален buff за да собере сè
        comp_denom.next_to(new_fractions_group, DOWN, buff=0.5)
        
        # Текст за правилото
        rule_text = self.get_text("Поголем именител = Помала дропка", size=24, color=MK_BLACK)
        rule_text.next_to(comp_denom, DOWN, buff=0.3)
        
        # Финален заклучок (Сега ќе биде видлив)
        final_res = self.get_math(r"c < b < a", size=60, color=MK_BLACK)
        final_box = SurroundingRectangle(final_res, color=MK_BLACK, buff=0.3)
        final_group = VGroup(final_box, final_res).next_to(rule_text, DOWN, buff=0.5)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(originals)
        self.add(arrow_a, label_a, arrow_b, label_b, arrow_c, label_c)
        self.add(new_a, new_b, new_c)
        self.add(comp_denom, rule_text)
        self.add(final_group)