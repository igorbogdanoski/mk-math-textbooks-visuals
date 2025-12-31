import sys, os
from manim import *

# 1. ПОДЕСУВАЊЕ НА ПАТЕКАТА
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE

class KT_2_14_Decimalni_Operacii(TextbookScene):
    
    # --- ПОМОШНА ФУНКЦИЈА СО КОРЕКЦИЈА ЗА ЗАПИРКАТА ---
    def get_digit_at(self, char, row, col, center_point, color=MK_BLACK, size=70):
        dx = 0.6  # Хоризонтално растојание
        dy = 1.0  # Вертикално растојание
        
        mob = MathTex(char, font_size=size, color=color)
        target_pos = center_point + (RIGHT * col * dx) + (DOWN * row * dy)
        mob.move_to(target_pos)
        
        # --- КОРЕКЦИЈА: Ако е запирка, спушти ја долу ---
        if "{,}" in char:
            mob.shift(DOWN * 0.15) # Ова ја "залепува" запирката за дното на редот
            
        return mob

    def construct(self):
        # ---------------------------------------------------------
        # ДЕЛ 1: НАСЛОВ
        # ---------------------------------------------------------
        title = self.get_text("Собирање и одземање на децимални броеви", size=40, color=MK_BLUE, is_bold=True)
        title.to_edge(UP)
        
        problem_str = r"(1{,}02 + 14{,}293) - (13 - 2{,}4) = ?"
        problem_eq = self.get_math(problem_str, size=48)
        problem_eq.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title), Write(problem_eq))
        self.wait(1)

        # ---------------------------------------------------------
        # ДЕЛ 2: ЧЕКОР 1 - СОБИРАЊЕ
        # ---------------------------------------------------------
        step1_title = self.get_text("Чекор 1", size=30, color=MK_BLUE, is_bold=True)
        grid_center_1 = LEFT * 3 + DOWN * 0.5
        
        # РЕД 1
        n1_int = self.get_digit_at("1", 0, -1, grid_center_1)
        n1_com = self.get_digit_at("{,}", 0, 0, grid_center_1)
        n1_d1  = self.get_digit_at("0", 0, 1, grid_center_1)
        n1_d2  = self.get_digit_at("2", 0, 2, grid_center_1)
        
        # РЕД 2
        n2_i1 = self.get_digit_at("1", 1, -2, grid_center_1)
        n2_i2 = self.get_digit_at("4", 1, -1, grid_center_1)
        n2_com = self.get_digit_at("{,}", 1, 0, grid_center_1)
        n2_d1 = self.get_digit_at("2", 1, 1, grid_center_1)
        n2_d2 = self.get_digit_at("9", 1, 2, grid_center_1)
        n2_d3 = self.get_digit_at("3", 1, 3, grid_center_1)
        
        # Оператор
        op_plus = MathTex("+", font_size=60, color=MK_BLACK).next_to(n2_i1, LEFT, buff=0.5)
        
        # ЛИНИЈА 
        # Ја врзуваме Y позицијата за дното на некоја ЦИФРА (не запирка), за да биде стабилна
        line_y = n2_d3.get_bottom()[1] - 0.2
        line1 = Line(
            start=[op_plus.get_left()[0], line_y, 0], 
            end=[n2_d3.get_right()[0] + 0.2, line_y, 0], 
            color=MK_BLACK, stroke_width=3
        )
        
        step1_title.next_to(n1_int, UP, buff=0.8).align_to(op_plus, LEFT)

        group_step1 = VGroup(step1_title, n1_int, n1_com, n1_d1, n1_d2, 
                             n2_i1, n2_i2, n2_com, n2_d1, n2_d2, n2_d3, 
                             op_plus, line1)
        
        self.play(Write(group_step1))
        self.wait(0.5)

        # Фантомска нула
        phantom_zero = self.get_digit_at("0", 0, 3, grid_center_1, color=MK_RED)
        self.play(Write(phantom_zero))
        self.wait(0.5)

        # Резултат 1
        y_res = line_y - 0.6 # Резултатот е под линијата
        # Запирките во резултатот исто така ќе бидат спуштени автоматски од get_digit_at
        r1_i1 = self.get_digit_at("1", 0, -2, grid_center_1).set_y(y_res)
        r1_i2 = self.get_digit_at("5", 0, -1, grid_center_1).set_y(y_res)
        r1_com = self.get_digit_at("{,}", 0, 0, grid_center_1).set_y(y_res - 0.15) # Тука мора рачно shift бидејќи set_y го пребришува нашето автоматско спуштање
        r1_d1 = self.get_digit_at("3", 0, 1, grid_center_1).set_y(y_res)
        r1_d2 = self.get_digit_at("1", 0, 2, grid_center_1).set_y(y_res)
        r1_d3 = self.get_digit_at("3", 0, 3, grid_center_1).set_y(y_res)

        res1_group = VGroup(r1_i1, r1_i2, r1_com, r1_d1, r1_d2, r1_d3)
        self.play(Write(res1_group))
        self.wait(1)

        whole_block_1 = VGroup(group_step1, phantom_zero, res1_group)
        self.play(whole_block_1.animate.scale(0.7).to_corner(DL, buff=1))

        # ---------------------------------------------------------
        # ДЕЛ 3: ЧЕКОР 2 - ОДЗЕМАЊЕ
        # ---------------------------------------------------------
        step2_title = self.get_text("Чекор 2", size=30, color=MK_BLUE, is_bold=True)
        grid_center_2 = RIGHT * 2 + DOWN * 0.5
        
        # РЕД 1
        m1_i1 = self.get_digit_at("1", 0, -2, grid_center_2)
        m1_i2 = self.get_digit_at("3", 0, -1, grid_center_2)
        
        # РЕД 2
        m2_i1 = self.get_digit_at("2", 1, -1, grid_center_2) 
        m2_com = self.get_digit_at("{,}", 1, 0, grid_center_2)
        m2_d1 = self.get_digit_at("4", 1, 1, grid_center_2)
        
        # Оператор
        op_minus = MathTex("-", font_size=60, color=MK_BLACK)
        minus_pos = grid_center_2 + (RIGHT * -3 * 0.6) + (DOWN * 1 * 1.0)
        op_minus.move_to(minus_pos)

        # ЛИНИЈА 2
        line2_y = m2_d1.get_bottom()[1] - 0.2
        line2 = Line(
            start=[op_minus.get_left()[0], line2_y, 0], 
            end=[m2_d1.get_right()[0] + 0.2, line2_y, 0], 
            color=MK_BLACK, stroke_width=3
        )
        
        step2_title.next_to(m1_i1, UP, buff=0.8).align_to(op_minus, LEFT)

        group_step2_base = VGroup(step2_title, m1_i1, m1_i2, m2_i1, m2_com, m2_d1, op_minus, line2)
        self.play(Write(group_step2_base))
        
        # 13 -> 13,0
        m1_com = self.get_digit_at("{,}", 0, 0, grid_center_2, color=MK_RED)
        m1_zero = self.get_digit_at("0", 0, 1, grid_center_2, color=MK_RED)
        
        self.play(Write(m1_com), Write(m1_zero))
        self.wait(0.5)

        # Резултат 2
        y_res_2 = line2_y - 0.6
        res2_i1 = self.get_digit_at("1", 0, -2, grid_center_2).set_y(y_res_2)
        res2_i2 = self.get_digit_at("0", 0, -1, grid_center_2).set_y(y_res_2)
        res2_com = self.get_digit_at("{,}", 0, 0, grid_center_2).set_y(y_res_2 - 0.15) # И тука рачно shift поради set_y
        res2_d1 = self.get_digit_at("6", 0, 1, grid_center_2).set_y(y_res_2)
        
        res2_group = VGroup(res2_i1, res2_i2, res2_com, res2_d1)
        self.play(Write(res2_group))
        self.wait(1)

        # Поместување
        whole_block_2 = VGroup(group_step2_base, m1_com, m1_zero, res2_group)
        self.play(
            whole_block_2.animate.scale(0.7).next_to(whole_block_1, RIGHT, buff=2).align_to(whole_block_1, DOWN)
        )
        self.wait(1)

        # ---------------------------------------------------------
        # ДЕЛ 4: ФИНАЛЕН РЕЗУЛТАТ
        # ---------------------------------------------------------
        final_eq_str = r"15{,}313 - 10{,}6 = 4{,}713"
        final_eq = self.get_math(final_eq_str, size=60, color=MK_BLUE)
        final_eq.move_to(UP * 0.5)

        box = SurroundingRectangle(final_eq, color=MK_ORANGE, buff=0.2, stroke_width=4)

        self.play(FadeIn(final_eq), Create(box))
        self.wait(3)