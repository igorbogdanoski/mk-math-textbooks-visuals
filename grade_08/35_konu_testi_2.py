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

class KT_Test2_Q1_Visual(TextbookScene):
    """
    Визуелизација на верижна равенка (Задача 1).
    Метод: Отпакување (чекор по чекор наоѓање на непознатиот дел).
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Решавање верижна равенка", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ГЛАВНА РАВЕНКА (Лево) ---
        eq_main = self.get_math(r"\frac{10}{1 + \frac{5}{1 + \frac{3}{1-x}}} = 5", size=48)
        eq_main.move_to(LEFT * 3.5 + UP * 0.5)
        
        # Рамка околу главната равенка
        box_main = SurroundingRectangle(eq_main, color=MK_GRAY, buff=0.3)
        label_main = self.get_text("Почеток", size=24, color=MK_GRAY).next_to(box_main, UP)

        # --- ЧЕКОРИ НА РЕШАВАЊЕ (Десно) ---
        # Ќе ги редиме вертикално
        
        # Чекор 1: Именителот мора да е 2 (бидејќи 10/2 = 5)
        step1 = self.get_math(r"1 + \frac{5}{1 + \frac{3}{1-x}} = 2", size=42)
        
        # Чекор 2: Дропката мора да е 1 (бидејќи 1+1=2)
        step2 = self.get_math(r"\frac{5}{1 + \frac{3}{1-x}} = 1", size=42)
        
        # Чекор 3: Именителот мора да е 5 (бидејќи 5/5=1)
        step3 = self.get_math(r"1 + \frac{3}{1-x} = 5", size=42)
        
        # Чекор 4: Дропката мора да е 4 (бидејќи 1+4=5)
        step4 = self.get_math(r"\frac{3}{1-x} = 4", size=42)
        
        # Чекор 5: Финале
        step5 = self.get_math(r"1-x = \frac{3}{4} \Rightarrow x = \frac{1}{4}", size=42, color=MK_RED)

        # Групирање и порамнување на чекорите
        steps_group = VGroup(step1, step2, step3, step4, step5).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        steps_group.move_to(RIGHT * 2.0)

        # --- СТРЕЛКИ ЗА ПОВРЗУВАЊЕ ---
        # Стрелка од главната равенка кон првиот чекор
        arrow_start = Arrow(eq_main.get_right(), step1.get_left(), color=MK_BLUE)
        
        # Мали стрелки помеѓу чекорите
        arrows_steps = VGroup()
        for i in range(len(steps_group) - 1):
            arr = Arrow(
                steps_group[i].get_bottom(), 
                steps_group[i+1].get_top(), 
                color=MK_GRAY, 
                buff=0.1,
                max_tip_length_to_length_ratio=0.15
            ).scale(0.5)
            arrows_steps.add(arr)

        # --- ИСТАКНУВАЊЕ НА ДЕЛОВИТЕ (Боење) ---
        # Во секој чекор го боиме делот што сме го "откриле"
        
        # Чекор 1: Боиме се освен 1+
        step1[0][2:].set_color(MK_BLUE) 
        
        # Чекор 2: Боиме се освен 5/
        step2[0][2:].set_color(MK_BLUE)
        
        # Чекор 3: Боиме се освен 1+
        step3[0][2:].set_color(MK_BLUE)
        
        # Чекор 4: Боиме 1-x
        step4[0][2:5].set_color(MK_BLUE)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(eq_main, box_main, label_main)
        self.add(steps_group)
        self.add(arrow_start, arrows_steps)
        
        # Рамка околу решението
        final_box = SurroundingRectangle(step5, color=MK_RED, buff=0.15)
        self.add(final_box)