import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE
from manim import *

class KT_Test7_Problem16(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Бројна оска со стрелки
        line = Arrow(LEFT * 5, RIGHT * 5, color=MK_RED, buff=0, stroke_width=4)
        
        # Точки A, B, C, D на еднакви растојанија
        pt_a = Dot(LEFT * 3, color=MK_BLACK, radius=0.08)
        pt_b = Dot(LEFT * 1, color=MK_BLACK, radius=0.08)
        pt_c = Dot(RIGHT * 1, color=MK_BLACK, radius=0.08)
        pt_d = Dot(RIGHT * 3, color=MK_BLACK, radius=0.08)
        
        # Ознаки A, B, C, D (под точките)
        lbl_a = MathTex("A", color=MK_BLACK, font_size=36).next_to(pt_a, DOWN, buff=0.2)
        lbl_b = MathTex("B", color=MK_BLACK, font_size=36).next_to(pt_b, DOWN, buff=0.2)
        lbl_c = MathTex("C", color=MK_BLACK, font_size=36).next_to(pt_c, DOWN, buff=0.2)
        lbl_d = MathTex("D", color=MK_BLACK, font_size=36).next_to(pt_d, DOWN, buff=0.2)
        
        # Црвени цртички за означување на еднакви растојанија (над линијата)
        tick_height = 0.3
        tick1_pos = (pt_a.get_center() + pt_b.get_center()) / 2
        tick2_pos = (pt_b.get_center() + pt_c.get_center()) / 2
        tick3_pos = (pt_c.get_center() + pt_d.get_center()) / 2
        
        tick1 = Line(tick1_pos + UP * tick_height/2, tick1_pos - UP * tick_height/2, 
                     color=MK_RED, stroke_width=4).rotate(60 * DEGREES)
        tick2 = Line(tick2_pos + UP * tick_height/2, tick2_pos - UP * tick_height/2, 
                     color=MK_RED, stroke_width=4).rotate(60 * DEGREES)
        tick3 = Line(tick3_pos + UP * tick_height/2, tick3_pos - UP * tick_height/2, 
                     color=MK_RED, stroke_width=4).rotate(60 * DEGREES)

        # Групирање и прикажување
        self.add(line, pt_a, pt_b, pt_c, pt_d, lbl_a, lbl_b, lbl_c, lbl_d, tick1, tick2, tick3)

class KT_Test1_Q2_Garden(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Правоаголна градина
        garden = Rectangle(width=6, height=4, color=MK_BLACK, stroke_width=4)
        
        # Поделба на половина
        div_line = Line(garden.get_top(), garden.get_bottom(), color=MK_BLACK)
        
        # Лева страна (Рози)
        roses_area = Rectangle(width=3, height=4, color=MK_RED, fill_opacity=0.3, stroke_width=0)
        roses_area.move_to(garden.get_left() + RIGHT*1.5)
        roses_text = self.get_text("Рози", size=36, color=MK_RED).move_to(roses_area)
        
        # Десна страна (Поделба на 3)
        right_side = VGroup()
        h = 4/3
        for i in range(3):
            strip = Rectangle(width=3, height=h, color=MK_BLACK, stroke_width=2)
            strip.move_to(garden.get_right() + LEFT*1.5 + UP*(4/2 - h/2 - i*h))
            right_side.add(strip)
            
        # Маргаритки (Средниот дел)
        daisies_area = right_side[1].copy()
        daisies_area.set_fill(MK_ORANGE, opacity=0.5)
        daisies_text = self.get_text("Маргаритки", size=24, color=MK_ORANGE).move_to(daisies_area)
        
        self.add(garden, div_line, roses_area, roses_text, right_side, daisies_area, daisies_text)

class KT_Test1_Q3_Beads(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # 4 Кутии (Цилиндри/Правоаголници)
        boxes = VGroup()
        labels = ["A", "B", "C", "D"]
        heights = [3.5, 1.5, 2.5, 1.0] # Визуелна репрезентација на количините
        
        for i, h in enumerate(heights):
            box = Rectangle(width=1.5, height=h, color=MK_BLUE, fill_opacity=0.5)
            # Порамнување долу
            box.move_to(RIGHT * (i*2.5 - 3.75) + DOWN * (2 - h/2))
            
            label = self.get_text(labels[i], size=36, color=MK_BLACK)
            label.next_to(box, DOWN)
            
            # Капак (елипса)
            lid = Ellipse(width=1.5, height=0.4, color=MK_BLUE, fill_opacity=0.5)
            lid.move_to(box.get_top())
            
            group = VGroup(box, lid, label)
            boxes.add(group)
            
        total_text = self.get_text("Вкупно: 1334", size=32, color=MK_BLACK)
        total_text.to_edge(UP)
        
        self.add(boxes, total_text)

class KT_Test1_Q5_Polygons(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Триаголник
        tri = RegularPolygon(n=3, color=MK_BLUE, fill_opacity=0.1).scale(1.2)
        tri_text = MathTex("x", color=MK_BLACK).move_to(tri)
        tri_group = VGroup(tri, tri_text).shift(LEFT * 4)
        
        # Знак =
        eq1 = MathTex("=", color=MK_BLACK).next_to(tri_group, RIGHT)
        
        # Шестаголник
        hex_shape = RegularPolygon(n=6, color=MK_RED, fill_opacity=0.1).scale(1.2)
        hex_text = MathTex("5000", color=MK_BLACK).move_to(hex_shape)
        hex_group = VGroup(hex_shape, hex_text).next_to(eq1, RIGHT)
        
        # Знак +
        plus = MathTex("+", color=MK_BLACK).next_to(hex_group, RIGHT)
        
        # Петаголник
        pent = RegularPolygon(n=5, color=MK_GREEN, fill_opacity=0.1).scale(1.2)
        pent_text = MathTex("100", color=MK_BLACK).move_to(pent)
        pent_group = VGroup(pent, pent_text).next_to(plus, RIGHT)
        
        # Формула долу
        formula = MathTex(r"\text{Вредност} = \frac{\text{Број}}{10^n}", color=MK_GRAY)
        formula.to_edge(DOWN, buff=1.0)
        
        self.add(tri_group, eq1, hex_group, plus, pent_group, formula)

class KT_Test1_Q6_Cakes(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Торти (Цилиндри)
        cakes = VGroup()
        data = [("Мала", 250, 1.5, 1.0), ("Средна", 400, 2.0, 1.2), ("Голема", 950, 3.0, 1.5)]
        # (Ime, Grama, Sirina, Visina)
        
        for i, (name, weight, w, h) in enumerate(data):
            body = Rectangle(width=w, height=h, color=MK_ORANGE, fill_opacity=0.8, stroke_width=0)
            top = Ellipse(width=w, height=0.5, color=MK_ORANGE, fill_opacity=0.4).move_to(body.get_top())
            
            # Декорација (глазура)
            glaze = Ellipse(width=w, height=0.5, color="#5D4037", fill_opacity=1).move_to(body.get_top())
            drips = VGroup()
            for k in range(int(w*3)):
                drip = Circle(radius=0.1, color="#5D4037", fill_opacity=1)
                drip.move_to(glaze.get_bottom() + LEFT*(w/2 - k*0.3) + DOWN*0.1)
                drips.add(drip)
                
            label = self.get_text(f"{weight} g", size=24, color=MK_BLACK).next_to(body, DOWN)
            
            cake = VGroup(body, top, glaze, drips, label)
            cake.move_to(RIGHT * (i*4 - 4))
            cakes.add(cake)
            
        # Илустрација на сечење кај големата торта
        large_cake = cakes[2]
        cut_line = DashedLine(
            large_cake[0].get_top() + RIGHT*0.5, 
            large_cake[0].get_bottom() + RIGHT*0.5, 
            color=MK_BLACK
        )
        cut_text = self.get_text("Сечење", size=20, color=MK_RED).next_to(cut_line, UP)
        
        self.add(cakes, cut_line, cut_text)