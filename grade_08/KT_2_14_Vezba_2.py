import sys, os
from manim import *

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE

class KT_2_14_Vezba_2(TextbookScene):
    
    # --- GRID SYSTEM ---
    def get_digit_at(self, char, row, col, center_point, color=MK_BLACK, size=70):
        dx = 0.8
        dy = 1.2
        mob = MathTex(char, font_size=size, color=color)
        target_pos = center_point + (RIGHT * col * dx) + (DOWN * row * dy)
        mob.move_to(target_pos)
        if "{,}" in char:
            mob.shift(DOWN * 0.15)
        return mob

    # --- CARRY ANIMATION ---
    def animate_carry(self, target_mob, val="1"):
        carry_num = MathTex(val, color=MK_RED, font_size=40)
        carry_num.next_to(target_mob, UP, buff=0.1)
        self.play(TransformFromCopy(target_mob, carry_num), run_time=0.6)
        return carry_num

    # --- BORROW ANIMATION ---
    def animate_borrow(self, lender, borrower, new_lender_val, new_borrower_val):
        slash_l = Line(lender.get_corner(DL), lender.get_corner(UR), color=MK_RED, stroke_width=4).scale(0.8)
        val_l = MathTex(new_lender_val, color=MK_RED, font_size=40).next_to(lender, UP, buff=0.1)
        
        slash_b = Line(borrower.get_corner(DL), borrower.get_corner(UR), color=MK_RED, stroke_width=4).scale(0.8)
        val_b = MathTex(new_borrower_val, color=MK_RED, font_size=40).next_to(borrower, UP, buff=0.1)
        
        self.play(Create(slash_l), Write(val_l))
        self.play(TransformFromCopy(val_l, val_b), Create(slash_b))
        return VGroup(slash_l, val_l, slash_b, val_b)

    def construct(self):
        # НАСЛОВ
        title = self.get_text("Задача 2: Комплексен израз", size=40, color=MK_BLUE, is_bold=True)
        title.to_edge(UP)
        
        # (2,25 + 3,275) - (2,34 - 9,145) = ?
        problem_str = r"(2{,}25 + 3{,}275) - (2{,}34 - 9{,}145) = ?"
        problem_eq = self.get_math(problem_str, size=48)
        problem_eq.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title), Write(problem_eq))
        self.wait(1)

        # =========================================================
        # ЧЕКОР 1: 2,25 + 3,275
        # =========================================================
        step1_title = self.get_text("Чекор 1", size=30, color=MK_BLUE, is_bold=True)
        c1 = LEFT * 3 + DOWN * 0.5 
        
        # Ред 1: 2,25(0)
        n1_int = self.get_digit_at("2", 0, -1, c1)
        n1_com = self.get_digit_at("{,}", 0, 0, c1)
        n1_d1  = self.get_digit_at("2", 0, 1, c1)
        n1_d2  = self.get_digit_at("5", 0, 2, c1)
        
        # Ред 2: 3,275
        n2_int = self.get_digit_at("3", 1, -1, c1)
        n2_com = self.get_digit_at("{,}", 1, 0, c1)
        n2_d1  = self.get_digit_at("2", 1, 1, c1)
        n2_d2  = self.get_digit_at("7", 1, 2, c1)
        n2_d3  = self.get_digit_at("5", 1, 3, c1)
        
        op_plus = MathTex("+", font_size=60).next_to(n2_int, LEFT, buff=0.5)
        
        line1_y = n2_d3.get_bottom()[1] - 0.2
        line1 = Line([op_plus.get_left()[0], line1_y, 0], [n2_d3.get_right()[0]+0.2, line1_y, 0], color=MK_BLACK)
        
        step1_title.next_to(n1_int, UP, buff=1.0).align_to(op_plus, LEFT)
        
        group1 = VGroup(step1_title, n1_int, n1_com, n1_d1, n1_d2, n2_int, n2_com, n2_d1, n2_d2, n2_d3, op_plus, line1)
        self.play(Write(group1))

        # Фантомска нула
        phantom_zero = self.get_digit_at("0", 0, 3, c1, color=MK_RED)
        self.play(Write(phantom_zero))
        
        # --- ПРЕСМЕТКА ---
        res1_y = line1_y - 0.6
        
        # 0+5=5
        r1_d3 = self.get_digit_at("5", 0, 3, c1).set_y(res1_y)
        self.play(Write(r1_d3))
        
        # 5+7=12 (Carry)
        r1_d2 = self.get_digit_at("2", 0, 2, c1).set_y(res1_y)
        self.play(Write(r1_d2))
        carry1 = self.animate_carry(n1_d1, "1") 
        
        # 2+2+1=5
        r1_d1 = self.get_digit_at("5", 0, 1, c1).set_y(res1_y)
        self.play(Write(r1_d1))
        
        # Запирка и 2+3=5
        r1_com = self.get_digit_at("{,}", 0, 0, c1).set_y(res1_y - 0.15)
        r1_int = self.get_digit_at("5", 0, -1, c1).set_y(res1_y)
        self.play(Write(VGroup(r1_com, r1_int)))
        self.wait(1)
        
        # Смалување
        block1 = VGroup(group1, phantom_zero, r1_d3, r1_d2, carry1, r1_d1, r1_com, r1_int)
        self.play(block1.animate.scale(0.7).to_corner(DL, buff=1))

        # =========================================================
        # ЧЕКОР 2: 2,34 - 9,145
        # =========================================================
        step2_title = self.get_text("Чекор 2", size=30, color=MK_BLUE, is_bold=True)
        c2 = RIGHT * 2 + DOWN * 0.5 
        
        # Поставуваме 9,145 горе
        # Ред 1: 9,145
        m1_int = self.get_digit_at("9", 0, -1, c2)
        m1_com = self.get_digit_at("{,}", 0, 0, c2)
        m1_d1  = self.get_digit_at("1", 0, 1, c2)
        m1_d2  = self.get_digit_at("4", 0, 2, c2)
        m1_d3  = self.get_digit_at("5", 0, 3, c2)
        
        # Ред 2: 2,34
        m2_int = self.get_digit_at("2", 1, -1, c2)
        m2_com = self.get_digit_at("{,}", 1, 0, c2)
        m2_d1  = self.get_digit_at("3", 1, 1, c2)
        m2_d2  = self.get_digit_at("4", 1, 2, c2)
        
        op_minus = MathTex("-", font_size=60).next_to(m2_int, LEFT, buff=0.5)
        line2_y = m2_d2.get_bottom()[1] - 0.2
        line2 = Line([op_minus.get_left()[0], line2_y, 0], [m1_d3.get_right()[0]+0.2, line2_y, 0], color=MK_BLACK)
        
        step2_title.next_to(m1_int, UP, buff=1.0).align_to(op_minus, LEFT)
        
        group2 = VGroup(step2_title, m1_int, m1_com, m1_d1, m1_d2, m1_d3, m2_int, m2_com, m2_d1, m2_d2, op_minus, line2)
        self.play(Write(group2))
        
        # Фантомска нула
        m2_zero = self.get_digit_at("0", 1, 3, c2, color=MK_RED)
        self.play(Write(m2_zero))
        
        # --- ПРЕСМЕТКА ---
        res2_y = line2_y - 0.6
        
        # 5-0=5
        r2_d3 = self.get_digit_at("5", 0, 3, c2).set_y(res2_y)
        self.play(Write(r2_d3))
        
        # 4-4=0
        r2_d2 = self.get_digit_at("0", 0, 2, c2).set_y(res2_y)
        self.play(Write(r2_d2))
        
        # 1-3 (Borrow)
        borrow_vis = self.animate_borrow(m1_int, m1_d1, "8", "11")
        
        # 11-3=8
        r2_d1 = self.get_digit_at("8", 0, 1, c2).set_y(res2_y)
        self.play(Write(r2_d1))
        
        # 8-2=6
        r2_int = self.get_digit_at("6", 0, -1, c2).set_y(res2_y)
        r2_com = self.get_digit_at("{,}", 0, 0, c2).set_y(res2_y - 0.15)
        self.play(Write(VGroup(r2_int, r2_com)))
        
        # Минус
        res_neg = MathTex("-", color=MK_RED, font_size=60).next_to(r2_int, LEFT, buff=0.2)
        self.play(Write(res_neg))
        self.wait(1)
        
        block2 = VGroup(group2, m2_zero, r2_d3, r2_d2, borrow_vis, r2_d1, r2_int, r2_com, res_neg)
        self.play(block2.animate.scale(0.7).next_to(block1, RIGHT, buff=2).align_to(block1, DOWN))

        # =========================================================
        # ФИНАЛЕ ВО ИСТ РЕД
        # =========================================================
        # 5,525 - (-6,805) = 5,525 + 6,805 = 12,33
        
        # Формираме текст за пресметката
        calc_text = self.get_math("5{,}525 - (-6{,}805) = 5{,}525 + 6{,}805", size=45)
        
        # Резултатот
        final_res = self.get_math("= 12{,}33", size=45, color=MK_BLUE)
        
        # Ги групираме хоризонтално за да ги центрираме заедно
        final_group = VGroup(calc_text, final_res).arrange(RIGHT, buff=0.2).move_to(UP * 0.5)
        
        # Анимација
        self.play(Write(calc_text))
        self.wait(0.5)
        
        # Резултатот се допишува во продолжение
        self.play(Write(final_res))
        
        # Рамка само околу резултатот за акцент
        box = SurroundingRectangle(final_res, color=MK_ORANGE, buff=0.1, stroke_width=3)
        self.play(Create(box))
        
        self.wait(3)