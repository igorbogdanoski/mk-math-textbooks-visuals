import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE
from manim import *

class KT_Test2_Q1_Cardboard(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Бои од сликата (приближни)
        COLOR_BLUE = "#AEEEEE"  # Светло сина
        COLOR_PINK = "#FFC0CB"  # Розева
        COLOR_ORANGE = "#FFDAB9" # Праска/Портокалова
        COLOR_GREEN = "#C1FFC1"  # Светло зелена
        
        # 1. Прва фаза: Празен квадрат
        square = Square(side_length=3, color=MK_BLACK, stroke_width=2)
        
        # 2. Втора фаза: Сечење (Сино горе, Розево долу со поделби)
        # Големиот правоаголник (поделен на пола хоризонтално)
        rect_blue = Rectangle(width=3, height=1.5, color=MK_BLACK, stroke_width=2, fill_color=COLOR_BLUE, fill_opacity=1)
        rect_pink_base = Rectangle(width=3, height=1.5, color=MK_BLACK, stroke_width=2, fill_color=COLOR_PINK, fill_opacity=1)
        
        # Ги позиционираме
        rect_blue.next_to(square, RIGHT, buff=1.5).align_to(square, UP)
        rect_pink_base.next_to(rect_blue, DOWN, buff=0)
        
        # Стрелка за означување на трансформација
        scissors = MathTex(r"\rightarrow", color=MK_RED, font_size=48)
        scissors.next_to(square, RIGHT, buff=0.5)

        # 3. Трета фаза: Распределба (Стрелка и имиња)
        arrow = Arrow(rect_blue.get_right(), rect_blue.get_right() + RIGHT*1, color=MK_RED, stroke_width=4)
        
        # Парчињата за учениците
        # Ахмет: Големо сино парче
        p_ahmet = Rectangle(width=4, height=2, color=MK_BLACK, stroke_width=1, fill_color=COLOR_BLUE, fill_opacity=1)
        
        # Бенгу: Розево (половина од долниот дел)
        p_bengu = Rectangle(width=2, height=2, color=MK_BLACK, stroke_width=1, fill_color=COLOR_PINK, fill_opacity=1)
        
        # Џанан: Портокалово (половина од остатокот)
        p_canan = Rectangle(width=0.5, height=2, color=MK_BLACK, stroke_width=1, fill_color=COLOR_ORANGE, fill_opacity=1)
        
        # Дениз: Зелено (остатокот, поделен на 3 ленти според сликата, но всушност е еден дел)
        # На сликата Дениз има 3 ленти, што сугерира дека тој дел е дополнително сецкан или е само визуелен приказ.
        # Ќе нацртаме 3 зелени ленти една до друга.
        p_deniz_group = VGroup()
        for _ in range(3):
            strip = Rectangle(width=0.5, height=2, color=MK_BLACK, stroke_width=1, fill_color=COLOR_GREEN, fill_opacity=1)
            p_deniz_group.add(strip)
        p_deniz_group.arrange(RIGHT, buff=0.1)

        # Групирање и позиционирање на крајниот дел
        final_group = VGroup(p_ahmet, p_bengu, p_canan, p_deniz_group).arrange(RIGHT, buff=0.5)
        final_group.next_to(arrow, RIGHT)
        
        # Имиња
        n_ahmet = Text("Ahmet", font="Arial", font_size=20, color=MK_BLACK).next_to(p_ahmet, DOWN)
        n_bengu = Text("Bengü", font="Arial", font_size=20, color=MK_BLACK).next_to(p_bengu, DOWN)
        n_canan = Text("Canan", font="Arial", font_size=20, color=MK_BLACK).next_to(p_canan, DOWN)
        n_deniz = Text("Deniz", font="Arial", font_size=20, color=MK_BLACK).next_to(p_deniz_group, DOWN)

        # Целосна сцена (Скалирана за да собере)
        full_scene = VGroup(
            square, scissors, rect_blue, rect_pink_base, arrow, 
            final_group, n_ahmet, n_bengu, n_canan, n_deniz
        ).scale(0.7).move_to(ORIGIN)
        
        # Додавање на линиите за поделба во втората фаза (розевиот дел)
        # На сликата розевиот дел е поделен на: Големо розево, Портокалово, и 3 Зелени
        # Ширина 3. Половина е 1.5 (Розево). Четвртина е 0.75 (Портокалово). Останато 0.75 (3x0.25 Зелени).
        
        div_line1 = Line(rect_pink_base.get_bottom() + LEFT*0, rect_pink_base.get_top() + LEFT*0, color=MK_BLACK, stroke_width=1) # Средина
        div_line2 = Line(rect_pink_base.get_bottom() + RIGHT*0.75, rect_pink_base.get_top() + RIGHT*0.75, color=MK_BLACK, stroke_width=1)
        div_line3 = Line(rect_pink_base.get_bottom() + RIGHT*1.0, rect_pink_base.get_top() + RIGHT*1.0, color=MK_BLACK, stroke_width=1)
        div_line4 = Line(rect_pink_base.get_bottom() + RIGHT*1.25, rect_pink_base.get_top() + RIGHT*1.25, color=MK_BLACK, stroke_width=1)
        
        # Боење на втората фаза (преку overlay)
        overlay_pink = Rectangle(width=1.5, height=1.5, fill_color=COLOR_PINK, fill_opacity=1, stroke_width=0).move_to(rect_pink_base.get_left() + RIGHT*0.75)
        overlay_orange = Rectangle(width=0.75, height=1.5, fill_color=COLOR_ORANGE, fill_opacity=1, stroke_width=0).next_to(overlay_pink, RIGHT, buff=0)
        overlay_green = Rectangle(width=0.75, height=1.5, fill_color=COLOR_GREEN, fill_opacity=1, stroke_width=0).next_to(overlay_orange, RIGHT, buff=0)
        
        # Ги додаваме овие во групата пред скалирање, но бидејќи веќе скалиравме, ги додаваме рачно
        # Најлесно е да се додаде сè на крај
        
        self.add(full_scene)

class KT_Test2_Q4_NumberLine(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Главна линија (сива/сребрена како игла)
        needle = Rectangle(width=12, height=0.2, color=MK_GRAY, fill_opacity=0.5, stroke_color=MK_BLACK, stroke_width=1).set_style(fill_color="#D3D3D3")
        needle.move_to(ORIGIN)
        
        # Врв на иглата (лево)
        tip = Triangle(color=MK_GRAY, fill_opacity=0.5).rotate(PI/2).scale(0.2).next_to(needle, LEFT, buff=0)
        tip.set_style(fill_color="#A9A9A9", stroke_color=MK_BLACK, stroke_width=1)
        
        # Крај на иглата (десно)
        end = RoundedRectangle(corner_radius=0.1, width=0.5, height=0.3, color=MK_BLACK).next_to(needle, RIGHT, buff=0)
        
        # Главни броеви (-2, -1, 0, 1, 2, 3)
        # Растојание меѓу главни броеви = 2 единици
        start_x = -5
        step = 2
        
        main_ticks = VGroup()
        labels = VGroup()
        
        for i in range(6): # 0 to 5
            val = -2 + i
            x_pos = start_x + i * step
            
            # Главна цртичка (Сина, дебела)
            tick = Line(UP*0.2, DOWN*0.2, color=MK_BLUE, stroke_width=4).move_to(RIGHT * x_pos)
            main_ticks.add(tick)
            
            # Бројка
            label = MathTex(str(val), color=MK_BLUE).next_to(tick, UP, buff=0.3)
            labels.add(label)

        # Поделби и Точки (Црвени)
        sub_ticks = VGroup()
        points = VGroup()
        point_labels = VGroup()
        arrows = VGroup()

        # Функција за додавање поделби
        def add_interval(start_val, end_val, divisions, point_index, label_char):
            # start_val е индекс (0 за -2, 1 за -1 итн.)
            x_start = start_x + start_val * step
            width = step
            sub_step = width / divisions
            
            # Цртање мали цртички
            for k in range(1, divisions):
                tick = Line(UP*0.1, DOWN*0.1, color=MK_BLUE, stroke_width=2).move_to(RIGHT * (x_start + k*sub_step))
                sub_ticks.add(tick)
            
            # Цртање точка и буква
            # point_index е која цртичка по ред (1-based)
            p_x = x_start + point_index * sub_step
            dot = Dot(point=RIGHT*p_x, color=MK_RED, radius=0.08)
            points.add(dot)
            
            lbl = MathTex(label_char, color=MK_RED).next_to(dot, UP, buff=0.3)
            point_labels.add(lbl)
            
            arr = Arrow(start=RIGHT*p_x + DOWN*1.0, end=RIGHT*p_x + DOWN*0.2, color=MK_RED, buff=0)
            arrows.add(arr)

        # A: (-2, -1), 5 дела, 3-та цртичка
        add_interval(0, 1, 5, 3, "A")
        
        # B: (-1, 0), 4 дела, 3-та цртичка
        add_interval(1, 2, 4, 3, "B")
        
        # C: (0, 1), 3 дела, 2-ра цртичка
        add_interval(2, 3, 3, 2, "C")
        
        # D: (1, 2), 2 дела, 1-ва цртичка (средина)
        add_interval(3, 4, 2, 1, "D")
        
        # E: (2, 3), 4 дела, 3-та цртичка
        add_interval(4, 5, 4, 3, "E")

        self.add(needle, tip, end, main_ticks, sub_ticks, labels, points, point_labels, arrows)

class KT_Test2_Q6_Candles(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Бои
        YELLOW_CANDLE = "#FFD700"
        GREEN_CANDLE = "#9ACD32" # YellowGreen
        FLAME_OUTER = "#FFA500"
        FLAME_INNER = "#FFFF00"

        # --- ЛЕВА ГРУПА (Жолта) ---
        # Свеќа 1 (Цела)
        y1_body = Rectangle(width=0.6, height=3, color=YELLOW_CANDLE, fill_opacity=1, stroke_width=0)
        # Капки (декорација)
        y1_drips = SVGMobject(os.path.join("assets", "candle_drips.svg")) if os.path.exists("assets/candle_drips.svg") else VGroup() 
        # Ако нема SVG, импровизираме со кругови
        y1_top = Ellipse(width=0.6, height=0.2, color=YELLOW_CANDLE, fill_opacity=1).move_to(y1_body.get_top())
        y1_wick = Line(y1_top.get_center(), y1_top.get_center() + UP*0.4, color=BLACK, stroke_width=2)
        # Пламен
        y1_flame = Ellipse(width=0.3, height=0.6, color=FLAME_OUTER, fill_opacity=0.8).move_to(y1_wick.get_end() + UP*0.3)
        
        y1_group = VGroup(y1_body, y1_top, y1_wick, y1_flame).move_to(LEFT * 4)
        
        # Свеќа 2 (Потрошена)
        # 45 мин од 120 мин = 3/8 потрошено. Останува 5/8.
        h2 = 3 * (5/8)
        y2_body = Rectangle(width=0.6, height=h2, color=YELLOW_CANDLE, fill_opacity=1, stroke_width=0)
        y2_top = Ellipse(width=0.6, height=0.2, color=YELLOW_CANDLE, fill_opacity=1).move_to(y2_body.get_top())
        y2_wick = Line(y2_top.get_center(), y2_top.get_center() + UP*0.4, color=BLACK, stroke_width=2)
        # Изгасен пламен (само фитил)
        
        y2_group = VGroup(y2_body, y2_top, y2_wick).next_to(y1_group, RIGHT, buff=0.5).align_to(y1_group, DOWN)
        
        # Текст за жолта свеќа
        y_text = self.get_text("Жолта свеќа", size=24, color=MK_BLACK)
        y_text.next_to(VGroup(y1_group, y2_group), DOWN)
        y_time = self.get_text("Време: 45 мин", size=18, color=MK_GRAY)
        y_time.next_to(y2_group, RIGHT, buff=0.3).rotate(PI/2)

        # --- ДЕСНА ГРУПА (Зелена) ---
        # Свеќа 3 (Цела)
        g1_body = Rectangle(width=0.6, height=3, color=GREEN_CANDLE, fill_opacity=1, stroke_width=0)
        g1_top = Ellipse(width=0.6, height=0.2, color=GREEN_CANDLE, fill_opacity=1).move_to(g1_body.get_top())
        g1_wick = Line(g1_top.get_center(), g1_top.get_center() + UP*0.4, color=BLACK, stroke_width=2)
        g1_flame = Ellipse(width=0.3, height=0.6, color=FLAME_OUTER, fill_opacity=0.8).move_to(g1_wick.get_end() + UP*0.3)
        
        g1_group = VGroup(g1_body, g1_top, g1_wick, g1_flame).move_to(RIGHT * 2)
        
        # Свеќа 4 (Потрошена)
        # 75 мин од 180 мин = 5/12 потрошено. Останува 7/12.
        h4 = 3 * (7/12)
        g2_body = Rectangle(width=0.6, height=h4, color=GREEN_CANDLE, fill_opacity=1, stroke_width=0)
        g2_top = Ellipse(width=0.6, height=0.2, color=GREEN_CANDLE, fill_opacity=1).move_to(g2_body.get_top())
        g2_wick = Line(g2_top.get_center(), g2_top.get_center() + UP*0.4, color=BLACK, stroke_width=2)
        
        g2_group = VGroup(g2_body, g2_top, g2_wick).next_to(g1_group, RIGHT, buff=0.5).align_to(g1_group, DOWN)
        
        # Текст за зелена свеќа
        g_text = self.get_text("Зелена свеќа", size=24, color=MK_BLACK)
        g_text.next_to(VGroup(g1_group, g2_group), DOWN)
        g_time = self.get_text("Време: 75 мин", size=18, color=MK_GRAY)
        g_time.next_to(g2_group, RIGHT, buff=0.3).rotate(PI/2)

        self.add(y1_group, y2_group, y_text, y_time, g1_group, g2_group, g_text, g_time)
        self.add(g1_group, g2_group, g_text, g_time)