from manim import Write, FadeIn, FadeOut, Create, MathTex, VGroup, Line, UP, DOWN, LEFT, RIGHT
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_GRAY

class KT_2_14_Decimalni_Operacii(TextbookScene):
    def construct(self):
        # 1. Наслов
        title = self.get_text("Собирање и одземање на децимални броеви", size=40, color=MK_BLUE)
        title.to_edge(UP)
        subtitle = self.get_text("Клучен пример (Köşetaşı 2.14)", size=30, color=MK_GRAY)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        # 2. Проблем
        problem_eq = MathTex(r"(1{,}02 + 14{,}293) - (13 - 2{,}4) = \?").scale(1.2)
        problem_eq.next_to(subtitle, DOWN, buff=1)
        self.play(Write(problem_eq))
        self.wait(1.5)
        self.play(problem_eq.animate.scale(0.7).to_edge(UP).shift(DOWN * 1.5), FadeOut(subtitle))

        # 3. Чекор 1
        step1_label = self.get_text("Чекор 1: Собирање", size=32, color=MK_BLUE).move_to(LEFT * 4 + UP * 0.5)
        self.play(Write(step1_label))

        # Порамнување
        comma_x, base_y = -4, -0.5
        r1_int = MathTex("1", font_size=60).move_to([comma_x - 0.3, base_y, 0])
        r1_com = MathTex("{,}", font_size=60).move_to([comma_x, base_y, 0])
        r1_dec = MathTex("02", font_size=60).next_to(r1_com, RIGHT, buff=0.1)
        r1_group = VGroup(r1_int, r1_com, r1_dec)

        r2_com = MathTex("{,}", font_size=60).move_to([comma_x, base_y - 0.8, 0])
        r2_dec = MathTex("293", font_size=60).next_to(r2_com, RIGHT, buff=0.1)
        r2_int = MathTex("14", font_size=60).next_to(r2_com, LEFT, buff=0.1)
        r2_group = VGroup(r2_int, r2_com, r2_dec)

        op_plus = MathTex("+", font_size=50).next_to(r2_int, LEFT, buff=0.3)
        line1 = Line(start=op_plus.get_left() + LEFT*0.2, end=r2_dec.get_right() + RIGHT*0.2).next_to(r2_group, DOWN, buff=0.2)

        self.play(Write(r1_group), Write(r2_group), Write(op_plus), Create(line1))
        
        # Фантомска нула
        phantom_zero = MathTex("0", color=MK_RED, font_size=60).next_to(r1_dec, RIGHT, buff=0.05)
        self.play(Write(phantom_zero))
        self.wait(0.5)

        # Резултат 1
        res1_com = MathTex("{,}", font_size=60).move_to([comma_x, line1.get_y() - 0.5, 0])
        res1_dec = MathTex("313", font_size=60).next_to(res1_com, RIGHT, buff=0.1)
        res1_int = MathTex("15", font_size=60).next_to(res1_com, LEFT, buff=0.1)
        res1_group = VGroup(res1_int, res1_com, res1_dec)
        self.play(Write(res1_group))
        
        group_step1 = VGroup(step1_label, r1_group, r2_group, op_plus, line1, phantom_zero, res1_group)
        self.play(group_step1.animate.scale(0.7).to_edge(LEFT).shift(DOWN*1))

        # 4. Чекор 2
        step2_label = self.get_text("Чекор 2: Одземање", size=32, color=MK_BLUE).move_to(RIGHT * 3 + UP * 0.5)
        self.play(Write(step2_label))

        comma_x_2 = 3
        q1_int = MathTex("13", font_size=60).move_to([comma_x_2 - 0.35, base_y, 0])
        
        q2_com = MathTex("{,}", font_size=60).move_to([comma_x_2, base_y - 0.8, 0])
        q2_dec = MathTex("4", font_size=60).next_to(q2_com, RIGHT, buff=0.1)
        q2_int = MathTex("2", font_size=60).next_to(q2_com, LEFT, buff=0.1)
        q2_group = VGroup(q2_int, q2_com, q2_dec)

        op_minus = MathTex("-", font_size=50).next_to(q2_int, LEFT, buff=0.5).align_to(q2_int, LEFT).shift(LEFT*0.5)
        line2 = Line(start=op_minus.get_left(), end=q2_dec.get_right() + RIGHT*0.2).next_to(q2_group, DOWN, buff=0.2)

        self.play(Write(q1_int), Write(q2_group), Write(op_minus), Create(line2))
        
        # 13 -> 13,0
        q1_com = MathTex("{,}", color=MK_RED, font_size=60).next_to(q1_int, RIGHT, buff=0.05)
        q1_zero = MathTex("0", color=MK_RED, font_size=60).next_to(q1_com, RIGHT, buff=0.1)
        self.play(Write(q1_com), Write(q1_zero))

        res2_com = MathTex("{,}", font_size=60).move_to([comma_x_2, line2.get_y() - 0.5, 0])
        res2_dec = MathTex("6", font_size=60).next_to(res2_com, RIGHT, buff=0.1)
        res2_int = MathTex("10", font_size=60).next_to(res2_com, LEFT, buff=0.1)
        res2_group = VGroup(res2_int, res2_com, res2_dec)
        self.play(Write(res2_group))
        self.wait(1)

        # 5. Крај
        self.play(FadeOut(group_step1), FadeOut(step2_label), FadeOut(q1_int), FadeOut(q1_com), FadeOut(q1_zero), FadeOut(q2_group), FadeOut(op_minus), FadeOut(line2), FadeOut(res2_group), FadeOut(problem_eq))
        
        final_label = self.get_text("Резултат: 4,713", size=48, color=MK_BLUE)
        self.play(Write(final_label))
        self.wait(2)