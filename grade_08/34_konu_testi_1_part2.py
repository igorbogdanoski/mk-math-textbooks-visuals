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
        # Заокружуваме x во именителот
        # x е на крајот од стрингот
        # Позиционираме круг рачно околу x
        
        # Наоѓаме каде е x (приближно долу десно)
        target_x = expression[0][-1]
        circle_x = Circle(radius=0.3, color=MK_RED).move_to(target_x)
        
        label_x = self.get_math(r"x \neq 0", size=36, color=MK_RED)
        label_x.next_to(circle_x, RIGHT, buff=0.5)
        
        arrow_x = Arrow(label_x.get_left(), circle_x.get_right(), color=MK_RED)

        # --- ЧЕКОР 3: Втор услов (1 - 2/x) ---
        # Целиот именител не смее да биде 0
        # 1 - 2/x
        
        denom_part = expression[0][4:] # Делот 1 - 2/x
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
        
        # Прв услов
        self.add(circle_x, label_x, arrow_x)
        
        # Втор услов
        self.add(rect_denom, label_denom, arrow_denom)
        self.add(solve_group)
        
        # Резултат
        self.add(final_group)

class KT_Test1_Q15_Visual(TextbookScene):
    """
    Визуелизација за: Трансформација на дропка
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Трансформација на дропка", size=32, is_bold=True)
        naslov.to_edge(UP)
        self.add(naslov)

        # Твојот код тука...
