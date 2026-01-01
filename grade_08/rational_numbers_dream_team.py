import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE
from manim import *

class KT_Test1_Q5_Visual_Corrected(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Боја за внатрешните форми (Розева)
        MK_PINK = "#E91E63"

        # --- ДЕЛ 1: ВОВЕД (ПРАВИЛО СО ОТВОРЕН МНОГУАГОЛНИК) ---
        
        # Креираме "отворен" многуаголник рачно со линии
        # Ова симулира дел од n-аголник
        
        # Точки кои формираат лак
        p1 = UP * 1.5 + LEFT * 2.5
        p2 = UP * 2.0 + LEFT * 1.8
        p3 = UP * 2.2 + LEFT * 1.0
        p4 = UP * 2.0 + LEFT * 0.2
        p5 = UP * 1.5 + RIGHT * 0.5
        
        # Полни линии (телото на формата)
        lines = VGroup(
            Line(p1, p2, color=MK_BLUE, stroke_width=4),
            Line(p2, p3, color=MK_BLUE, stroke_width=4),
            Line(p3, p4, color=MK_BLUE, stroke_width=4),
            Line(p4, p5, color=MK_BLUE, stroke_width=4)
        )
        
        # Испрекинати линии на краевите (сугерираат продолжување)
        dash_start = DashedLine(p1 + DL*0.5, p1, color=MK_BLUE, stroke_width=4)
        dash_end = DashedLine(p5, p5 + DR*0.5, color=MK_BLUE, stroke_width=4)
        
        open_polygon = VGroup(dash_start, lines, dash_end)
        
        # Текст и Формула
        # Го позиционираме 'x' во "центарот" на лакот
        x_label = MathTex("x", color=MK_BLACK, font_size=48).move_to(p3 + DOWN*0.8)
        
        # Текст "n-аголник"
        n_label = self.get_text("n-аголник", size=28, color=MK_BLUE).next_to(lines, UP, buff=0.2)
        
        # Формула десно
        formula = MathTex(r"= \frac{x}{10^n}", color=MK_BLACK, font_size=60)
        formula.next_to(open_polygon, RIGHT, buff=1.0)
        
        # Групирање на горниот дел
        top_section = VGroup(open_polygon, x_label, n_label, formula)
        top_section.move_to(UP * 1.5) # Позиционирање горе
        
        self.add(top_section)

        # --- ЛИНИЈА ЗА РАЗДВОЈУВАЊЕ ---
        separator = Line(LEFT*7, RIGHT*7, color=MK_GRAY, stroke_width=2)
        separator.next_to(top_section, DOWN, buff=1.0)
        self.add(separator)

        # --- ДЕЛ 2: ЗАДАЧАТА (ДОЛУ) ---

        # 1. Триаголник (x)
        tri = RegularPolygon(n=3, color=MK_BLUE, stroke_width=4).scale(1.3)
        tri_text = MathTex("x", color=MK_BLACK, font_size=48).move_to(tri).shift(DOWN*0.15)
        lhs = VGroup(tri, tri_text)

        # Знак =
        eq = MathTex("=", color=MK_BLACK, font_size=60)

        # 2. Шестаголник (5000)
        hex_shape = RegularPolygon(n=6, color=MK_BLUE, stroke_width=4).scale(1.6)
        # Внатре правоаголник
        rect = RoundedRectangle(corner_radius=0.1, width=1.8, height=1.0, color=MK_PINK, stroke_width=4)
        text_5000 = MathTex("5000", color=MK_BLACK, font_size=36).move_to(rect)
        rhs1 = VGroup(hex_shape, rect, text_5000)

        # Знак +
        plus = MathTex("+", color=MK_BLACK, font_size=60)

        # 3. Квадрат (100)
        square = RoundedRectangle(corner_radius=0.3, width=2.8, height=2.8, color=MK_BLUE, stroke_width=4)
        # Внатре петаголник
        pent = RegularPolygon(n=5, color=MK_PINK, stroke_width=4).scale(0.9)
        text_100 = MathTex("100", color=MK_BLACK, font_size=36).move_to(pent).shift(DOWN*0.1)
        rhs2 = VGroup(square, pent, text_100)

        # Позиционирање на долниот дел
        problem_row = VGroup(lhs, eq, rhs1, plus, rhs2).arrange(RIGHT, buff=0.6)
        problem_row.next_to(separator, DOWN, buff=1.0)

        self.add(problem_row)