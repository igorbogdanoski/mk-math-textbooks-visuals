import sys
import os

# --- 1. SETUP PATH ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# --- 2. IMPORTS ---
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN
from manim import (
    Scene, VGroup, MathTex, Text, NumberLine, Line, Arrow, Dot, Circle, 
    SurroundingRectangle, DashedLine, Brace,
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN
)

class KT_2_21_Visual(TextbookScene):
    """
    Визуелизација: Вертикално порамнување со ГРИД систем.
    """
    
    def create_element(self, char, row, col, center_point, color=MK_BLACK, size=60):
        """Креира елемент на точна позиција во мрежата."""
        dx = 0.8  # Хоризонтално растојание
        dy = 1.2  # Вертикално растојание
        
        mob = MathTex(char, font_size=size, color=color)
        
        # Пресметка на позиција
        target_pos = center_point + (RIGHT * col * dx) + (DOWN * row * dy)
        mob.move_to(target_pos)
        
        # Специјална корекција за запирката да биде долу
        if char == "{,}":
            mob.shift(DOWN * 0.2)
            
        return mob

    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Претворање дропка во периодичен број", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Равенката (Горе) ---
        # Тука ја додаваме цртичката за периода: 0,7\overline{36}
        division = self.get_math(r"\frac{81}{110} = 0{,}7\overline{36}...", size=48)
        division.move_to(UP * 2.0)

        # --- ЧЕКОР 2: Грид Систем (Лево) ---
        grid_center = LEFT * 2.0 + UP * 0.5
        
        # Податоци за мрежата: (Ред, Колона, Карактер, Боја)
        # Ред 0: 0 , 7 3 6 ...
        # Ред 1: 0 , a b c ...
        
        grid_data = [
            # Ред 0 (Бројот)
            (0, 0, "0", MK_BLACK), (0, 1, "{,}", MK_BLACK), 
            (0, 2, "7", MK_RED), (0, 3, "3", MK_GREEN), (0, 4, "6", MK_BLUE), (0, 5, "...", MK_BLACK),
            
            # Ред 1 (Променливите)
            (1, 0, "0", MK_BLACK), (1, 1, "{,}", MK_BLACK), 
            (1, 2, "a", MK_RED), (1, 3, "b", MK_GREEN), (1, 4, "c", MK_BLUE), (1, 5, "...", MK_BLACK),
        ]

        grid_group = VGroup()
        elements = {} # За да ги поврземе подоцна

        for r, c, char, color in grid_data:
            el = self.create_element(char, r, c, grid_center, color)
            grid_group.add(el)
            elements[(r, c)] = el

        # --- ЧЕКОР 3: Линии за поврзување ---
        lines = VGroup()
        # Поврзуваме (0,2) со (1,2) -> 7 со a
        lines.add(DashedLine(elements[(0,2)].get_bottom(), elements[(1,2)].get_top(), color=MK_RED))
        # Поврзуваме (0,3) со (1,3) -> 3 со b
        lines.add(DashedLine(elements[(0,3)].get_bottom(), elements[(1,3)].get_top(), color=MK_GREEN))
        # Поврзуваме (0,4) со (1,4) -> 6 со c
        lines.add(DashedLine(elements[(0,4)].get_bottom(), elements[(1,4)].get_top(), color=MK_BLUE))

        # --- ЧЕКОР 4: Резултати (Десно) ---
        val_a = self.get_math("a = 7", size=48, color=MK_RED)
        val_b = self.get_math("b = 3", size=48, color=MK_GREEN)
        val_c = self.get_math("c = 6", size=48, color=MK_BLUE)
        
        values_group = VGroup(val_a, val_b, val_c).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        values_group.next_to(grid_group, RIGHT, buff=2.0)
        
        # Рамка
        box_vals = SurroundingRectangle(values_group, color=MK_BLACK, buff=0.3)

        # --- ЧЕКОР 5: Финален збир (Долу) ---
        final_sum = self.get_math("a + b + c = 7 + 3 + 6 = 16", size=54, color=MK_BLACK)
        final_sum.move_to(DOWN * 2.5)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(division)
        self.add(grid_group)
        self.add(lines)
        self.add(values_group, box_vals)
        self.add(final_sum)