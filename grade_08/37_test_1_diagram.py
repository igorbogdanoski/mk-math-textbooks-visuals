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
    SurroundingRectangle, DashedLine, Brace, Square,
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN,
    Transform, ReplacementTransform, FadeOut, FadeIn, Wait, Write, Create
)

class KT_Test1_Q6_Visual(TextbookScene):
    """
    Визуелизација на дијаграм со операции (Задача 6).
    Скалирана верзија за да собере сè на екранот.
    """
    
    def create_box(self, content_str, color=MK_BLUE, width=1.5):
        """Креира кутија со содржина."""
        box = Square(side_length=width, color=color)
        if content_str:
            content = MathTex(content_str, color=MK_BLACK, font_size=48)
            return VGroup(box, content)
        return box 

    def create_op_circle(self, op_str, color=MK_ORANGE):
        """Креира круг со операција."""
        circle = Circle(radius=0.4, color=color, fill_opacity=0.1, fill_color=color)
        op = MathTex(op_str, color=color, font_size=48)
        return VGroup(circle, op)

    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Дијаграм на операции", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ГРАДЕЊЕ НА ДИЈАГРАМОТ ---
        
        # Растојание меѓу нивоата (пред скалирање)
        V_BUFF = 1.5

        # 1. Влезни дропки
        box1 = self.create_box(r"\frac{3}{4}", MK_BLUE)
        box2 = self.create_box(r"\frac{1}{5}", MK_RED)
        row1 = VGroup(box1, box2).arrange(RIGHT, buff=3.0)

        # 2. Плус
        op_plus = self.create_op_circle("+")
        op_plus.move_to(row1.get_center() + DOWN * V_BUFF)
        
        line1 = Line(box1.get_bottom(), op_plus.get_top(), color=MK_GRAY)
        line2 = Line(box2.get_bottom(), op_plus.get_top(), color=MK_GRAY)

        # 3. Празно поле (зелено)
        box_sum = self.create_box("", MK_GREEN)
        box_sum.move_to(op_plus.get_center() + DOWN * V_BUFF)
        
        line_sum = Line(op_plus.get_bottom(), box_sum.get_top(), color=MK_GRAY)

        # 4. Бројот 20 (лево)
        box_20 = self.create_box("20", MK_BLACK)
        # Го позиционираме лево од box_sum
        box_20.move_to(box_sum.get_center() + LEFT * 3.0)

        # 5. Множење
        op_mult = self.create_op_circle(r"\cdot")
        # Позиција: Средина помеѓу 20 и празното поле, но подолу
        mid_x = (box_20.get_center()[0] + box_sum.get_center()[0]) / 2
        op_mult.move_to([mid_x, box_sum.get_center()[1] - V_BUFF, 0])
        
        line3 = Line(box_20.get_bottom(), op_mult.get_top(), color=MK_GRAY)
        line4 = Line(box_sum.get_bottom(), op_mult.get_top(), color=MK_GRAY)

        # 6. Прашалник
        box_final = self.create_box("?", MK_RED)
        box_final.move_to(op_mult.get_center() + DOWN * V_BUFF)
        
        line_final = Line(op_mult.get_bottom(), box_final.get_top(), color=MK_GRAY)

        # --- ГРУПИРАЊЕ И СКАЛИРАЊЕ ---
        
        diagram = VGroup(
            row1, op_plus, box_sum, box_20, op_mult, box_final,
            line1, line2, line_sum, line3, line4, line_final
        )
        
        # КЛУЧЕН МОМЕНТ: Намалуваме сè на 80%
        diagram.scale(0.8)
        
        # Центрираме на екранот (малку подолу од насловот)
        diagram.move_to(DOWN * 0.5)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(diagram)