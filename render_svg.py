"""
Asymptote → SVG Render Script за Illustrator
Генерира PDF со вградени фонтови, потоа автоматски отвара во Illustrator
"""

import subprocess
import sys
import os
from pathlib import Path
import time

def render_asymptote_for_illustrator(asy_file):
    """
    Рендерира Asymptote фајл во PDF со вградени фонтови,
    потоа отвара во Adobe Illustrator за SVG експорт
    """
    asy_path = Path(asy_file)
    
    if not asy_path.exists():
        print(f"❌ Фајлот не постои: {asy_file}")
        return False
    
    # Пат до Asymptote
    asy_exe = r"C:\Program Files\Asymptote\asy.exe"
    
    if not Path(asy_exe).exists():
        print(f"❌ Asymptote не е пронајден на: {asy_exe}")
        return False
    
    print(f"🔨 Рендерирам {asy_path.name}...")
    
    # Генерирај PDF со вградени фонтови
    try:
        result = subprocess.run(
            [asy_exe, str(asy_path)],
            cwd=str(asy_path.parent),
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            print(f"❌ Грешка при рендерирање:")
            print(result.stderr)
            return False
        
        # Провери дали е креиран PDF
        pdf_file = asy_path.with_suffix('.pdf')
        
        if not pdf_file.exists():
            print(f"❌ PDF не е креиран: {pdf_file}")
            return False
        
        print(f"✅ PDF креиран: {pdf_file.name}")
        
        # Најди Illustrator
        illustrator_paths = [
            r"C:\Program Files\Adobe\Adobe Illustrator 2026\Support Files\Contents\Windows\Illustrator.exe",
            r"C:\Program Files\Adobe\Adobe Illustrator 2025\Support Files\Contents\Windows\Illustrator.exe",
            r"C:\Program Files\Adobe\Adobe Illustrator 2024\Support Files\Contents\Windows\Illustrator.exe",
            r"C:\Program Files\Adobe\Adobe Illustrator 2023\Support Files\Contents\Windows\Illustrator.exe",
        ]
        
        illustrator_exe = None
        for path in illustrator_paths:
            if Path(path).exists():
                illustrator_exe = path
                break
        
        if illustrator_exe:
            print(f"🎨 Отварам во Illustrator и автоматски конвертирам...")
            
            # Отвори PDF во Illustrator
            subprocess.Popen([illustrator_exe, str(pdf_file)])
            
            # Почекај малку да се вчита Illustrator
            time.sleep(3)
            
            # Изврши .jsx script за автоматска конверзија
            jsx_script = asy_path.parent / "pdf_to_svg_auto.jsx"
            
            if jsx_script.exists():
                try:
                    # Изврши Illustrator script
                    subprocess.run(
                        [illustrator_exe, str(pdf_file), str(jsx_script)],
                        timeout=30
                    )
                    
                    svg_file = pdf_file.with_suffix('.svg')
                    if svg_file.exists():
                        print(f"✅ SVG автоматски креиран: {svg_file.name}")
                    else:
                        print(f"⚠️ SVG не е креиран автоматски")
                        print(f"📋 Рачни чекори во Illustrator:")
                        print(f"   1. Ctrl+A → Ctrl+Shift+O (Create Outlines)")
                        print(f"   2. File → Save As → SVG")
                except Exception as e:
                    print(f"⚠️ Автоматска конверзија не успеа: {e}")
                    print(f"📋 Рачни чекори во Illustrator:")
                    print(f"   1. Ctrl+A → Ctrl+Shift+O (Create Outlines)")
                    print(f"   2. File → Save As → SVG")
            else:
                print(f"✅ Готово! PDF е отворен во Illustrator")
                print(f"\n📋 Следни чекори во Illustrator:")
                print(f"   1. Ctrl+A → Ctrl+Shift+O (Create Outlines)")
                print(f"   2. File → Save As → SVG")
        else:
            print(f"⚠️ Illustrator не е пронајден автоматски")
            print(f"📂 Отвори рачно: {pdf_file}")
            os.startfile(str(pdf_file))
        
        return True
        
    except subprocess.TimeoutExpired:
        print(f"❌ Timeout при рендерирање")
        return False
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False


def render_svg_alternative(asy_file):
    """
    Алтернатива: Рендерира директно во SVG (без кирилична поддршка)
    """
    asy_path = Path(asy_file)
    
    # Прочитај го фајлот
    with open(asy_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Направи SVG верзија
    svg_content = content.replace(
        'settings.outformat="pdf";',
        'settings.outformat="svg";'
    )
    
    temp_file = asy_path.parent / f"{asy_path.stem}_svg.asy"
    
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"🔨 Рендерирам SVG (без кирилична поддршка)...")
    
    asy_exe = r"C:\Program Files\Asymptote\asy.exe"
    
    try:
        result = subprocess.run(
            [asy_exe, str(temp_file)],
            cwd=str(temp_file.parent),
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            svg_file = temp_file.with_suffix('.svg')
            print(f"✅ SVG креиран: {svg_file.name}")
            print(f"⚠️ ВАЖНО: Кириличните фонтови можеби нема да се прикажат правилно!")
            return True
        else:
            print(f"❌ Грешка: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False
    finally:
        # Избриши го temp фајлот
        if temp_file.exists():
            temp_file.unlink()


def main():
    if len(sys.argv) < 2:
        print("Употреба: python render_svg.py <file.asy> [--svg-direct]")
        print("\nОпции:")
        print("  --svg-direct    Рендерира директно во SVG (без кирилична поддршка)")
        print("  (default)       Рендерира PDF → отвора во Illustrator")
        sys.exit(1)
    
    asy_file = sys.argv[1]
    use_svg_direct = '--svg-direct' in sys.argv
    
    if use_svg_direct:
        render_svg_alternative(asy_file)
    else:
        render_asymptote_for_illustrator(asy_file)


if __name__ == "__main__":
    main()
