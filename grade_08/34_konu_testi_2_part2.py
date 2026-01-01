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
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN,
    Transform, ReplacementTransform, FadeOut, FadeIn, Wait, Write, Create, GrowArrow
)

class KT_Test1_Q13_Visual(TextbookScene):
    """
    Визуелизација на недефинирани вредности во верижна дропка.
    Израз: 2 - 3 / (1 - 2/x)
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Недефинирани вредности", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Изразот ---
        expression = self.get_math(r"2 - \frac{3}{1 - \frac{2}{x}}", size=60)
        expression.move_to(UP * 1.0)

        # --- ЧЕКОР 2: Прв услов (x) ---
        target_x = expression[0][-1]
        circle_x = Circle(radius=0.3, color=MK_RED).move_to(target_x)
        
        label_x = self.get_math(r"x \neq 0", size=36, color=MK_RED)
        label_x.next_to(circle_x, RIGHT, buff=0.5)
        
        arrow_x = Arrow(label_x.get_left(), circle_x.get_right(), color=MK_RED)

        # --- ЧЕКОР 3: Втор услов (1 - 2/x) ---
        denom_part = expression[0][4:] 
        rect_denom = SurroundingRectangle(denom_part, color=MK_BLUE, buff=0.1)
        
        label_denom = self.get_math(r"1 - \frac{2}{x} = 0", size=36, color=MK_BLUE)
        label_denom.next_to(rect_denom, LEFT, buff=0.5).shift(DOWN*0.5)
        
        arrow_denom = Arrow(label_denom.get_right(), rect_denom.get_left(), color=MK_BLUE)
        
        # Решавање на равенката
        solve_step1 = self.get_math(r"1 = \frac{2}{x}", size=36, color=MK_BLUE)
        solve_step2 = self.get_math(r"x = 2", size=36, color=MK_BLUE)
        
        solve_group = VGroup(solve_step1, solve_step2).arrange(DOWN, buff=0.2)
        solve_group.next_to(label_denom, DOWN, buff=0.3)

        # --- ЧЕКОР 4: Заклучок ---
        final_text = self.get_text("Вкупно 2 вредности: {0, 2}", size=28, color=MK_BLACK)
        final_box = SurroundingRectangle(final_text, color=MK_BLACK, buff=0.2)
        final_group = VGroup(final_box, final_text).to_edge(DOWN, buff=1.0)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(expression)
        self.add(circle_x, label_x, arrow_x)
        self.add(rect_denom, label_denom, arrow_denom)
        self.add(solve_group)
        self.add(final_group)


class KT_Test1_Q15_Visual(TextbookScene):
    """
    Визуелизација на трансформација на дропка (Задача 15).
    7/22 -> 1 / (3 + 2/14)
    КОРЕКЦИЈА: Подигнато нагоре за да не биде на дното.
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Трансформација на дропка", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Почетно равенство (КРЕВАМЕ ПОВИСОКО) ---
        eq_start = self.get_math(r"\frac{7}{22} = \frac{1}{m + \frac{n}{14}}", size=48)
        # КОРЕКЦИЈА: UP * 2.5 наместо 1.5
        eq_start.move_to(UP * 2.5)
        
        self.add(naslov)
        self.add(eq_start)

        # --- ЧЕКОР 2: Реципрочна вредност ---
        step1 = self.get_math(r"\frac{7}{22} = \frac{1}{\frac{22}{7}}", size=48)
        # КОРЕКЦИЈА: Намален buff од 1.0 на 0.7
        step1.next_to(eq_start, DOWN, buff=0.7)
        
        arrow1 = Arrow(eq_start.get_bottom(), step1.get_top(), color=MK_GRAY)
        label1 = self.get_text("Реципрочно", size=20, color=MK_GRAY).next_to(arrow1, RIGHT)

        self.add(arrow1, label1, step1)

        # --- ЧЕКОР 3: Мешан број ---
        step2 = self.get_math(r"= \frac{1}{3 + \frac{1}{7}}", size=48)
        step2.next_to(step1, RIGHT, buff=0.5)
        self.add(step2)

        # --- ЧЕКОР 4: Проширување ---
        step3 = self.get_math(r"= \frac{1}{3 + \frac{2}{14}}", size=48)
        step3.next_to(step2, RIGHT, buff=0.5)
        
        # Боење
        step3[0][4].set_color(MK_RED)   # 3 (m)
        step3[0][8].set_color(MK_BLUE)  # 2 (n)
        self.add(step3)

        # --- ЧЕКОР 5: Идентификација ---
        val_m = self.get_math("m = 3", size=42, color=MK_RED)
        val_n = self.get_math("n = 2", size=42, color=MK_BLUE)
        
        values = VGroup(val_m, val_n).arrange(RIGHT, buff=1.0)
        # КОРЕКЦИЈА: Намален buff од 1.0 на 0.7
        values.next_to(step1, DOWN, buff=0.7).shift(RIGHT * 2.0)
        
        self.add(values)

        # --- ЧЕКОР 6: Финален резултат ---
        final_calc = self.get_math("2m + 3n = 2(3) + 3(2) = 6 + 6 = 12", size=48, color=MK_BLACK)
        final_box = SurroundingRectangle(final_calc, color=MK_BLACK, buff=0.2)
        final_group = VGroup(final_box, final_calc).next_to(values, DOWN, buff=0.5)
        
        self.add(final_group)