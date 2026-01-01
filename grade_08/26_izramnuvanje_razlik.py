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
# ТЕМА: Изедначување на разликите
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

class KT_2_26_Visual(TextbookScene):
    """
    Визуелизација: Изедначување на разликите.
    a=25/29 (4), b=23/26 (3), c=17/19 (2), d=7/8 (1) -> НЗС=12
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Изедначување на разликите", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ПОДАТОЦИ ---
        # Име, Дропка, Разлика, Множител, Нова Дропка
        rows_data = [
            ("a", r"\frac{25}{29}", "4", "x3", r"\frac{75}{87}"),
            ("b", r"\frac{23}{26}", "3", "x4", r"\frac{92}{104}"),
            ("c", r"\frac{17}{19}", "2", "x6", r"\frac{102}{114}"),
            ("d", r"\frac{7}{8}", "1", "x12", r"\frac{84}{96}"),
        ]

        # --- КРЕИРАЊЕ НА РЕДОВИТЕ ---
        table_group = VGroup()
        
        # Хедери (Опционално, но добро за јасност)
        h1 = self.get_text("Дропка", size=20, color=MK_GRAY)
        h2 = self.get_text("Разлика", size=20, color=MK_RED)
        h3 = self.get_text("Прошири", size=20, color=MK_BLUE)
        h4 = self.get_text("Нова Дропка", size=20, color=MK_BLACK)
        
        headers = VGroup(h1, h2, h3, h4).arrange(RIGHT, buff=1.5)
        headers.move_to(UP * 2.0)
        table_group.add(headers)

        prev_row = headers
        
        new_fractions = [] # За подоцна да ги истакнеме

        for name, frac, diff, mult, new_frac in rows_data:
            # Елементи на редот
            t_name = self.get_math(name + " =", size=42)
            t_frac = self.get_math(frac, size=42)
            # Група за името и дропката
            col1 = VGroup(t_name, t_frac).arrange(RIGHT, buff=0.2)
            
            col2 = self.get_text(diff, size=32, color=MK_RED)
            col3 = self.get_text(mult, size=32, color=MK_BLUE)
            col4 = self.get_math(new_frac, size=42)
            new_fractions.append(col4)

            # Порамнување со хедерите
            col1.move_to([h1.get_x(), 0, 0])
            col2.move_to([h2.get_x(), 0, 0])
            col3.move_to([h3.get_x(), 0, 0])
            col4.move_to([h4.get_x(), 0, 0])
            
            # Вертикално порамнување
            row_group = VGroup(col1, col2, col3, col4)
            row_group.next_to(prev_row, DOWN, buff=0.4)
            
            # Порамнување на Y-оската на елементите во редот
            y_pos = row_group.get_center()[1]
            for item in row_group:
                item.set_y(y_pos)

            table_group.add(row_group)
            prev_row = row_group

        # --- СТРЕЛКИ ЗА ПРОЦЕСОТ ---
        # Стрелка од разлика кон множител (4 -> x3) за да се добие 12
        arrows = VGroup()
        for i in range(1, 5): # Ги прескокнуваме хедерите
            row = table_group[i]
            diff_el = row[1] # Разлика
            mult_el = row[2] # Множител
            new_el = row[3]  # Нова дропка
            
            a1 = Arrow(diff_el.get_right(), mult_el.get_left(), buff=0.2, color=MK_GRAY, stroke_width=2)
            a2 = Arrow(mult_el.get_right(), new_el.get_left(), buff=0.2, color=MK_GRAY, stroke_width=2)
            arrows.add(a1, a2)

        # --- ЗАКЛУЧОК ---
        # 75 < 84 < 92 < 102
        comp_nums = self.get_math(r"75 < 84 < 92 < 102", size=42, color=MK_BLACK)
        comp_nums.next_to(table_group, DOWN, buff=0.8)
        
        final_res = self.get_math(r"a < d < b < c", size=60, color=MK_BLACK)
        final_box = SurroundingRectangle(final_res, color=MK_BLACK, buff=0.3)
        final_group = VGroup(final_box, final_res).next_to(comp_nums, DOWN, buff=0.4)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(table_group)
        self.add(arrows)
        self.add(comp_nums)
        self.add(final_group)