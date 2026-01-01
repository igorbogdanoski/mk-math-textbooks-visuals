import sys
import os

# --- 1. SETUP PATH ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# --- 2. IMPORTS ---
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY
from manim import (
    Scene, VGroup, MathTex, Text, NumberLine, Line, Arrow, Dot, Circle, 
    SurroundingRectangle, DashedLine,
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN
)

class KT_2_15_Multiplication_Visual(TextbookScene):
    """
    Визуелизација на множење децимални броеви со броење на местата.
    4,02 * 3,6
    """
    
    def create_digit(self, char, pos, color=MK_BLACK, size=48):
        mob = MathTex(char, font_size=size, color=color)
        mob.move_to(pos)
        
        # КОРЕКЦИЈА 1: Запирката ја спуштаме на дното
        if char == "{,}":
            mob.shift(DOWN * 0.2)
            
        return mob

    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Множење и броење децимали", size=32, is_bold=True)
        naslov.to_edge(UP)

        # Параметри за мрежата
        dx = 0.6
        dy = 0.7
        center = LEFT * 1.0 + UP * 1.0

        # =====================================================
        # ПОСТАВКА НА МНОЖЕЊЕТО
        # =====================================================
        # 4,02
        #  3,6
        
        # Матрица (Row, Col, Char)
        data = [
            # Прв број: 4,02
            (0, -1, "4"), (0, 0, "{,}"), (0, 1, "0"), (0, 2, "2"),
            
            # Втор број: 3,6
            # КОРЕКЦИЈА 2: Користиме \cdot наместо x
            (1, -4, r"\cdot"), (1, 1, "3"), (1, 2, "{,}"), (1, 3, "6"),
        ]

        main_group = VGroup()
        
        # Цртање на броевите
        for r, c, char in data:
            pos = center + RIGHT * (c * dx) + DOWN * (r * dy)
            digit = self.create_digit(char, pos)
            main_group.add(digit)

        # Линија
        line = Line(
            start=center + RIGHT * (-4.5 * dx) + DOWN * (1.5 * dy),
            end=center + RIGHT * (4.5 * dx) + DOWN * (1.5 * dy),
            color=MK_BLACK
        )
        main_group.add(line)

        # =====================================================
        # МЕЃУ-РЕЗУЛТАТИ (Множење без запирки)
        # =====================================================
        # 6 * 402 = 2412
        # 3 * 402 = 1206
        
        res_data = [
            # 2412
            (2, 0, "2"), (2, 1, "4"), (2, 2, "1"), (2, 3, "2"),
            # 1206 (поместено лево)
            (3, -1, "1"), (3, 0, "2"), (3, 1, "0"), (3, 2, "6"),
        ]

        for r, c, char in res_data:
            pos = center + RIGHT * (c * dx) + DOWN * (r * dy)
            digit = self.create_digit(char, pos, MK_GRAY)
            main_group.add(digit)

        # Линија за собирање
        line2 = Line(
            start=center + RIGHT * (-4.5 * dx) + DOWN * (3.5 * dy),
            end=center + RIGHT * (4.5 * dx) + DOWN * (3.5 * dy),
            color=MK_BLACK
        )
        main_group.add(line2)
        
        # КОРЕКЦИЈА 3: Плусот е поместен појасно на лево
        plus_sign = self.create_digit("+", center + RIGHT * (-5.0 * dx) + DOWN * (3 * dy), size=40)
        main_group.add(plus_sign)

        # =====================================================
        # КРАЕН РЕЗУЛТАТ
        # =====================================================
        # 14472 -> 14,472
        
        final_data = [
            (4, -1, "1"), (4, 0, "4"), (4, 1, "{,}"), (4, 2, "4"), (4, 3, "7"), (4, 4, "2")
        ]
        
        for r, c, char in final_data:
            color = MK_RED if char == "{,}" else MK_BLACK
            pos = center + RIGHT * (c * dx) + DOWN * (r * dy)
            digit = self.create_digit(char, pos, color)
            main_group.add(digit)

        # =====================================================
        # ВИЗУЕЛИЗАЦИЈА НА БРОЕЊЕТО (ДЕСНО)
        # =====================================================
        
        # Стрелка и текст за првиот број (2 места)
        arrow1 = Arrow(start=LEFT, end=RIGHT, color=MK_BLUE, buff=0).scale(0.5)
        arrow1.move_to(center + RIGHT * (4 * dx) + DOWN * (0 * dy))
        
        text1 = self.get_text("2 децимали", size=24, color=MK_BLUE)
        text1.next_to(arrow1, RIGHT)
        
        # Стрелка и текст за вториот број (1 место)
        arrow2 = Arrow(start=LEFT, end=RIGHT, color=MK_BLUE, buff=0).scale(0.5)
        arrow2.move_to(center + RIGHT * (4 * dx) + DOWN * (1 * dy))
        
        text2 = self.get_text("1 децимала", size=24, color=MK_BLUE)
        text2.next_to(arrow2, RIGHT)
        
        # Линија за собирање на местата
        sum_line = Line(
            start=text2.get_corner(DL) + DOWN*0.1,
            end=text2.get_corner(DR) + DOWN*0.1,
            color=MK_BLACK
        )
        plus_small = MathTex("+", color=MK_BLACK, font_size=24).next_to(sum_line, UP, buff=0.1).shift(LEFT*1.5)

        # Вкупно места
        arrow3 = Arrow(start=LEFT, end=RIGHT, color=MK_RED, buff=0).scale(0.5)
        arrow3.move_to(center + RIGHT * (5 * dx) + DOWN * (4 * dy))
        
        text3 = self.get_text("3 децимали", size=24, color=MK_RED, is_bold=True)
        text3.next_to(arrow3, RIGHT)

        right_info = VGroup(arrow1, text1, arrow2, text2, sum_line, plus_small, arrow3, text3)

        # =====================================================
        # ДОДАВАЊЕ НА СЦЕНА
        # =====================================================
        self.add(naslov)
        self.add(main_group)
        self.add(right_info)