import os

# --- ШАБЛОН ЗА НОВ ФАЈЛ (Содржи сè што е потребно за да нема грешки) ---
TEMPLATE_NEW_FILE = """import sys
import os

# --- 1. SETUP PATH ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# --- 2. IMPORTS ---
from common.style import TextbookScene, MK_BLUE, MK_RED, MK_BLACK, MK_GRAY, MK_GREEN, MK_ORANGE
from manim import (
    Scene, VGroup, MathTex, Text, NumberLine, Line, Arrow, Dot, Circle, 
    SurroundingRectangle, DashedLine, Brace,
    RIGHT, LEFT, UP, DOWN, DL, UR, UL, DR, WHITE, BLACK, RED, BLUE, ORIGIN,
    FadeOut, Write, Create, Indicate, TransformFromCopy, Wait
)

# ==========================================
# ТЕМА: {topic_name}
# ==========================================

class {class_name}(TextbookScene):
    \"\"\"
    Визуелизација за: {topic_name}
    \"\"\"
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("{topic_name}", size=32, is_bold=True)
        naslov.to_edge(UP)
        self.add(naslov)

        # Твојот код тука...
"""

# --- ШАБЛОН ЗА ДОДАВАЊЕ НОВА КЛАСА ВО ПОСТОЕЧКИ ФАЈЛ ---
TEMPLATE_APPEND_CLASS = """

class {class_name}(TextbookScene):
    \"\"\"
    Визуелизација за: {topic_name}
    \"\"\"
    def construct(self):
        # 1. Наслов
        naslov = self.get_text("{topic_name}", size=32, is_bold=True)
        naslov.to_edge(UP)
        self.add(naslov)

        # Твојот код тука...
"""

def main():
    print("🆕 КРЕАТОР НА НОВИ ЗАДАЧИ (v3.0 - Full Imports)")
    print("===============================================")
    
    # 1. Избери одделение
    grades = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('grade_')]
    grades.sort()
    
    if not grades:
        print("❌ Нема папки 'grade_XX'.")
        return

    print("\n📂 Достапни одделенија:")
    for i, g in enumerate(grades):
        print(f"{i + 1}. {g}")
    
    try:
        g_idx = int(input("👉 Избери број: ")) - 1
        selected_grade = grades[g_idx]
    except:
        print("❌ Невалиден избор.")
        return

    # 2. Внеси податоци
    print("\n📝 Детали за задачата:")
    filename = input("   Име на фајл (пр. 22_racionalni_broevi): ").strip()
    if not filename.endswith(".py"):
        filename += ".py"
    
    class_name = input("   Име на Класа (пр. KT_2_22_Visual): ").strip()
    topic_name = input("   Наслов на лекција (пр. Споредување дропки): ").strip()

    # 3. Креирање или Ажурирање
    full_path = os.path.join(selected_grade, filename)
    
    if os.path.exists(full_path):
        print(f"\n⚠️ Фајлот '{filename}' веќе постои.")
        choice = input("   Дали сакаш да ја додадеме новата класа најдолу? (d/n): ")
        if choice.lower() in ['d', 'da', 'y', 'yes']:
            with open(full_path, "a", encoding="utf-8") as f:
                f.write(TEMPLATE_APPEND_CLASS.format(topic_name=topic_name, class_name=class_name))
            print(f"✅ Успешно додадена класа '{class_name}'!")
        else:
            print("❌ Прекинато.")
    else:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(TEMPLATE_NEW_FILE.format(topic_name=topic_name, class_name=class_name))
        print(f"✅ Успешно креиран нов фајл: {full_path}")

if __name__ == "__main__":
    main()