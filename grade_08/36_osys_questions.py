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
    SurroundingRectangle, DashedLine, Brace, Rectangle,
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN,
    Transform, ReplacementTransform, FadeOut, FadeIn, Wait, Write, Create
)

# ==========================================
# ЗАДАЧА 12: ТОРТА (Само илустрација)
# ==========================================
class KT_Test_Q12_Visual(TextbookScene):
    """
    Визуелизација на тортата поделена на 4, па едно парче на 3.
    Без текст и решенија.
    """
    def construct(self):
        # --- ЧЕКОР 1: Цела торта (4 дела) ---
        # Правоаголник 6x4
        cake = Rectangle(width=6, height=4, color=MK_BLACK, stroke_width=4)
        
        # Линии за поделба на 4 дела
        v_line = Line(cake.get_top(), cake.get_bottom(), color=MK_BLACK, stroke_width=2)
        h_line = Line(cake.get_left(), cake.get_right(), color=MK_BLACK, stroke_width=2)
        
        # --- ЧЕКОР 2: Поделба на горното лево парче на 3 ---
        # Горното лево парче е со димензии 3x2, центар [-1.5, 1, 0]
        
        # Ги цртаме трите помали парчиња едно до друго
        # Ширина на секое мало парче = 3 / 3 = 1
        
        # Парче 1 (Бурџу)
        p1 = Rectangle(width=1, height=2, color=MK_BLACK, fill_opacity=0.6, fill_color=MK_BLUE)
        p1.move_to([-2.5, 1, 0]) # Лево
        
        # Парче 2 (Џем)
        p2 = Rectangle(width=1, height=2, color=MK_BLACK, fill_opacity=0.6, fill_color=MK_RED)
        p2.move_to([-1.5, 1, 0]) # Средина
        
        # Парче 3 (Дениз)
        p3 = Rectangle(width=1, height=2, color=MK_BLACK, fill_opacity=0.6, fill_color=MK_GREEN)
        p3.move_to([-0.5, 1, 0]) # Десно

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(cake)
        self.add(v_line, h_line)
        self.add(p1, p2, p3)


# ==========================================
# ЗАДАЧА 14: ЛИНИЈАРИ (Само поставка)
# ==========================================
class KT_Test_Q14_Visual(TextbookScene):
    """
    Визуелизација на линијарите порамнети лево.
    Без линии за решение.
    """
    
    def create_ruler(self, length, gap, color=MK_BLACK):
        """Креира линијар со празнини."""
        total_width = length + 2 * gap
        
        # Телото на линијарот
        body = Rectangle(width=total_width, height=1, color=color, fill_opacity=0.05, fill_color=color, stroke_width=2)
        
        # Скалата (NumberLine)
        scale = NumberLine(
            x_range=[0, length, 1],
            length=length,
            color=color,
            include_numbers=True,
            font_size=24,
            label_direction=UP,
            tick_size=0.1
        )
        scale.move_to(body.get_center())
        
        # Ознаки за празнините (вертикални цртички на краевите на скалата)
        # Лева граница на скалата
        tick_start = Line(scale.n2p(0) + UP*0.3, scale.n2p(0) + DOWN*0.3, color=color, stroke_width=2)
        # Десна граница на скалата
        tick_end = Line(scale.n2p(length) + UP*0.3, scale.n2p(length) + DOWN*0.3, color=color, stroke_width=2)
        
        return VGroup(body, scale, tick_start, tick_end)

    def construct(self):
        # Скалирање за да собере на екран
        SCALE_FACTOR = 0.9
        
        # --- ГОРЕН ЛИНИЈАР (10 cm, gap 0.8) ---
        ruler_top = self.create_ruler(10, 0.8, MK_BLUE)
        ruler_top.scale(SCALE_FACTOR)
        
        # Позиционирање: Горе лево
        ruler_top.move_to(UP * 1.0 + LEFT * 4) 
        ruler_top.to_edge(LEFT, buff=1.0)

        # --- ДОЛНИ ЛИНИЈАРИ (6 cm, gap 0.2) ---
        ruler_bot1 = self.create_ruler(6, 0.2, MK_BLACK)
        ruler_bot1.scale(SCALE_FACTOR)
        
        ruler_bot2 = self.create_ruler(6, 0.2, MK_BLACK)
        ruler_bot2.scale(SCALE_FACTOR)
        
        # Позиционирање
        # Долен 1 точно под Горниот, порамнети ЛЕВО (според надворешната ивица)
        ruler_bot1.next_to(ruler_top, DOWN, buff=0.2, aligned_edge=LEFT)
        
        # Долен 2 залепен до Долен 1 (без размак)
        ruler_bot2.next_to(ruler_bot1, RIGHT, buff=0)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(ruler_top)
        self.add(ruler_bot1, ruler_bot2)