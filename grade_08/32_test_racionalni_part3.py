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

class KT_Test_22_Visual(TextbookScene):
    """
    Визуелизација на споредување периодични броеви (Задача 22).
    КОРЕКЦИЈА: Точни периоди според задачата.
    a = 4,3213... (Периода 321)
    b = 4,3212... (Периода 21)
    c = 4,3211... (Периода 1)
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Споредување на периодични броеви", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Поставка на броевите ---
        # Ги делиме стринговите за да ја истакнеме 4-тата децимала (каде што се разликуваат)
        
        # a = 4,321 3 21...
        eq_a = MathTex(r"a = 4{,}321", r"3", r"21...", font_size=48, color=MK_BLACK)
        
        # b = 4,321 2 12...
        eq_b = MathTex(r"b = 4{,}321", r"2", r"12...", font_size=48, color=MK_BLACK)
        
        # c = 4,321 1 11...
        eq_c = MathTex(r"c = 4{,}321", r"1", r"11...", font_size=48, color=MK_BLACK)
        
        # Ги групираме и порамнуваме лево
        equations = VGroup(eq_a, eq_b, eq_c).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        equations.move_to(UP * 0.5)

        # --- ЧЕКОР 2: Истакнување (Боја + Правоаголник) ---
        
        # Ги боиме клучните цифри во ЦРВЕНО (индекс 1 е средниот елемент)
        target_digits = VGroup(eq_a[1], eq_b[1], eq_c[1])
        target_digits.set_color(MK_RED)
        
        # Правоаголник околу разликата
        highlight_box = SurroundingRectangle(
            target_digits,
            color=MK_RED,
            buff=0.25, 
            stroke_width=3
        )
        
        label_diff = self.get_text("Разлика!", size=24, color=MK_RED)
        label_diff.next_to(highlight_box, UP)

        # --- ЧЕКОР 3: Споредба ---
        # 3 > 2 > 1
        comp_text = self.get_math(r"3 > 2 > 1", size=48, color=MK_BLUE)
        comp_text.next_to(highlight_box, RIGHT, buff=1.5)
        
        # Стрелка
        arrow_comp = Arrow(
            start=eq_b[1].get_right() + RIGHT*0.3, 
            end=comp_text.get_left(), 
            color=MK_BLUE,
            stroke_width=4
        )

        # --- ЧЕКОР 4: Заклучок ---
        # a > b > c
        final_res = self.get_math("a > b > c", size=60, color=MK_BLACK)
        final_res.next_to(equations, DOWN, buff=1.5)
        
        final_box = SurroundingRectangle(final_res, color=MK_BLACK, buff=0.3)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(equations)
        self.add(highlight_box, label_diff)
        self.add(arrow_comp, comp_text)
        self.add(final_res, final_box)