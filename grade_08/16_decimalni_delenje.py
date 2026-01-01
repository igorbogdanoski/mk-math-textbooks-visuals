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
    SurroundingRectangle, DashedLine,
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN
)

# ==========================================
# ТЕМА: Dividing decimal numbers
# ==========================================

class KT_2_16_Visual(TextbookScene):
    """
    Визуелизација на проширување дропки:
    0.09/0.003 -> 90/3
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Проширување на дропки", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ДЕЛ 1: Првата дропка ---
        # 0.09 / 0.003
        f1_orig = self.get_math(r"\frac{0{,}09}{0{,}003}", size=42)
        
        # Стрелка со x1000
        arrow1 = Arrow(LEFT, RIGHT, color=MK_BLUE).next_to(f1_orig, RIGHT)
        label1 = self.get_text("x1000", size=20, color=MK_BLUE).next_to(arrow1, UP, buff=0.1)
        
        # Резултат
        f1_res = self.get_math(r"= \frac{90}{3} = 30", size=42).next_to(arrow1, RIGHT)
        
        group1 = VGroup(f1_orig, arrow1, label1, f1_res).arrange(RIGHT, buff=0.3)

        # --- ДЕЛ 2: Втората дропка ---
        # 5.1 / 0.17
        f2_orig = self.get_math(r"\frac{5{,}1}{0{,}17}", size=42)
        
        arrow2 = Arrow(LEFT, RIGHT, color=MK_RED).next_to(f2_orig, RIGHT)
        label2 = self.get_text("x100", size=20, color=MK_RED).next_to(arrow2, UP, buff=0.1)
        
        f2_res = self.get_math(r"= \frac{510}{17} = 30", size=42).next_to(arrow2, RIGHT)
        
        group2 = VGroup(f2_orig, arrow2, label2, f2_res).arrange(RIGHT, buff=0.3)

        # --- ДЕЛ 3: Третата дропка ---
        # 1 / 0.1
        f3_orig = self.get_math(r"\frac{1}{0{,}1}", size=42)
        
        arrow3 = Arrow(LEFT, RIGHT, color=MK_GREEN).next_to(f3_orig, RIGHT)
        label3 = self.get_text("x10", size=20, color=MK_GREEN).next_to(arrow3, UP, buff=0.1)
        
        f3_res = self.get_math(r"= \frac{10}{1} = 10", size=42).next_to(arrow3, RIGHT)
        
        group3 = VGroup(f3_orig, arrow3, label3, f3_res).arrange(RIGHT, buff=0.3)

        # --- РАСПОРЕД ---
        # Ги редиме вертикално
        all_groups = VGroup(group1, group2, group3).arrange(DOWN, buff=1.0, aligned_edge=LEFT)
        all_groups.move_to(ORIGIN)

        # --- ФИНАЛЕН ЗБИР ---
        final_sum = self.get_math("30 + 30 + 10 = 70", size=48, color=MK_BLACK)
        final_box = SurroundingRectangle(final_sum, color=MK_BLACK, buff=0.2)
        final_group = VGroup(final_box, final_sum).next_to(all_groups, DOWN, buff=0.5)

        self.add(naslov)
        self.add(all_groups)
        self.add(final_group)