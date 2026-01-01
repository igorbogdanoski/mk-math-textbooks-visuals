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
# ТЕМА: Телескопски производ
# ==========================================

class KT_Test_12_Visual(TextbookScene):
    """
    Визуелизација на телескопски производ (Задача 12).
    Робустен метод: Рачно креирање на дропките за прецизно прецртување.
    """
    
    def create_fraction(self, num_str, den_str, color=MK_BLACK):
        """Помошна функција за креирање дропка како група од објекти."""
        num = MathTex(num_str, color=color, font_size=48)
        den = MathTex(den_str, color=color, font_size=48)
        line = Line(LEFT, RIGHT, color=color).match_width(VGroup(num, den)).scale(1.2)
        
        # Позиционирање
        group = VGroup(num, line, den).arrange(DOWN, buff=0.1)
        return group, num, den # Враќаме и пристап до броителот/именителот

    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Телескопски производ", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Оригиналниот израз ---
        eq_start = self.get_math(
            r"\left(1-\frac{2}{3}\right) \cdot \left(1-\frac{2}{5}\right) \cdot \left(1-\frac{2}{7}\right) \dots \left(1-\frac{2}{99}\right)",
            size=42
        )
        eq_start.move_to(UP * 2.0)

        # --- ЧЕКОР 2: Конструирање на дропките (Рачно) ---
        # Сакаме: 1/3 * 3/5 * 5/7 ... 97/99
        
        # Дропка 1: 1/3
        f1, n1, d1 = self.create_fraction("1", "3")
        dot1 = MathTex(r"\cdot", color=MK_BLACK)
        
        # Дропка 2: 3/5
        f2, n2, d2 = self.create_fraction("3", "5")
        dot2 = MathTex(r"\cdot", color=MK_BLACK)
        
        # Дропка 3: 5/7
        f3, n3, d3 = self.create_fraction("5", "7")
        dot3 = MathTex(r"\cdot", color=MK_BLACK)
        
        # Точки ...
        dots = MathTex(r"\dots", color=MK_BLACK)
        dot4 = MathTex(r"\cdot", color=MK_BLACK)
        
        # Последна дропка: 97/99
        f_last, n_last, d_last = self.create_fraction("97", "99")

        # Групирање во еден ред
        # Редослед: f1, dot, f2, dot, f3, dot, dots, dot, f_last
        expression_group = VGroup(
            f1, dot1, f2, dot2, f3, dot3, dots, dot4, f_last
        ).arrange(RIGHT, buff=0.2)
        
        expression_group.move_to(ORIGIN)

        # --- ЧЕКОР 3: Прецртување (Slash Lines) ---
        # Сега имаме директен пристап до d1 (именител 3) и n2 (броител 3)
        
        lines = VGroup()
        
        # Кратиме 3 со 3
        l1 = Line(d1.get_corner(DL), d1.get_corner(UR), color=MK_RED, stroke_width=3)
        l2 = Line(n2.get_corner(DL), n2.get_corner(UR), color=MK_RED, stroke_width=3)
        lines.add(l1, l2)
        
        # Кратиме 5 со 5
        l3 = Line(d2.get_corner(DL), d2.get_corner(UR), color=MK_RED, stroke_width=3)
        l4 = Line(n3.get_corner(DL), n3.get_corner(UR), color=MK_RED, stroke_width=3)
        lines.add(l3, l4)
        
        # Кратиме 7 со ...
        l5 = Line(d3.get_corner(DL), d3.get_corner(UR), color=MK_RED, stroke_width=3)
        lines.add(l5)
        
        # Кратиме ... со 97
        l6 = Line(n_last.get_corner(DL), n_last.get_corner(UR), color=MK_RED, stroke_width=3)
        lines.add(l6)

        # --- ЧЕКОР 4: Истакнување на преживеаните ---
        # Преживуваат n1 (1) и d_last (99)
        
        c1 = Circle(radius=0.3, color=MK_BLUE).move_to(n1)
        c2 = Circle(radius=0.4, color=MK_BLUE).move_to(d_last)
        circles = VGroup(c1, c2)

        # --- ЧЕКОР 5: Резултат ---
        result = self.get_math(r"= \frac{1}{99}", size=60, color=MK_BLACK)
        result.next_to(expression_group, DOWN, buff=1.0)
        
        box = SurroundingRectangle(result, color=MK_BLUE, buff=0.2)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(eq_start)
        self.add(expression_group)
        self.add(lines)
        self.add(circles)
        self.add(result, box)
