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

class KT_2_20_Visual(TextbookScene):
    """
    Визуелизација на сложен израз со периодични броеви.
    """
    def construct(self):
        # 1. Наслов (КОРИГИРАНО)
        naslov = self.get_text("Операции со периодични броеви", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ГЛАВЕН ИЗРАЗ ---
        expression = self.get_math(
            r"\frac{1}{0{,}\overline{5}} \cdot \left( \frac{0{,}\overline{a}}{0{,}0\overline{a}} : \frac{a{,}a}{aa} \right)",
            size=42
        )
        expression.move_to(UP * 2.0)

        # --- ЧЕКОР 1: Првиот дел ---
        part1_src = self.get_math(r"\frac{1}{0{,}\overline{5}}", size=42, color=MK_BLUE)
        part1_arrow = Arrow(UP, DOWN, color=MK_BLUE).next_to(part1_src, DOWN)
        part1_res = self.get_math(r"\frac{9}{5}", size=42, color=MK_BLUE).next_to(part1_arrow, DOWN)
        
        group1 = VGroup(part1_src, part1_arrow, part1_res)

        # --- ЧЕКОР 2: Вториот дел (Дропката со a) ---
        part2_src = self.get_math(r"\frac{0{,}\overline{a}}{0{,}0\overline{a}}", size=42, color=MK_RED)
        part2_arrow = Arrow(UP, DOWN, color=MK_RED).next_to(part2_src, DOWN)
        part2_res = self.get_math("10", size=42, color=MK_RED).next_to(part2_arrow, DOWN)
        
        group2 = VGroup(part2_src, part2_arrow, part2_res)

        # --- ЧЕКОР 3: Третиот дел (Делењето) ---
        part3_src = self.get_math(r"\frac{a{,}a}{aa}", size=42, color=MK_GREEN)
        part3_arrow = Arrow(UP, DOWN, color=MK_GREEN).next_to(part3_src, DOWN)
        part3_res = self.get_math(r"\frac{1}{10}", size=42, color=MK_GREEN).next_to(part3_arrow, DOWN)
        
        group3 = VGroup(part3_src, part3_arrow, part3_res)

        # --- РАСПОРЕД НА ГРУПИТЕ ---
        steps_group = VGroup(group1, group2, group3).arrange(RIGHT, buff=1.5)
        steps_group.next_to(expression, DOWN, buff=1.0)

        # --- ФИНАЛНА ПРЕСМЕТКА ---
        final_eq = self.get_math(
            r"= \frac{9}{5} \cdot \left( 10 : \frac{1}{10} \right) = \frac{9}{5} \cdot 100 = 180",
            size=48, color=MK_BLACK
        )
        final_box = SurroundingRectangle(final_eq, color=MK_BLACK, buff=0.2)
        
        final_group = VGroup(final_box, final_eq).next_to(steps_group, DOWN, buff=1.0)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(expression)
        self.add(steps_group)
        self.add(final_group)
        
        # Дополнителни линии за поврзување
        line1 = DashedLine(expression[0][0:4].get_bottom(), part1_src.get_top(), color=MK_GRAY)
        line2 = DashedLine(expression[0][6:13].get_bottom(), part2_src.get_top(), color=MK_GRAY)
        line3 = DashedLine(expression[0][14:18].get_bottom(), part3_src.get_top(), color=MK_GRAY)
        
        self.add(line1, line2, line3)