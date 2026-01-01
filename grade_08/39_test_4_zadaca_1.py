import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE
from manim import *

class KT_Test4_Problem1(TextbookScene):
    def construct(self):
        # 1. Подесување на позадина
        self.camera.background_color = WHITE

        # 2. Креирање на кругот
        circle = Circle(radius=2.5, color=MK_BLUE, stroke_width=4)
        
        # 3. Креирање на линиите за поделба (8 дела)
        lines = VGroup()
        for i in range(4):
            angle = i * (PI / 4) # 0, 45, 90, 135 степени
            line = Line(
                start=circle.point_at_angle(angle),
                end=circle.point_at_angle(angle + PI),
                color=MK_BLUE,
                stroke_width=2
            )
            lines.add(line)

        # 4. Боење на секторите (3 дела)
        # Агол на еден сектор = 360 / 8 = 45 степени = PI/4
        sectors = VGroup()
        for i in range(3):
            # Почнуваме од 90 степени (PI/2) и одиме во насока на стрелките на часовникот
            start_angle = PI/2 - (i + 1) * (PI/4)
            sector = Sector(
                radius=2.5,
                angle=PI/4,
                start_angle=start_angle,
                color=MK_BLUE,
                fill_opacity=0.5, # Полу-транспарентно за да се гледаат линиите
                stroke_width=0
            )
            sectors.add(sector)

        # 5. Групирање и прикажување
        diagram = VGroup(sectors, circle, lines)
        diagram.move_to(ORIGIN)
        
        self.add(diagram)

        # Ова е статична илустрација за тестот, нема анимација.