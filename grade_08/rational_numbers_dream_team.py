import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE
from manim import *

class KT_OSYM_Q8_NumberLine_Fixed(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Параметри за оската
        UNIT_SIZE = 2.0  # Колку простор на екран зафаќа 1 единица број
        
        # 1. Главна линија
        axis = Line(LEFT * 5.5, RIGHT * 5.5, color=MK_BLACK, stroke_width=2)
        
        # 2. Стрелки на краевите (Рачно додадени)
        tip_right = Arrow(start=RIGHT*5, end=RIGHT*5.5, color=MK_BLACK, buff=0, max_tip_length_to_length_ratio=0.5).get_tip()
        tip_right.move_to(axis.get_end())
        
        tip_left = Arrow(start=LEFT*5, end=LEFT*5.5, color=MK_BLACK, buff=0, max_tip_length_to_length_ratio=0.5).get_tip()
        tip_left.move_to(axis.get_start())
        
        # 3. Цртички и Броеви
        ticks = VGroup()
        numbers = VGroup()
        
        # Ги цртаме сите цртички од -2.5 до 2.5 со чекор 0.5
        # i оди од -5 до 5 (делено со 2)
        for i in range(-5, 6):
            val = i / 2
            pos = RIGHT * (val * UNIT_SIZE)
            
            # Дали е цел број?
            if val.is_integer():
                # Голема цртичка
                tick = Line(UP*0.15, DOWN*0.15, color=MK_BLACK, stroke_width=2).move_to(pos)
                
                # Број под цртичката
                num = MathTex(str(int(val)), color=MK_BLACK, font_size=36)
                num.next_to(tick, DOWN, buff=0.3)
                numbers.add(num)
            else:
                # Мала цртичка (за половините)
                tick = Line(UP*0.1, DOWN*0.1, color=MK_BLACK, stroke_width=1.5).move_to(pos)
            
            ticks.add(tick)

        # 4. Ознаки x, y, z (над оската)
        labels = VGroup()
        
        # z = -0.5
        pos_z = RIGHT * (-0.5 * UNIT_SIZE)
        lbl_z = MathTex("z", color=MK_BLACK, font_size=36).next_to(pos_z, UP, buff=0.4)
        
        # y = 0.5
        pos_y = RIGHT * (0.5 * UNIT_SIZE)
        lbl_y = MathTex("y", color=MK_BLACK, font_size=36).next_to(pos_y, UP, buff=0.4)
        
        # x = 1.5
        pos_x = RIGHT * (1.5 * UNIT_SIZE)
        lbl_x = MathTex("x", color=MK_BLACK, font_size=36).next_to(pos_x, UP, buff=0.4)
        
        labels.add(lbl_z, lbl_y, lbl_x)

        # 5. Прикажување на сè
        self.add(axis, tip_right, tip_left, ticks, numbers, labels)