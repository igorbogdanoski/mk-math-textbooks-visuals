import sys, os
from manim import *

# Подесување на патеки
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE

class KT_2_14_Final(TextbookScene):
    
    # --- 1. ФУНКЦИЈА ЗА МРЕЖА (GRID) ---
    def get_digit_at(self, char, row, col, center_point, color=MK_BLACK, size=70):
        dx = 0.8  # Малку пошироко за да има место за прецртување
        dy = 1.2
        mob = MathTex(char, font_size=size, color=color)
        target_pos = center_point + (RIGHT * col * dx) + (DOWN * row * dy)
        mob.move_to(target_pos)
        if "{,}" in char:
            mob.shift(DOWN * 0.15)
        return mob

    # --- 2. ФУНКЦИЈА ЗА ПОЗАЈМУВАЊЕ (ANIMATE BORROW) ---
    def animate_borrow(self, lender, borrower, new_lender_val, new_borrower_val):
        # Прецртување на оној што дава
        slash_l = Line(lender.get_corner(DL), lender.get_corner(UR), color=MK_RED, stroke_width=4).scale(0.8)
        val_l = MathTex(new_lender_val, color=MK_RED, font_size=40).next_to(lender, UP, buff=0.1)
        
        # Прецртување на оној што прима
        slash_b = Line(borrower.get_corner(DL), borrower.get_corner(UR), color=MK_RED, stroke_width=4).scale(0.8)
        val_b = MathTex(new_borrower_val, color=MK_RED, font_size=40).next_to(borrower, UP, buff=0.1) # Малку повисоко
        
        self.play(Create(slash_l), Write(val_l))
        self.play(TransformFromCopy(val_l, val_b), Create(slash_b))
        
        # Ги враќаме новите објекти за да можеме да ги групираме подоцна
        return VGroup(slash_l, val_l, slash_b, val_b)

    def construct(self):
        # ---------------------------------------------------------
        # ВОВЕД
        # ---------------------------------------------------------
        title = self.get_text("Собирање и одземање на децимални броеви", size=40, color=MK_BLUE, is_bold=True)
        title.to_edge(UP)
        
        problem_str = r"(1{,}02 + 14{,}293) - (13 - 2{,}4) = ?"
        problem_eq = self.get_math(problem_str, size=48)
        problem_eq.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title), Write(problem_eq))
        self.wait(1)

        # ---------------------------------------------------------
        # ЧЕКОР 1: СОБИРАЊЕ (1,02 + 14,293)
        # ---------------------------------------------------------
        step1_title = self.get_text("Чекор 1", size=30, color=MK_BLUE, is_bold=True)
        c1 = LEFT * 3 + DOWN * 0.5 # Центар за Чекор 1
        
        # Ред 1
        n1_int = self.get_digit_at("1", 0, -1, c1)
        n1_com = self.get_digit_at("{,}", 0, 0, c1)
        n1_d1  = self.get_digit_at("0", 0, 1, c1)
        n1_d2  = self.get_digit_at("2", 0, 2, c1)
        
        # Ред 2
        n2_i1 = self.get_digit_at("1", 1, -2, c1)
        n2_i2 = self.get_digit_at("4", 1, -1, c1)
        n2_com = self.get_digit_at("{,}", 1, 0, c1)
        n2_d1 = self.get_digit_at("2", 1, 1, c1)
        n2_d2 = self.get_digit_at("9", 1, 2, c1)
        n2_d3 = self.get_digit_at("3", 1, 3, c1)
        
        op_plus = MathTex("+", font_size=60).next_to(n2_i1, LEFT, buff=0.5)
        
        line1_y = n2_d3.get_bottom()[1] - 0.2
        line1 = Line([op_plus.get_left()[0], line1_y, 0], [n2_d3.get_right()[0]+0.2, line1_y, 0], color=MK_BLACK, stroke_width=3)
        
        step1_title.next_to(n1_int, UP, buff=1.0).align_to(op_plus, LEFT)
        
        group1 = VGroup(step1_title, n1_int, n1_com, n1_d1, n1_d2, n2_i1, n2_i2, n2_com, n2_d1, n2_d2, n2_d3, op_plus, line1)
        self.play(Write(group1))

        # Фантомска нула
        phantom_zero = self.get_digit_at("0", 0, 3, c1, color=MK_RED)
        self.play(Write(phantom_zero))
        
        # Резултат 1: 15,313
        res1_y = line1_y - 0.6
        r1_i1 = self.get_digit_at("1", 0, -2, c1).set_y(res1_y)
        r1_i2 = self.get_digit_at("5", 0, -1, c1).set_y(res1_y)
        r1_com = self.get_digit_at("{,}", 0, 0, c1).set_y(res1_y - 0.15)
        r1_d1 = self.get_digit_at("3", 0, 1, c1).set_y(res1_y)
        r1_d2 = self.get_digit_at("1", 0, 2, c1).set_y(res1_y)
        r1_d3 = self.get_digit_at("3", 0, 3, c1).set_y(res1_y)
        
        res_group1 = VGroup(r1_i1, r1_i2, r1_com, r1_d1, r1_d2, r1_d3)
        self.play(Write(res_group1))
        self.wait(1)

        # Смалување и поместување
        block1 = VGroup(group1, phantom_zero, res_group1)
        self.play(block1.animate.scale(0.7).to_corner(DL, buff=1))


        # ---------------------------------------------------------
        # ЧЕКОР 2: ОДЗЕМАЊЕ СО ПОЗАЈМУВАЊЕ (13 - 2,4)
        # ---------------------------------------------------------
        step2_title = self.get_text("Чекор 2", size=30, color=MK_BLUE, is_bold=True)
        c2 = RIGHT * 2 + DOWN * 0.5 # Центар за Чекор 2
        
        # Ред 1: 13
        m1_i1 = self.get_digit_at("1", 0, -2, c2)
        m1_i2 = self.get_digit_at("3", 0, -1, c2)
        
        # Ред 2: 2,4
        m2_i1 = self.get_digit_at("2", 1, -1, c2) 
        m2_com = self.get_digit_at("{,}", 1, 0, c2)
        m2_d1 = self.get_digit_at("4", 1, 1, c2)
        
        op_minus = MathTex("-", font_size=60)
        op_minus.move_to(c2 + (RIGHT * -3 * 0.8) + (DOWN * 1.2)) # Рачно позициониран лево
        
        line2_y = m2_d1.get_bottom()[1] - 0.2
        line2 = Line([op_minus.get_left()[0], line2_y, 0], [m2_d1.get_right()[0]+0.2, line2_y, 0], color=MK_BLACK, stroke_width=3)
        
        step2_title.next_to(m1_i1, UP, buff=1.0).align_to(op_minus, LEFT)
        
        group2_base = VGroup(step2_title, m1_i1, m1_i2, m2_i1, m2_com, m2_d1, op_minus, line2)
        self.play(Write(group2_base))
        
        # 13 -> 13,0
        m1_com = self.get_digit_at("{,}", 0, 0, c2, color=MK_RED)
        m1_zero = self.get_digit_at("0", 0, 1, c2, color=MK_RED)
        self.play(Write(m1_com), Write(m1_zero))
        self.wait(0.5)

        # --- АНИМАЦИЈА НА ПОЗАЈМУВАЊЕ (НАЈВАЖНИОТ ДЕЛ!) ---
        # 0 - 4 не може. Позајмуваме од 3.
        # 3 станува 2. 0 станува 10.
        
        borrow_visuals = self.animate_borrow(
            lender=m1_i2,         # Позајмуваме од 3
            borrower=m1_zero,     # Даваме на 0
            new_lender_val="2", 
            new_borrower_val="10"
        )
        self.wait(1)

        # Резултат: 10,6
        res2_y = line2_y - 0.6
        # 10 - 4 = 6
        r2_d1 = self.get_digit_at("6", 0, 1, c2).set_y(res2_y)
        # Запирка
        r2_com = self.get_digit_at("{,}", 0, 0, c2).set_y(res2_y - 0.15)
        # 2 (горе) - 2 (доле) = 0
        r2_i2 = self.get_digit_at("0", 0, -1, c2).set_y(res2_y)
        # 1 (лево) - ништо = 1
        r2_i1 = self.get_digit_at("1", 0, -2, c2).set_y(res2_y)
        
        res_group2 = VGroup(r2_i1, r2_i2, r2_com, r2_d1)
        self.play(Write(res_group2))
        self.wait(1)

        # Смалување и поместување (вклучувајќи ги и црвените ознаки)
        block2 = VGroup(group2_base, m1_com, m1_zero, borrow_visuals, res_group2)
        self.play(block2.animate.scale(0.7).next_to(block1, RIGHT, buff=2).align_to(block1, DOWN))


        # ---------------------------------------------------------
        # ФИНАЛЕ
        # ---------------------------------------------------------
        final_eq_str = r"15{,}313 - 10{,}6 = 4{,}713"
        final_eq = self.get_math(final_eq_str, size=60, color=MK_BLUE)
        final_eq.move_to(UP * 0.5)

        box = SurroundingRectangle(final_eq, color=MK_ORANGE, buff=0.2, stroke_width=4)

        self.play(FadeIn(final_eq), Create(box))
        self.wait(3)