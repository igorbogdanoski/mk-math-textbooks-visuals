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

class KT_Test1_Q3_Visual(TextbookScene):
    """
    Визуелизација на двојни дропки (Задача 3).
    КОРЕКЦИЈА: Знакот = е перфектно порамнет со главната дробна црта.
    """
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("Внимавај на главната дробна црта!", size=32, is_bold=True)
        naslov.to_edge(UP)

        # ==========================================
        # ЛЕВА СТРАНА: (2/3) / 7
        # ==========================================
        
        # 1. Креирање на елементите
        num1 = self.get_math(r"\frac{2}{3}", size=42, color=MK_BLUE)
        den1 = self.get_math("7", size=42)
        line1 = Line(LEFT, RIGHT, color=BLACK).match_width(num1).scale(1.5)
        
        # 2. Групирање на дропката
        double_frac1 = VGroup(num1, line1, den1).arrange(DOWN, buff=0.15)
        
        # 3. Резултат
        res1 = self.get_math(r"= \frac{2}{3} \cdot \frac{1}{7} = \frac{2}{21}", size=42, color=MK_BLUE)
        
        # 4. Првично позиционирање (десно од дропката)
        res1.next_to(double_frac1, RIGHT, buff=0.3)
        
        # 5. --- КЛУЧНА КОРЕКЦИЈА ЗА ПОРАМНУВАЊЕ ---
        # Го наоѓаме знакот "=" (тој е првиот елемент res1[0][0])
        # Пресметуваме колку треба да се помести за да биде на иста висина со линијата
        y_diff = line1.get_center()[1] - res1[0][0].get_center()[1]
        res1.shift(UP * y_diff)
        
        # Групирање на целата лева страна
        group_left = VGroup(double_frac1, res1)

        # ==========================================
        # ДЕСНА СТРАНА: 2 / (3/7)
        # ==========================================
        
        # 1. Креирање
        num2 = self.get_math("2", size=42)
        den2 = self.get_math(r"\frac{3}{7}", size=42, color=MK_RED)
        line2 = Line(LEFT, RIGHT, color=BLACK).match_width(den2).scale(1.5)
        
        # 2. Групирање
        double_frac2 = VGroup(num2, line2, den2).arrange(DOWN, buff=0.15)
        
        # 3. Резултат
        res2 = self.get_math(r"= 2 \cdot \frac{7}{3} = \frac{14}{3}", size=42, color=MK_RED)
        
        # 4. Првично позиционирање
        res2.next_to(double_frac2, RIGHT, buff=0.3)
        
        # 5. --- КЛУЧНА КОРЕКЦИЈА ЗА ПОРАМНУВАЊЕ ---
        y_diff2 = line2.get_center()[1] - res2[0][0].get_center()[1]
        res2.shift(UP * y_diff2)
        
        group_right = VGroup(double_frac2, res2)

        # ==========================================
        # ГЛАВЕН РАСПОРЕД
        # ==========================================
        
        # Ги ставаме двете групи една до друга
        # Користиме align_to за да ги порамниме по главните црти, а не по центрите
        group_right.next_to(group_left, RIGHT, buff=1.5)
        # Фино подесување: ги порамнуваме line1 и line2 да бидат на иста висина
        group_right.shift(UP * (line1.get_center()[1] - line2.get_center()[1]))
        
        # Ги центрираме заедно на екранот (малку погоре)
        total_group = VGroup(group_left, group_right)
        total_group.move_to(UP * 1.0)

        # ==========================================
        # ФИНАЛНА ПРЕСМЕТКА (Средина)
        # ==========================================
        
        final_eq = self.get_math(
            r"\frac{2}{21} - \frac{14}{3} = \frac{2 - 98}{21} = -\frac{96}{21} = -\frac{32}{7}", 
            size=48
        )
        final_box = SurroundingRectangle(final_eq, color=MK_BLACK, buff=0.2)
        
        final_group = VGroup(final_box, final_eq).next_to(total_group, DOWN, buff=1.0)

        # ==========================================
        # ТЕКСТ ЗА ПОЈАСНУВАЊЕ (Најдолу)
        # ==========================================
        note = self.get_text(
            "Главната црта е секогаш подолга и е во линија со знакот =", 
            size=24, 
            color=MK_GRAY
        )
        note.next_to(final_group, DOWN, buff=0.5)

        # --- ДОДАВАЊЕ НА СЦЕНА ---
        self.add(naslov)
        self.add(total_group)
        self.add(final_group)
        self.add(note)