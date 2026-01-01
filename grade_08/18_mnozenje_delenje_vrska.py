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

class KT_2_18_Visual(TextbookScene):
    """
    Визуелизација: x * 0.125 = x / 8
    КОРЕКЦИЈА: Подигната позиција за да не се сече текстот долу.
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Врска меѓу множење и делење", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Поставка (ПОДИГНАТО НАГОРЕ) ---
        # x * 0.125
        # Претходно беше UP * 1.0, сега го креваме на UP * 2.0
        eq_start = self.get_math("x \cdot 0{,}125", size=48)
        eq_start.move_to(UP * 2.0 + LEFT * 3.0)

        # Стрелка кон конверзија
        arrow1 = Arrow(LEFT, RIGHT, color=MK_BLACK).next_to(eq_start, RIGHT)
        
        # --- ЧЕКОР 2: Конверзија во дропка ---
        # x * 125/1000
        eq_mid = self.get_math(r"x \cdot \frac{125}{1000}", size=48)
        eq_mid.next_to(arrow1, RIGHT)
        
        # Истакнување на кратењето
        # 125/1000 -> 1/8
        brace = Brace(eq_mid[0][2:], direction=DOWN, color=MK_BLUE)
        brace_text = self.get_math(r"= \frac{1}{8}", size=36, color=MK_BLUE).next_to(brace, DOWN)
        
        # --- ЧЕКОР 3: Финален облик ---
        # Стрелка надолу кон заклучокот
        arrow2 = Arrow(UP, DOWN, color=MK_BLACK).next_to(brace_text, DOWN, buff=0.5)
        
        # x * 1/8 = x/8
        eq_final = self.get_math(r"x \cdot \frac{1}{8} = \frac{x}{8}", size=60)
        eq_final.next_to(arrow2, DOWN)
        
        # Рамка за заклучокот
        box = SurroundingRectangle(eq_final, color=MK_RED, buff=0.3)
        
        # Текстуален заклучок
        conclusion = self.get_text("Множење со 0,125 = Делење со 8", size=28, color=MK_RED, is_bold=True)
        conclusion.next_to(box, DOWN, buff=0.3)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(eq_start, arrow1, eq_mid)
        self.add(brace, brace_text)
        self.add(arrow2, eq_final, box, conclusion)