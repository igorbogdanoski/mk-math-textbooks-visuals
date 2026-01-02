import os
import subprocess
import platform

def open_file(path):
    """Отвора фајл во default апликација."""
    print(f"🖼️ Се отвора: {path}")
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.call(["open", path])
    else:
        subprocess.call(["xdg-open", path])

def main():
    print("🎨 ASYMPTOTE RENDERER 🎨")
    print("========================")
    
    # Додај нов Ghostscript во PATH
    import os
    gs_path = r"C:\Program Files\gs\gs10.06.0\bin"
    if os.path.exists(gs_path):
        os.environ["PATH"] = gs_path + os.pathsep + os.environ.get("PATH", "")
        print("✅ Ghostscript 10.06.0 додаден во PATH")
    else:
        print("⚠️ Ghostscript 10.06.0 не е пронајден, користам системски...")

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
    except:
        return

    # 2. Избери фајл
    files = [f for f in os.listdir(selected_grade) if f.endswith('.asy')]
    if not files:
        print("❌ Нема .asy фајлови.")
        return

    print(f"\n📄 .asy фајлови во {selected_grade}:")
    for i, f in enumerate(files):
        print(f"{i + 1}. {f}")
    
    try:
        f_idx = int(input("👉 Избери број: ")) - 1
        selected_file = files[f_idx]
        file_path = os.path.join(selected_grade, selected_file)
    except:
        return

    # 3. Рендирање
    print(f"\n🚀 Компајлирам во PDF...")
    
    # Оди во директориумот каде е фајлот
    original_dir = os.getcwd()
    os.chdir(selected_grade)
    
    # Компајлирај во PDF
    result = subprocess.run(["asy", "-f", "pdf", selected_file])
    
    # Врати се назад
    os.chdir(original_dir)
    
    if result.returncode == 0:
        # Најди го генерираниот PDF
        pdf_name = selected_file.replace('.asy', '.pdf')
        pdf_path = os.path.join(selected_grade, pdf_name)
        
        if os.path.exists(pdf_path):
            print(f"✅ Успешно генериран: {pdf_name}")
            open_file(os.path.abspath(pdf_path))
        else:
            print(f"⚠️ PDF не е пронајден: {pdf_path}")
    else:
        print("\n❌ Грешка при компајлирањето.")

if __name__ == "__main__":
    main()
