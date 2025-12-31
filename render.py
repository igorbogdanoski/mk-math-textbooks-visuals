import os
import sys
import subprocess
import re
import platform
import ast

def check_syntax(file_path):
    """Проверува синтакса пред извршување."""
    print(f"🕵️ Вршам валидација на кодот...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source = f.read()
        ast.parse(source)
        print("✅ Синтаксата е исправна!")
        return True
    except SyntaxError as e:
        print("\n" + "="*40)
        print(f"❌ ГРЕШКА ВО КОДОТ (Syntax Error)!")
        print(f"📄 Фајл: {os.path.basename(file_path)}")
        print(f"📍 Линија: {e.lineno}")
        print(f"👉 Твојот код: {e.text.strip() if e.text else '?'}")
        print(f"⚠️ Опис: {e.msg}")
        print("="*40 + "\n")
        return False
    except Exception as e:
        print(f"⚠️ Неочекувана грешка при валидација: {e}")
        return False

def list_scenes(file_path):
    scenes = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        matches = re.findall(r'class\s+(\w+)\(TextbookScene\):', content)
        return matches

def open_file(path):
    print(f"🖼️ Се отвора: {path}")
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.call(["open", path])
    else:
        subprocess.call(["xdg-open", path])

def find_and_open_image(scene_name):
    search_dir = "media"
    if not os.path.exists(search_dir):
        return

    print(f"🔍 Ја барам сликата за '{scene_name}'...")
    found_path = None
    
    # --- ПОПРАВКАТА Е ТУКА ---
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            # Бараме фајл што ПОЧНУВА со името на сцената и завршува на .png
            # Ова ќе го фати и "Scene.png" и "Scene_ManimCE_v0.19.1.png"
            if file.startswith(scene_name) and file.endswith(".png"):
                found_path = os.path.join(root, file)
                break
        if found_path:
            break
    # -------------------------

    if found_path:
        open_file(os.path.abspath(found_path))
    else:
        print(f"⚠️ Сликата не е пронајдена автоматски. Провери во папка 'media'.")

def main():
    print("🎨 MK-MATH-VISUALS INTELLIGENT RENDERER 🎨")
    print("===========================================")

    # 1. Избери одделение
    grades = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('grade_')]
    if not grades:
        print("❌ Нема папки 'grade_XX'.")
        return

    print("\n📂 Достапни одделенија:")
    for i, g in enumerate(grades):
        print(f"{i + 1}. {g}")
    
    try:
        g_idx = int(input("👉 Избери број: ")) - 1
        selected_grade = grades[g_idx]
    except: return

    # 2. Избери фајл
    files = [f for f in os.listdir(selected_grade) if f.endswith('.py') and f != '__init__.py']
    if not files:
        print("❌ Нема фајлови.")
        return

    print(f"\n📄 Фајлови во {selected_grade}:")
    for i, f in enumerate(files):
        print(f"{i + 1}. {f}")
    
    try:
        f_idx = int(input("👉 Избери број: ")) - 1
        selected_file = os.path.join(selected_grade, files[f_idx])
    except: return

    # Валидација
    if not check_syntax(selected_file):
        print("🛑 Процесот е запрен поради грешка во кодот.")
        return

    # 3. Избери Сцена
    scenes = list_scenes(selected_file)
    if not scenes:
        print("❌ Нема сцени.")
        return

    print(f"\n🎬 Достапни задачи:")
    for i, s in enumerate(scenes):
        print(f"{i + 1}. {s}")
    
    try:
        s_idx = int(input("👉 Избери број: ")) - 1
        selected_scene = scenes[s_idx]
    except: return

    # 4. Рендирање
    print(f"\n🚀 Генерирање на: {selected_scene} (4K)...")
    
    cmd = [
        "manim", "-s", "--resolution", "2160,3840", 
        selected_file, selected_scene
    ]
    
    result = subprocess.run(cmd)

    if result.returncode == 0:
        find_and_open_image(selected_scene)
    else:
        print("\n❌ Грешка при Manim генерирањето.")

if __name__ == "__main__":
    main()