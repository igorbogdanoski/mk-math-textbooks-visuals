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

class KT_2_25_Visual(TextbookScene):
    """
    Визуелизација: Споредување со константна разлика.
    КОРЕКЦИЈА: Стрелките се поместени десно за да не ги сечат бројките.
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Споредување со константна разлика", size=32, is_bold=True)
        naslov.to_edge(UP)

        # --- ЧЕКОР 1: Дропките ---
        eq_a = self.get_math(r"a = \frac{19}{23}", size=48)
        eq_b = self.get_math(r"b = \frac{31}{35}", size=48)
        eq_c = self.get_math(r"c = \frac{41}{45}", size=48)
        
        fractions = VGroup(eq_a, eq_b, eq_c).arrange(RIGHT, buff=1.5)
        fractions.move_to(UP * 1.5)

        # --- ЧЕКОР 2: Истакнување на разликата ---
        # Стрелки од броител до именител со текст "4"
        
        diff_arrows = VGroup()
        for eq in [eq_a, eq_b, eq_c]:
            # КОРЕКЦИЈА: Ги земаме координатите на десната ивица на дропката
            right_edge_x = eq.get_right()[0]
            top_y = eq.get_top()[1]
            bottom_y = eq.get_bottom()[1]
            
            # Ги дефинираме точките малку подесно (+0.1) од ивицата
            # Малку подолу од врвот (-0.2) и малку погоре од дното (+0.2) за да биде центрирано вертикално
            start_p = [right_edge_x + 0.1, top_y - 0.2, 0]
            end_p = [right_edge_x + 0.1, bottom_y + 0.2, 0]
            
            # Крива стрелка
            arrow = Arrow(start_p, end_p, path_arc=-1.5, color=MK_RED, buff=0).scale(0.6)
            label = self.get_text("4", size=18, color=MK_RED).next_to(arrow, RIGHT, buff=0.05)
            
            diff_arrows.add(VGroup(arrow, label))

        # --- ЧЕКОР 3: Правило (Визуелно) ---
        # Правилни дропки -> Растат
        
        rule_box = VGroup()
        rule_text = self.get_text("Правилни дропки + Иста разлика", size=24, color=MK_BLUE)
        rule_arrow = Arrow(LEFT, RIGHT, color=MK_BLUE)
        rule_result = self.get_text("Поголеми броеви = Поголема дропка", size=24, color=MK_BLUE)
        
        rule_group = VGroup(rule_text, rule_arrow, rule_result).arrange(RIGHT)
        rule_group.move_to(DOWN * 0.5)
        
        # --- ЧЕКОР 4: Споредба ---
        # 19 < 31 < 41
        comp_nums = self.get_math(r"19 < 31 < 41", size=42, color=MK_BLACK)
        comp_nums.next_to(rule_group, DOWN, buff=0.5)
        
        # Заклучок
        final_res = self.get_math(r"a < b < c", size=60, color=MK_BLACK)
        final_box = SurroundingRectangle(final_res, color=MK_BLACK, buff=0.3)
        final_group = VGroup(final_box, final_res).next_to(comp_nums, DOWN, buff=0.5)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(fractions)
        self.add(diff_arrows)
        self.add(rule_group)
        self.add(comp_nums)
        self.add(final_group)