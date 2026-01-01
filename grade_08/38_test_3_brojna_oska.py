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
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN,
    Create, Write
)

class KT_Test3_Q6_Visual(TextbookScene):
    """
    Визуелизација на бројна оска (Задача 6).
    0-1: 4 дела.
    1-2: 7 дела.
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Бројна оска со различни интервали", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ГЛАВНА ОСКА ---
        # Цртаме линија од -0.5 до 2.5
        # Должина на единица = 4
        UNIT_SIZE = 4
        
        line = NumberLine(
            x_range=[-0.2, 2.2, 1],
            length=10,
            color=MK_BLACK,
            include_numbers=False, # Ќе ги додадеме рачно за подобра контрола
            include_ticks=False    # И цртичките рачно
        )
        line.move_to(DOWN * 0.5)
        
        # Главни броеви (0, 1, 2)
        tick_0 = Line(UP*0.2, DOWN*0.2, color=MK_BLACK).move_to(line.n2p(0))
        label_0 = MathTex("0", color=MK_BLACK).next_to(tick_0, DOWN)
        
        tick_1 = Line(UP*0.2, DOWN*0.2, color=MK_BLACK).move_to(line.n2p(1))
        label_1 = MathTex("1", color=MK_BLACK).next_to(tick_1, DOWN)
        
        tick_2 = Line(UP*0.2, DOWN*0.2, color=MK_BLACK).move_to(line.n2p(2))
        label_2 = MathTex("2", color=MK_BLACK).next_to(tick_2, DOWN)
        
        main_ticks = VGroup(tick_0, label_0, tick_1, label_1, tick_2, label_2)

        # --- ИНТЕРВАЛ 0-1 (4 дела) ---
        # Цртички на 1/4, 2/4, 3/4
        ticks_part1 = VGroup()
        for i in range(1, 4):
            pos = line.n2p(i/4)
            tick = Line(UP*0.1, DOWN*0.1, color=MK_BLUE)
            tick.move_to(pos)
            ticks_part1.add(tick)
            
            # Точка А е на 3-тата цртичка (3/4)
            if i == 3:
                dot_A = Dot(pos, color=MK_RED, radius=0.12)
                label_A = self.get_text("A", size=24, color=MK_RED, is_bold=True).next_to(dot_A, UP)

        # --- ИНТЕРВАЛ 1-2 (7 дела) ---
        # Цртички на 1 + k/7
        ticks_part2 = VGroup()
        for k in range(1, 7):
            pos = line.n2p(1 + k/7)
            tick = Line(UP*0.1, DOWN*0.1, color=MK_GREEN)
            tick.move_to(pos)
            ticks_part2.add(tick)
            
            # Точка B е на 5-тата цртичка (според сликата во книгата, B е некаде после средината)
            # 5/7 е околу 0.71.
            if k == 5:
                dot_B = Dot(pos, color=MK_RED, radius=0.12)
                label_B = self.get_text("B", size=24, color=MK_RED, is_bold=True).next_to(dot_B, UP)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(line, main_ticks)
        self.add(ticks_part1, ticks_part2)
        self.add(dot_A, label_A)
        self.add(dot_B, label_B)