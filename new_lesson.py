import sys, os
from manim import *

# Подесување на патеки
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE

class KT_2_14_Vezba_1_Pozajmuvanje(TextbookScene):
    
    # --- ГРИД ФУНКЦИЈА ---
    def get_digit_at(self, char, row, col, center_point, color=MK_BLACK, size=70):
        dx = 0.8  # Зголемено растојание за да има место за прецртување
        dy = 1.2  # Зголемено вертикално за броевите што ќе ги пишуваме горе
        mob = MathTex(char, font_size=size, color=color)
        target_pos = center_point + (RIGHT * col * dx) + (DOWN * row * dy)
        mob.move_to(target_pos)
        if "{,}" in char:
            mob.shift(DOWN * 0.15)
        return mob

    # --- НОВА ФУНКЦИЈА ЗА ПОЗАЈМУВАЊЕ (BORROWING) ---
    def animate_borrow(self, lender, borrower, new_lender_val, new_borrower_val):
        # 1. Линија за прецртување на оној што дава (Lender)
        slash_l = Line(
            start=lender.get_corner(DL), 
            end=lender.get_corner(UR), 
            color=MK_RED, stroke_width=4
        ).scale(0.8)
        
        # 2. Новата вредност над него
        val_l = MathTex(new_lender_val, color=MK_RED, font_size=50)
        val_l.next_to(lender, UP, buff=0.2)
        
        # 3. Линија за прецртување на оној што прима (Borrower)
        slash_b = Line(
            start=borrower.get_corner(DL), 
            end=borrower.get_corner(UR), 
            color=MK_RED, stroke_width=4
        ).scale(0.8)
        
        # 4. Новата вредност над него
        val_b = MathTex(new_borrower_val, color=MK_RED, font_size=50)
        val_b.next_to(borrower, UP, buff=0.2) # Малку повисоко
        
        # Анимација
        self.play(Create(slash_l), Write(val_l))
        self.play(TransformFromCopy(val_l, val_b), Create(slash_b)) # Ефект како да прелетува вредноста
        
        return val_l, val_b

    def construct(self):
        # НАСЛОВ
        title = self.get_text("Одземање со позајмување", size=40, color=MK_BLUE, is_bold=True)
        title.to_edge(UP)
        
        # Равенка: 11 - 3,8
        subtitle = self.get_math("11 - 3{,}8 = ?", size=50).next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(1)

        # ЦЕНТАР НА МРЕЖАТА
        grid_center = DOWN * 0.5
        
        # ---------------------------------------------------------
        # ПОСТАВУВАЊЕ НА ЗАДАЧАТА
        # ---------------------------------------------------------
        # РЕД 1: 11 (станува 11,0)
        # Колони: -2(десетки), -1(единици), 0(запирка), 1(десетинки)
        m1_tens = self.get_digit_at("1", 0, -2, grid_center)
        m1_ones = self.get_digit_at("1", 0, -1, grid_center)
        m1_com  = self.get_digit_at("{,}", 0, 0, grid_center, color=MK_RED) # Црвена зошто ја додаваме
        m1_zero = self.get_digit_at("0", 0, 1, grid_center, color=MK_RED)
        
        # РЕД 2: 3,8
        m2_ones = self.get_digit_at("3", 1, -1, grid_center)
        m2_com  = self.get_digit_at("{,}", 1, 0, grid_center)
        m2_dec  = self.get_digit_at("8", 1, 1, grid_center)
        
        op_minus = MathTex("-", font_size=60).next_to(m2_ones, LEFT, buff=1.2)
        
        line = Line(
            start=[op_minus.get_left()[0], m2_dec.get_bottom()[1] - 0.2, 0],
            end=[m2_dec.get_right()[0] + 0.2, m2_dec.get_bottom()[1] - 0.2, 0],
            color=MK_BLACK, stroke_width=3
        )

        # Групирање
        setup_group = VGroup(m1_tens, m1_ones, m2_ones, m2_com, m2_dec, op_minus, line)
        self.play(Write(setup_group))
        
        # Анимација: Додавање на ,0
        self.play(Write(m1_com), Write(m1_zero))
        self.wait(1)

        # ---------------------------------------------------------
        # АНИМАЦИЈА НА ПРЕСМЕТКА СО ПОЗАЈМУВАЊЕ
        # ---------------------------------------------------------
        
        # 1. ДЕСЕТИНКИ: 0 - 8 (Не може)
        # Индикатор
        indicator = SurroundingRectangle(VGroup(m1_zero, m2_dec), color=MK_ORANGE, buff=0.1)
        self.play(Create(indicator))
        
        cant_do = self.get_text("0 < 8 (Позајмуваме!)", size=24, color=MK_RED)
        cant_do.next_to(indicator, RIGHT)
        self.play(Write(cant_do))
        self.wait(1)
        
        self.play(FadeOut(indicator), FadeOut(cant_do))

        # --- ПОЗАЈМУВАЊЕ 1 ---
        # Позајмуваме од единиците (m1_ones = 1)
        # m1_ones станува 0, m1_zero станува 10
        
        new_ones, new_tenths = self.animate_borrow(
            lender=m1_ones, 
            borrower=m1_zero, 
            new_lender_val="0", 
            new_borrower_val="10"
        )
        self.wait(1)

        # Сега пресметуваме: 10 - 8 = 2
        res_y = line.get_center()[1] - 0.7
        res_dec = self.get_digit_at("2", 0, 1, grid_center).set_y(res_y)
        
        # Флеш ефект за да се види што се пресметува
        self.play(
            Indicate(new_tenths, color=MK_GREEN), 
            Indicate(m2_dec, color=MK_GREEN),
            TransformFromCopy(VGroup(new_tenths, m2_dec), res_dec)
        )
        self.wait(1)

        # 2. ЕДИНИЦИ: 0 - 3 (Не може)
        # Внимавајте: Сега гледаме во new_ones (кој е 0), а не во m1_ones
        
        indicator2 = SurroundingRectangle(VGroup(new_ones, m2_ones), color=MK_ORANGE, buff=0.1)
        self.play(Create(indicator2))
        self.wait(0.5)
        self.play(FadeOut(indicator2))

        # --- ПОЗАЈМУВАЊЕ 2 ---
        # Позајмуваме од десетките (m1_tens = 1)
        # m1_tens станува 0, new_ones (кој беше 0) станува 10
        
        new_tens_final, new_ones_final = self.animate_borrow(
            lender=m1_tens, 
            borrower=new_ones,  # Внимавајте, тука borrower е веќе новиот број горе!
            new_lender_val="0", 
            new_borrower_val="10"
        )
        self.wait(1)

        # Сега пресметуваме: 10 - 3 = 7
        res_ones = self.get_digit_at("7", 0, -1, grid_center).set_y(res_y)
        
        self.play(
            Indicate(new_ones_final, color=MK_GREEN),
            Indicate(m2_ones, color=MK_GREEN),
            TransformFromCopy(VGroup(new_ones_final, m2_ones), res_ones)
        )
        
        # Ја додаваме запирката
        res_com = self.get_digit_at("{,}", 0, 0, grid_center).set_y(res_y - 0.15)
        self.play(Write(res_com))
        self.wait(1)
        
        # 3. ДЕСЕТКИ: 0 - (ништо) = 0 (Не го пишуваме)
        # Само за крај, означуваме резултат
        
        final_box = SurroundingRectangle(VGroup(res_ones, res_com, res_dec), color=MK_GREEN)
        self.play(Create(final_box))
        self.wait(2)