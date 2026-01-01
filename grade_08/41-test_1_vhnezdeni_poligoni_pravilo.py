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
    SurroundingRectangle, DashedLine, Brace, RegularPolygon, RoundedRectangle,
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN,
    Create, Write
)

class KT_Test3_Q11_Polygon_Visual(TextbookScene):
    """
    Визуелизација на задача со полигони.
    n-аголник(x) = x / 10^n
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Операции со полигони", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ДЕФИНИЦИЈА (Горе) ---
        # Сина линија (лак) што претставува дел од n-аголник
        # За едноставност, ќе нацртаме само текст и формула
        
        def_shape = RegularPolygon(n=6, color=MK_BLUE).scale(0.5)
        # Ги бришеме долните линии за да личи на "n-аголник" (апстрактно)
        # Или подобро, само текст
        
        def_text = self.get_text("n-аголник", size=24, color=MK_BLUE)
        def_val = self.get_math("x", size=36, color=MK_BLACK)
        def_val.next_to(def_text, DOWN, buff=0.2)
        
        # Формула
        def_eq = self.get_math(r"= \frac{x}{10^n}", size=48)
        
        definition_group = VGroup(def_text, def_val, def_eq).arrange(RIGHT, buff=0.5)
        # КРЕВАМЕ ВИСОКО ЗА ДА ИМА МЕСТО
        definition_group.to_edge(UP, buff=1.5)
        
        # Линија за одвојување
        sep_line = Line(LEFT*6, RIGHT*6, color=MK_GRAY).next_to(definition_group, DOWN, buff=0.5)

        # --- РАВЕНКА (Долу) ---
        
        # 1. Триаголник (x)
        tri = RegularPolygon(n=3, color=MK_BLUE, stroke_width=4).scale(0.8)
        tri_content = self.get_math("x", size=36)
        tri_content.move_to(tri.get_center() + DOWN*0.1) # Мала корекција за центарот на триаголникот
        shape1 = VGroup(tri, tri_content)
        
        # Знак =
        eq_sign = self.get_math("=", size=48)
        
        # 2. Шестаголник (5000)
        hex_shape = RegularPolygon(n=6, color=MK_BLUE, stroke_width=4).scale(0.8)
        # Црвен правоаголник внатре
        hex_inner = RoundedRectangle(corner_radius=0.1, width=1.2, height=0.6, color=MK_RED)
        hex_content = self.get_math("5000", size=24)
        hex_content.move_to(hex_inner.get_center())
        shape2 = VGroup(hex_shape, hex_inner, hex_content)
        
        # Знак +
        plus_sign = self.get_math("+", size=48)
        
        # 3. Петаголник (100) во рамка
        # Сина рамка
        frame = RoundedRectangle(corner_radius=0.2, width=1.8, height=1.8, color=MK_BLUE, stroke_width=4)
        # Црвен петаголник
        pent = RegularPolygon(n=5, color=MK_RED, stroke_width=4).scale(0.6)
        pent_content = self.get_math("100", size=24)
        pent_content.move_to(pent.get_center())
        shape3 = VGroup(frame, pent, pent_content)
        
        # Групирање на равенката
        equation_group = VGroup(shape1, eq_sign, shape2, plus_sign, shape3).arrange(RIGHT, buff=0.5)
        equation_group.next_to(sep_line, DOWN, buff=0.8)

        # --- РЕШЕНИЕ (Најдолу) ---
        # x/1000 = 5000/1000000 + 100/100000
        sol_step1 = self.get_math(r"\frac{x}{10^3} = \frac{5000}{10^6} + \frac{100}{10^5}", size=36)
        sol_step2 = self.get_math(r"\frac{x}{1000} = \frac{5}{1000} + \frac{1}{1000}", size=36)
        sol_step3 = self.get_math(r"x = 6", size=48, color=MK_RED)
        
        solution_group = VGroup(sol_step1, sol_step2, sol_step3).arrange(DOWN, buff=0.2)
        solution_group.next_to(equation_group, DOWN, buff=0.5)
        
        # Рамка околу решението
        sol_box = SurroundingRectangle(solution_group, color=MK_GRAY, buff=0.2)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(definition_group)
        self.add(sep_line)
        self.add(equation_group)
        self.add(sol_box, solution_group)