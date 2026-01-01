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
# ТЕМА: Целобројни вредности на дропки
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

class KT_2_29_Visual(TextbookScene):
    """
    Визуелизација: (2x-3)/(x+1) = 2 - 5/(x+1)
    Анализа на делители на 5.
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Целобројни вредности на дропки", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Трансформација ---
        eq_start = self.get_math(r"\frac{2x-3}{x+1}", size=48)
        arrow_trans = Arrow(LEFT, RIGHT, color=MK_BLACK)
        eq_end = self.get_math(r"= 2 - \frac{5}{x+1}", size=48)
        
        # Боење на клучниот дел
        eq_end[0][4].set_color(MK_RED)   # 5
        eq_end[0][6:].set_color(MK_BLUE) # x+1
        
        top_group = VGroup(eq_start, arrow_trans, eq_end).arrange(RIGHT, buff=0.5)
        top_group.move_to(UP * 2.0)

        # --- ЧЕКОР 2: Услов за деливост ---
        condition_text = self.get_text("Именителот мора да биде делител на 5", size=24, color=MK_GRAY)
        condition_text.next_to(top_group, DOWN, buff=0.5)
        
        # --- ЧЕКОР 3: Гранки за случаите ---
        # Делители на 5: 1, 5, -1, -5
        
        # Централна точка за гранките
        branch_start = condition_text.get_bottom() + DOWN*0.2
        
        # Случај 1
        case1 = self.get_math("x+1 = 1", size=36, color=MK_BLUE)
        res1 = self.get_math(r"\Rightarrow x=0", size=36, color=MK_BLACK)
        g1 = VGroup(case1, res1).arrange(DOWN, buff=0.1)
        
        # Случај 2
        case2 = self.get_math("x+1 = 5", size=36, color=MK_BLUE)
        res2 = self.get_math(r"\Rightarrow x=4", size=36, color=MK_BLACK)
        g2 = VGroup(case2, res2).arrange(DOWN, buff=0.1)
        
        # Случај 3
        case3 = self.get_math("x+1 = -1", size=36, color=MK_BLUE)
        res3 = self.get_math(r"\Rightarrow x=-2", size=36, color=MK_BLACK)
        g3 = VGroup(case3, res3).arrange(DOWN, buff=0.1)
        
        # Случај 4
        case4 = self.get_math("x+1 = -5", size=36, color=MK_BLUE)
        res4 = self.get_math(r"\Rightarrow x=-6", size=36, color=MK_BLACK)
        g4 = VGroup(case4, res4).arrange(DOWN, buff=0.1)
        
        # Ги редиме хоризонтално
        cases_group = VGroup(g1, g2, g3, g4).arrange(RIGHT, buff=1.0)
        cases_group.move_to(DOWN * 0.5)
        
        # Стрелки кон случаите
        arrows = VGroup()
        for g in [g1, g2, g3, g4]:
            arr = Arrow(branch_start, g.get_top(), color=MK_GRAY, buff=0.1, stroke_width=2)
            arrows.add(arr)

        # --- ЧЕКОР 4: Финален збир ---
        final_sum = self.get_math("0 + 4 + (-2) + (-6) = -4", size=48, color=MK_RED)
        final_box = SurroundingRectangle(final_sum, color=MK_RED, buff=0.2)
        final_group = VGroup(final_box, final_sum).move_to(DOWN * 2.5)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(top_group)
        self.add(condition_text)
        self.add(arrows, cases_group)
        self.add(final_group)