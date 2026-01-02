import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE
from manim import *

class KT_Test3_Q3_Cube(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Параметри за изометриска проекција
        unit = 0.35  # Големина на еден квадар
        angle_x = 30 * DEGREES  
        angle_y = 30 * DEGREES
        
        # Функција за изометриска трансформација
        def iso_transform(x, y, z):
            ix = (x - y) * np.cos(angle_x) * unit
            iy = z * unit + (x + y) * np.sin(angle_y) * unit
            return np.array([ix, iy, 0])
        
        # Креираме коцка од мали квадари 3×4×6
        cubes = VGroup()
        
        for i in range(3):  # Ширина
            for j in range(4):  # Длабочина
                for k in range(6):  # Висина
                    # Темиња на квадарот
                    p000 = iso_transform(i, j, k)
                    p100 = iso_transform(i+1, j, k)
                    p010 = iso_transform(i, j+1, k)
                    p110 = iso_transform(i+1, j+1, k)
                    p001 = iso_transform(i, j, k+1)
                    p101 = iso_transform(i+1, j, k+1)
                    p011 = iso_transform(i, j+1, k+1)
                    p111 = iso_transform(i+1, j+1, k+1)
                    
                    # Предна страна (видлива)
                    front = Polygon(p000, p100, p101, p001, 
                                   color=MK_BLUE, fill_color="#B0D4F1", 
                                   fill_opacity=0.7, stroke_width=1)
                    
                    # Горна страна
                    top = Polygon(p001, p101, p111, p011, 
                                 color=MK_BLUE, fill_color="#E3F2FD", 
                                 fill_opacity=0.9, stroke_width=1)
                    
                    # Десна страна
                    right = Polygon(p100, p110, p111, p101, 
                                   color=MK_BLUE, fill_color="#90CAF9", 
                                   fill_opacity=0.8, stroke_width=1)
                    
                    cube_small = VGroup(front, top, right)
                    cubes.add(cube_small)
        
        cubes.move_to(LEFT * 1.5)
        
        # Извлечен квадар - средишен и затворен
        i, j, k = 1, 1, 2
        p000 = iso_transform(i, j, k)
        p100 = iso_transform(i+1, j, k)
        p010 = iso_transform(i, j+1, k)
        p110 = iso_transform(i+1, j+1, k)
        p001 = iso_transform(i, j, k+1)
        p101 = iso_transform(i+1, j, k+1)
        p011 = iso_transform(i, j+1, k+1)
        p111 = iso_transform(i+1, j+1, k+1)
        
        front_ext = Polygon(p000, p100, p101, p001, 
                           color=MK_RED, fill_color="#FFCDD2", 
                           fill_opacity=0.9, stroke_width=2)
        top_ext = Polygon(p001, p101, p111, p011, 
                         color=MK_RED, fill_color="#EF9A9A", 
                         fill_opacity=0.9, stroke_width=2)
        right_ext = Polygon(p100, p110, p111, p101, 
                           color=MK_RED, fill_color="#E57373", 
                           fill_opacity=0.9, stroke_width=2)
        
        extracted = VGroup(front_ext, top_ext, right_ext)
        extracted.move_to(cubes.get_center() + RIGHT * 2.5 + DOWN * 0.5)
        
        # Стрелка
        arrow = Arrow(cubes.get_right() + UP * 0.5, extracted.get_left(), 
                     color=MK_RED, stroke_width=4, buff=0.2)
        
        self.add(cubes, arrow, extracted)

class KT_Test3_Q4_Flowers(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Саксија 1 (3 цвеќиња)
        pot1 = Polygon([-1, 0, 0], [1, 0, 0], [1.2, 1.5, 0], [-1.2, 1.5, 0], color=MK_GRAY, fill_opacity=1, fill_color="#795548")
        pot1.move_to(LEFT * 3 + DOWN * 1)
        
        flowers1 = VGroup()
        for i in range(3):
            stem = Line(pot1.get_top() + RIGHT*(i-1)*0.5, pot1.get_top() + RIGHT*(i-1)*0.5 + UP*1.5, color=MK_GREEN, stroke_width=4)
            petals = Circle(radius=0.3, color=MK_RED, fill_opacity=1, fill_color="#E91E63").move_to(stem.get_end())
            center = Circle(radius=0.1, color=MK_ORANGE, fill_opacity=1, fill_color="#FFEB3B").move_to(stem.get_end())
            flowers1.add(VGroup(stem, petals, center))
            
        # Саксија 2 (Многу цвеќиња - 10)
        pot2 = pot1.copy().move_to(RIGHT * 3 + DOWN * 1)
        
        flowers2 = VGroup()
        # Распоредуваме 10 цвеќиња во пирамидална форма
        positions = [
            (0, 2.5), 
            (-0.5, 2.0), (0.5, 2.0),
            (-1.0, 1.5), (0, 1.5), (1.0, 1.5),
            (-1.2, 1.0), (-0.4, 1.0), (0.4, 1.0), (1.2, 1.0)
        ]
        
        for x, y in positions:
            stem = Line(pot2.get_top() + RIGHT*x*0.5, pot2.get_top() + RIGHT*x*0.5 + UP*y, color=MK_GREEN, stroke_width=3)
            petals = Circle(radius=0.25, color=MK_RED, fill_opacity=1, fill_color="#E91E63").move_to(stem.get_end())
            center = Circle(radius=0.08, color=MK_ORANGE, fill_opacity=1, fill_color="#FFEB3B").move_to(stem.get_end())
            flowers2.add(VGroup(stem, petals, center))

        self.add(pot1, flowers1, pot2, flowers2)

class KT_Test1_Q7_Cakes(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Торта 1 (8 парчиња)
        slices1 = VGroup()
        colors1 = [MK_RED, MK_BLUE, MK_GREEN, MK_ORANGE, "#FFD700", "#8A2BE2", "#FF69B4", "#00CED1"]
        center1 = LEFT * 3
        radius = 2
        
        for i in range(8):
            angle_start = i * PI/4
            angle_end = (i + 1) * PI/4
            
            # Точки на секторот
            p1 = center1
            p2 = center1 + radius * np.array([np.cos(angle_start), np.sin(angle_start), 0])
            p3 = center1 + radius * np.array([np.cos(angle_end), np.sin(angle_end), 0])
            
            slice_piece = Polygon(p1, p2, p3, color=colors1[i], fill_opacity=0.7, stroke_color=WHITE, stroke_width=3)
            slices1.add(slice_piece)
            
        label1 = self.get_text("I. Торта (8 парчиња)", size=24, color=MK_BLACK).next_to(slices1, UP, buff=0.5)

        # Торта 2 (12 парчиња)
        slices2 = VGroup()
        colors2 = colors1 + ["#A52A2A", "#5F9EA0", "#D2691E", "#DC143C"]
        center2 = RIGHT * 3
        
        for i in range(12):
            angle_start = i * PI/6
            angle_end = (i + 1) * PI/6
            
            # Точки на секторот
            p1 = center2
            p2 = center2 + radius * np.array([np.cos(angle_start), np.sin(angle_start), 0])
            p3 = center2 + radius * np.array([np.cos(angle_end), np.sin(angle_end), 0])
            
            slice_piece = Polygon(p1, p2, p3, color=colors2[i], fill_opacity=0.7, stroke_color=WHITE, stroke_width=3)
            slices2.add(slice_piece)
            
        label2 = self.get_text("II. Торта (12 парчиња)", size=24, color=MK_BLACK).next_to(slices2, UP, buff=0.5)

        self.add(slices1, label1, slices2, label2)

class KT_Test1_Q6_Boxes(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Бои за рамките
        C_BLUE = "#00BFFF"
        C_PINK = "#FF69B4"
        
        # Креирање на еден "мешан број" блок
        def create_mixed_block(color):
            whole = Rectangle(width=1, height=1.5, color=color, stroke_width=4)
            frac_line = Line(LEFT*0.6, RIGHT*0.6, color=MK_BLACK, stroke_width=4).next_to(whole, RIGHT, buff=0.2)
            num = Rectangle(width=1, height=1, color=color, stroke_width=4).next_to(frac_line, UP, buff=0.1)
            den = Rectangle(width=1, height=1, color=color, stroke_width=4).next_to(frac_line, DOWN, buff=0.1)
            return VGroup(whole, frac_line, num, den)

        # Блок 1 (Син)
        b1 = create_mixed_block(C_BLUE).move_to(LEFT * 5)
        
        # Плус
        plus = MathTex("+", color=MK_BLACK, font_size=60).next_to(b1, RIGHT, buff=0.5)
        
        # Блок 2 (Розев)
        b2 = create_mixed_block(C_PINK).next_to(plus, RIGHT, buff=0.5)
        
        # Минус
        minus = MathTex("-", color=MK_BLACK, font_size=60).next_to(b2, RIGHT, buff=0.5)
        
        # Блок 3 (Син)
        b3 = create_mixed_block(C_BLUE).next_to(minus, RIGHT, buff=0.5)
        
        self.add(b1, plus, b2, minus, b3)

class KT_Test1_Q8_Symbols(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Легенда на врвот - секој симбол е операција
        legend_title = self.get_text("Симболите се операции:", size=24, color=MK_GRAY, is_bold=True)
        legend_title.to_edge(UP, buff=0.4)
        
        # Креираме мали симболи за легенда
        pent_leg = RegularPolygon(n=5, color="#ADD8E6", fill_opacity=0.5).scale(0.25)
        tri_leg = Triangle(color="#FF69B4", fill_opacity=0.5).scale(0.25)
        sq_leg = Square(side_length=0.4, color="#90EE90", fill_opacity=0.5)
        circ_leg = Circle(radius=0.2, color="#FF69B4", fill_opacity=0.5)
        
        # Операции
        ops = self.get_math(r"= \{+, -, \cdot, :\}", size=28, color=MK_BLACK)
        
        # Групирање: симбол = {операции}
        legend_content = VGroup(
            pent_leg, ops.copy(),
            tri_leg, ops.copy(),
            sq_leg, ops.copy(),
            circ_leg, ops.copy()
        ).arrange_in_grid(rows=1, cols=8, buff=0.2)
        legend_content.next_to(legend_title, DOWN, buff=0.3)
        
        # Елементи на равенката
        # 2 [pentagon] 3 [triangle] 4 [square] 5 [circle] 6
        # / 1 [triangle] 2
        
        # Форми
        pentagon = RegularPolygon(n=5, color="#ADD8E6", fill_opacity=0.5).scale(0.4)
        triangle = Triangle(color="#FF69B4", fill_opacity=0.5).scale(0.4)
        square = Square(side_length=0.7, color="#90EE90", fill_opacity=0.5)
        circle = Circle(radius=0.35, color="#FF69B4", fill_opacity=0.5)
        
        # Броеви
        n2 = MathTex("2", color=MK_BLACK, font_size=48)
        n3 = MathTex("3", color=MK_BLACK, font_size=48)
        n4 = MathTex("4", color=MK_BLACK, font_size=48)
        n5 = MathTex("5", color=MK_BLACK, font_size=48)
        n6 = MathTex("6", color=MK_BLACK, font_size=48)
        
        # Горен ред
        top_row = VGroup(
            n2, pentagon, n3, triangle.copy(), n4, square, n5, circle, n6
        ).arrange(RIGHT, buff=0.2)
        top_row.shift(DOWN * 0.8)
        
        # Дробна црта
        line = Line(top_row.get_left(), top_row.get_right(), color=MK_BLACK, stroke_width=2).next_to(top_row, DOWN, buff=0.2)
        
        # Долен ред
        n1_bot = MathTex("1", color=MK_BLACK, font_size=48)
        n2_bot = MathTex("2", color=MK_BLACK, font_size=48)
        bot_row = VGroup(n1_bot, triangle.copy(), n2_bot).arrange(RIGHT, buff=0.2).next_to(line, DOWN, buff=0.2)
        
        # = X
        eq_x = MathTex("= X", color=MK_BLACK, font_size=48).next_to(line, RIGHT, buff=0.3)
        
        self.add(legend_title, legend_content, top_row, line, bot_row, eq_x)

        import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE
from manim import *

class KT_Test3_Q3_Cube_Corrected(TextbookScene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Бои (Светло сина со градиент ефект симулиран со opacity)
        CUBE_COLOR = "#B0E0E6" # PowderBlue
        LINE_COLOR = "#404040" # Dark Gray
        
        # Димензии на главната коцка (Визуелни)
        W = 4.0  # Ширина на екранот
        H = 4.0  # Висина на екранот
        # Вектор за длабочина (за 2.5D ефект)
        D_VEC = UP * 1.0 + RIGHT * 1.5 
        
        # Број на поделби според задачата (НЗС=12 -> 2,3,4)
        # Предна страна: 4 колони (12/3), 6 редови (12/2)
        COLS = 4
        ROWS = 6
        # Длабочина: 3 слоја (12/4)
        DEPTHS = 3

        # --- 1. ГЛАВНА КОЦКА ---
        
        # Предна страна (Правоаголник)
        front_face = Rectangle(width=W, height=H, color=LINE_COLOR, stroke_width=2)
        front_face.set_fill(CUBE_COLOR, opacity=0.8)
        
        # Линии на предната страна
        front_lines = VGroup()
        # Вертикални
        for i in range(1, COLS):
            x = -W/2 + i * (W/COLS)
            line = Line(UP*H/2 + RIGHT*x, DOWN*H/2 + RIGHT*x, color=LINE_COLOR, stroke_width=1.5)
            front_lines.add(line)
        # Хоризонтални
        for i in range(1, ROWS):
            y = -H/2 + i * (H/ROWS)
            line = Line(LEFT*W/2 + UP*y, RIGHT*W/2 + UP*y, color=LINE_COLOR, stroke_width=1.5)
            front_lines.add(line)

        # Горна страна (Паралелограм)
        fl_corner = front_face.get_corner(UL) # Front-Left
        fr_corner = front_face.get_corner(UR) # Front-Right
        bl_corner = fl_corner + D_VEC         # Back-Left
        br_corner = fr_corner + D_VEC         # Back-Right
        
        top_face = Polygon(fl_corner, fr_corner, br_corner, bl_corner, color=LINE_COLOR, stroke_width=2)
        top_face.set_fill(CUBE_COLOR, opacity=0.6) # Малку посветла
        
        # Линии на горната страна
        top_lines = VGroup()
        # Линии паралелни со длабочината (продолжение на вертикалните)
        for i in range(1, COLS):
            x = -W/2 + i * (W/COLS)
            start = UP*H/2 + RIGHT*x
            end = start + D_VEC
            top_lines.add(Line(start, end, color=LINE_COLOR, stroke_width=1.5))
        # Линии паралелни со ширината (поделба на длабочината)
        for i in range(1, DEPTHS):
            alpha = i / DEPTHS
            p1 = fl_corner + D_VEC * alpha
            p2 = fr_corner + D_VEC * alpha
            top_lines.add(Line(p1, p2, color=LINE_COLOR, stroke_width=1.5))

        # Десна страна (Паралелограм)
        fr_bot = front_face.get_corner(DR)
        br_bot = fr_bot + D_VEC
        
        side_face = Polygon(fr_corner, br_corner, br_bot, fr_bot, color=LINE_COLOR, stroke_width=2)
        side_face.set_fill(CUBE_COLOR, opacity=0.4) # Најтемна (сенка)
        
        # Линии на десната страна
        side_lines = VGroup()
        # Линии паралелни со длабочината (продолжение на хоризонталните)
        for i in range(1, ROWS):
            y = -H/2 + i * (H/ROWS)
            start = RIGHT*W/2 + UP*y
            end = start + D_VEC
            side_lines.add(Line(start, end, color=LINE_COLOR, stroke_width=1.5))
        # Вертикални линии (поделба на длабочината)
        for i in range(1, DEPTHS):
            alpha = i / DEPTHS
            p1 = fr_corner + D_VEC * alpha
            p2 = fr_bot + D_VEC * alpha
            side_lines.add(Line(p1, p2, color=LINE_COLOR, stroke_width=1.5))

        # Групирање на големата коцка
        big_cube = VGroup(front_face, top_face, side_face, front_lines, top_lines, side_lines)
        big_cube.move_to(LEFT * 2)

        # --- 2. МАЛА ПРИЗМА (ИЗВАДЕНА) ---
        
        # Димензии на малата призма (пропорционални)
        sW = W / COLS
        sH = H / ROWS
        sD_VEC = D_VEC / DEPTHS
        
        # Мала предна
        s_front = Rectangle(width=sW, height=sH, color=LINE_COLOR, stroke_width=2)
        s_front.set_fill(CUBE_COLOR, opacity=0.8)
        
        # Мала горна
        s_fl = s_front.get_corner(UL)
        s_fr = s_front.get_corner(UR)
        s_bl = s_fl + sD_VEC
        s_br = s_fr + sD_VEC
        s_top = Polygon(s_fl, s_fr, s_br, s_bl, color=LINE_COLOR, stroke_width=2)
        s_top.set_fill(CUBE_COLOR, opacity=0.6)
        
        # Мала десна
        s_fr_bot = s_front.get_corner(DR)
        s_br_bot = s_fr_bot + sD_VEC
        s_side = Polygon(s_fr, s_br, s_br_bot, s_fr_bot, color=LINE_COLOR, stroke_width=2)
        s_side.set_fill(CUBE_COLOR, opacity=0.4)
        
        small_prism = VGroup(s_front, s_top, s_side)
        small_prism.move_to(RIGHT * 3)
        
        # --- 3. ЕЛЕМЕНТИ ЗА ПОВРЗУВАЊЕ ---
        
        arrow = Arrow(big_cube.get_right(), small_prism.get_left(), color=MK_RED, stroke_width=4)
        
        label_cube = self.get_text("Голема коцка", size=24).next_to(big_cube, DOWN)
        label_prism = self.get_text("Една призма", size=24).next_to(small_prism, DOWN)

        self.add(big_cube, small_prism, arrow, label_cube, label_prism)