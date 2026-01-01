import sys
import os

# --- 1. SETUP PATH ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# --- 2. IMPORTS ---
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY
from manim import (
    Scene, VGroup, MathTex, Tex, Text, NumberLine, Line, Arrow, Dot, Circle, 
    SurroundingRectangle, DashedLine,
    RIGHT, LEFT, UP, DOWN, WHITE, BLACK, RED, BLUE
)

# ==========================================
# ВИЗУЕЛИЗАЦИЈА: Децимални броеви (Köşetaşı 2.14)
# ==========================================

class KT_2_14_Decimal_Ops_Visual(TextbookScene):
    """
    Визуелизација на вертикално собирање/одземање со порамнување на запирки.
    Пример: (1.02 + 14.293) - (13 - 2.4)
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Порамнување на децимални запирки", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ДЕЛ 1: СОБИРАЊЕ ---
        # 1.02 + 14.293
        # Користиме табеларен приказ за перфектно порамнување
        
        # Наслов за делот
        label_add = self.get_text("1. Собирање", size=24, color=MK_BLUE)
        
        # Броевите (со црвена нула каде што фали)
        # Користиме LaTeX array за порамнување
        add_tex = Tex(
            r"$$"
            r"\begin{array}{r@{\,}l}"
            r"1 & ,02{\color{red}0} \\"
            r"+\quad 14 & ,293 \\ \hline"
            r"15 & ,313"
            r"\end{array}$$",
            color=MK_BLACK,
            font_size=36
        )
        
        group_add = VGroup(label_add, add_tex).arrange(DOWN, buff=0.3)

        # --- ДЕЛ 2: ОДЗЕМАЊЕ ---
        # 13 - 2.4
        
        label_sub1 = self.get_text("2. Одземање", size=24, color=MK_BLUE)
            # Исправено: користи само Tex, не MathTex
        sub1_tex = Tex(
            r"$$"
            r"\begin{array}{r@{\,}l}"
            r"13 & ,{\color{red}0} \\"
            r"-\quad 2 & ,4 \\ \hline"
            r"10 & ,6"
            r"\end{array}$$",
            color=MK_BLACK,
            font_size=36
        )
        
        group_sub1 = VGroup(label_sub1, sub1_tex).arrange(DOWN, buff=0.3)

        # --- ДЕЛ 3: КОНЕЧНО ---
        # 15.313 - 10.6
        
        label_final = self.get_text("3. Конечен резултат", size=24, color=MK_RED)
        
        final_tex = Tex(
            r"$$"
            r"\begin{array}{r@{\,}l}"
            r"15 & ,313 \\"
            r"-\quad 10 & ,6{\color{red}00} \\ \hline"
            r"4 & ,713"
            r"\end{array}$$",
            color=MK_BLACK,
            font_size=36
        )
        
        # Рамка околу резултатот
        box = SurroundingRectangle(final_tex, color=MK_RED, buff=0.2)
        group_final = VGroup(label_final, final_tex, box).arrange(DOWN, buff=0.3)

        # --- РАСПОРЕД НА ЕКРАНОТ ---
        # Ги редиме трите групи хоризонтално
        all_groups = VGroup(group_add, group_sub1, group_final).arrange(RIGHT, buff=1.5)
        all_groups.next_to(naslov, DOWN, buff=1.0)

        # Стрелки помеѓу чекорите
        arrow1 = Arrow(start=group_add.get_right(), end=group_sub1.get_left(), color=MK_GRAY)
        arrow2 = Arrow(start=group_sub1.get_right(), end=group_final.get_left(), color=MK_GRAY)

        # Додавање на сцена
        self.add(naslov)
        self.add(all_groups)
        self.add(arrow1, arrow2)
        
        # Дополнителен текст за појаснување (долу)
        note = self.get_text(
            "Црвените нули се допишуваат за полесно пресметување.", 
            size=20, 
            color=MK_RED,
            is_bold=False
        )
        note.to_edge(DOWN, buff=0.5)
        self.add(note)