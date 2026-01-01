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

class KT_2_14_Grid_Visual(TextbookScene):
    """
    Професионална верзија со GRID систем за перфектно порамнување.
    """
    
    def create_digit(self, char, pos, color=MK_BLACK, size=48):
        """Помошна функција за креирање цифра на точна позиција."""
        mob = MathTex(char, font_size=size, color=color)
        mob.move_to(pos)
        return mob

    def add_borrow_mark(self, target_digit, new_val_str, color=MK_RED):
        """Додава цртичка и нова вредност над цифрата."""
        # 1. Цртичка (дијагонална)
        slash = Line(
            start=target_digit.get_corner(DL),
            end=target_digit.get_corner(UR),
            color=color,
            stroke_width=3
        ).scale(0.8)
        
        # 2. Нова вредност (точно над цифрата)
        val = MathTex(new_val_str, color=color, font_size=32)
        # Ја позиционираме точно над цифрата, малку погоре
        val.move_to(target_digit.get_center() + UP * 0.7)
        
        return VGroup(slash, val)

    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Пресметка со позајмување и пренесување", size=32, is_bold=True)
        naslov.to_edge(UP)

        # Параметри за мрежата
        dx = 0.5  # Хоризонтално растојание меѓу цифри
        dy = 0.7  # Вертикално растојание меѓу редови

        # =====================================================
        # ОПЕРАЦИЈА 1: СОБИРАЊЕ (1.020 + 14.293)
        # =====================================================
        # Центар за првата операција (лево)
        center_1 = LEFT * 4.5 + UP * 0.5
        
        label1 = self.get_text("1. Собирање", size=24, color=MK_BLUE)
        label1.move_to(center_1 + UP * 2.0)

        # Матрица на карактери (Row, Col, Char, Color)
        # Редови: 0 (прв број), 1 (втор број), 2 (резултат)
        # Колони: релативни (0 е запирката)
        data_op1 = [
            # Прв број: 1,020
            (0, -1, "1", MK_BLACK), (0, 0, "{,}", MK_BLACK), (0, 1, "0", MK_BLACK), (0, 2, "2", MK_BLACK), (0, 3, "0", MK_RED),
            # Втор број: + 14,293
            (1, -4, "+", MK_BLACK), (1, -2, "1", MK_BLACK), (1, -1, "4", MK_BLACK), (1, 0, "{,}", MK_BLACK), (1, 1, "2", MK_BLACK), (1, 2, "9", MK_BLACK), (1, 3, "3", MK_BLACK),
            # Резултат: 15,313
            (2, -2, "1", MK_BLACK), (2, -1, "5", MK_BLACK), (2, 0, "{,}", MK_BLACK), (2, 1, "3", MK_BLACK), (2, 2, "1", MK_BLACK), (2, 3, "3", MK_BLACK),
        ]

        group_op1 = VGroup()
        
        # Речник за да ги чуваме цифрите за подоцна (за ознаки)
        digits_op1 = {} 

        for r, c, char, col in data_op1:
            pos = center_1 + RIGHT * (c * dx) + DOWN * (r * dy)
            digit = self.create_digit(char, pos, col)
            group_op1.add(digit)
            digits_op1[(r, c)] = digit

        # Линија за собирање
        line1 = Line(
            start=center_1 + RIGHT * (-4.5 * dx) + DOWN * (1.5 * dy),
            end=center_1 + RIGHT * (3.5 * dx) + DOWN * (1.5 * dy),
            color=MK_BLACK
        )
        group_op1.add(line1)

        # ОЗНАКА ЗА ПРЕНЕСУВАЊЕ (CARRY)
        # 2+9=11 -> 1 долу, 1 горе (над 0)
        # Го наоѓаме елементот над кој треба да стои (Ред 0, Колона 1 - тоа е нулата)
        target_digit = digits_op1[(0, 1)]
        carry_1 = MathTex("1", color=MK_BLUE, font_size=24)
        carry_1.move_to(target_digit.get_center() + UP * 0.6) # Точно над нулата
        carry_circle = Circle(radius=0.15, color=MK_BLUE, stroke_width=2).move_to(carry_1)
        
        group_op1.add(carry_1, carry_circle, label1)


        # =====================================================
        # ОПЕРАЦИЈА 2: ОДЗЕМАЊЕ (13,0 - 2,4)
        # =====================================================
        center_2 = ORIGIN + UP * 0.5
        
        label2 = self.get_text("2. Одземање", size=24, color=MK_BLUE)
        label2.move_to(center_2 + UP * 2.0)

        data_op2 = [
            # 13,0
            (0, -2, "1", MK_BLACK), (0, -1, "3", MK_BLACK), (0, 0, "{,}", MK_BLACK), (0, 1, "0", MK_RED),
            # - 2,4
            (1, -4, "-", MK_BLACK), (1, -1, "2", MK_BLACK), (1, 0, "{,}", MK_BLACK), (1, 1, "4", MK_BLACK),
            # 10,6
            (2, -2, "1", MK_BLACK), (2, -1, "0", MK_BLACK), (2, 0, "{,}", MK_BLACK), (2, 1, "6", MK_BLACK),
        ]

        group_op2 = VGroup()
        digits_op2 = {}

        for r, c, char, col in data_op2:
            pos = center_2 + RIGHT * (c * dx) + DOWN * (r * dy)
            digit = self.create_digit(char, pos, col)
            group_op2.add(digit)
            digits_op2[(r, c)] = digit

        line2 = Line(
            start=center_2 + RIGHT * (-4.5 * dx) + DOWN * (1.5 * dy),
            end=center_2 + RIGHT * (1.5 * dx) + DOWN * (1.5 * dy),
            color=MK_BLACK
        )
        group_op2.add(line2)

        # ОЗНАКИ ЗА ПОЗАЈМУВАЊЕ (BORROW)
        # 3 станува 2
        mark_3 = self.add_borrow_mark(digits_op2[(0, -1)], "2")
        # 0 станува 10
        mark_0 = self.add_borrow_mark(digits_op2[(0, 1)], "10")
        
        group_op2.add(mark_3, mark_0, label2)


        # =====================================================
        # ОПЕРАЦИЈА 3: КОНЕЧНО (15,313 - 10,600)
        # =====================================================
        center_3 = RIGHT * 4.5 + UP * 0.5
        
        label3 = self.get_text("3. Резултат", size=24, color=MK_RED)
        label3.move_to(center_3 + UP * 2.0)

        data_op3 = [
            # 15,313
            (0, -2, "1", MK_BLACK), (0, -1, "5", MK_BLACK), (0, 0, "{,}", MK_BLACK), (0, 1, "3", MK_BLACK), (0, 2, "1", MK_BLACK), (0, 3, "3", MK_BLACK),
            # - 10,600
            (1, -4, "-", MK_BLACK), (1, -2, "1", MK_BLACK), (1, -1, "0", MK_BLACK), (1, 0, "{,}", MK_BLACK), (1, 1, "6", MK_BLACK), (1, 2, "0", MK_RED), (1, 3, "0", MK_RED),
            # 4,713
            (2, -1, "4", MK_BLACK), (2, 0, "{,}", MK_BLACK), (2, 1, "7", MK_BLACK), (2, 2, "1", MK_BLACK), (2, 3, "3", MK_BLACK),
        ]

        group_op3 = VGroup()
        digits_op3 = {}

        for r, c, char, col in data_op3:
            pos = center_3 + RIGHT * (c * dx) + DOWN * (r * dy)
            digit = self.create_digit(char, pos, col)
            group_op3.add(digit)
            digits_op3[(r, c)] = digit

        line3 = Line(
            start=center_3 + RIGHT * (-4.5 * dx) + DOWN * (1.5 * dy),
            end=center_3 + RIGHT * (3.5 * dx) + DOWN * (1.5 * dy),
            color=MK_BLACK
        )
        group_op3.add(line3)

        # ОЗНАКИ ЗА ПОЗАЈМУВАЊЕ
        # 5 станува 4
        mark_5 = self.add_borrow_mark(digits_op3[(0, -1)], "4")
        # 3 станува 13
        mark_3b = self.add_borrow_mark(digits_op3[(0, 1)], "13")

        group_op3.add(mark_5, mark_3b, label3)

        # =====================================================
        # ДОДАВАЊЕ НА СЦЕНА
        # =====================================================
        self.add(naslov)
        self.add(group_op1, group_op2, group_op3)