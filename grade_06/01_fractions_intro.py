import sys
import os

# --- МАГИЈА ЗА ИМПОРТИРАЊЕ ---
# Ова му кажува на Python да гледа две нивоа погоре за да го најде 'common' фолдерот
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Сега можеме да го импортираме нашиот стил
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK
from manim import UP, DOWN, RIGHT, NumberLine, Line, Arrow, Dot

class FractionClassification(TextbookScene):
    def construct(self):
        # 1. Наслов
        title = self.get_text("Видови дропки: Правилни и Неправилни", size=36, is_bold=True)
        title.to_edge(UP)
        
        # 2. Бројна оска
        number_line = NumberLine(
            x_range=[-0.5, 2.5, 1],
            length=10,
            color=MK_BLACK,
            include_numbers=True,
            label_direction=DOWN,
            font_size=24
        ).set_color(MK_BLACK)
        
        # Помести ја оската малку надолу
        number_line.shift(DOWN * 0.5)

        # 3. Дефинирање на регионите
        
        # ПРАВИЛНИ (Сино)
        proper_line = Line(
            number_line.n2p(0),
            number_line.n2p(1),
            color=MK_BLUE,
            stroke_width=8
        )
        proper_label = self.get_text("Правилни", color=MK_BLUE, size=24, is_bold=True)
        proper_label.next_to(proper_line, UP, buff=0.5)
        proper_math = self.get_math(r"\frac{a}{b} < 1", color=MK_BLUE, size=30)
        proper_math.next_to(proper_label, DOWN)

        # НЕПРАВИЛНИ (Црвено)
        improper_line = Arrow(
            number_line.n2p(1),
            number_line.n2p(2.5),
            color=MK_RED,
            stroke_width=8,
            buff=0
        )
        improper_label = self.get_text("Неправилни", color=MK_RED, size=24, is_bold=True)
        improper_label.next_to(improper_line, UP, buff=0.5).shift(RIGHT*0.5)
        improper_math = self.get_math(r"\frac{a}{b} \ge 1", color=MK_RED, size=30)
        improper_math.next_to(improper_label, DOWN)

        # 4. Додавање на елементите на сцена
        self.add(title)
        self.add(number_line)
        self.add(proper_line, proper_label, proper_math)
        self.add(improper_line, improper_label, improper_math)

        # 5. Примери (Точки)
        # 3/5
        dot1 = Dot(number_line.n2p(0.6), color=MK_BLUE)
        lbl1 = self.get_math(r"\frac{3}{5}", color=MK_BLUE, size=28).next_to(dot1, DOWN)
        
        # 7/5
        dot2 = Dot(number_line.n2p(1.4), color=MK_RED)
        lbl2 = self.get_math(r"\frac{7}{5}", color=MK_RED, size=28).next_to(dot2, DOWN)

        self.add(dot1, lbl1, dot2, lbl2)