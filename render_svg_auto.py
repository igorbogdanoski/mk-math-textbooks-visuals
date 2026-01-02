"""
Целосна автоматизација: Asymptote → PDF → SVG со Create Outlines
Користи Illustrator scripting за автоматска конверзија
"""

import subprocess
import sys
import os
from pathlib import Path
import time

def render_asy_to_svg_auto(asy_file):
    """
    Целосна автоматизација без рачна интеракција
    """
    asy_path = Path(asy_file)
    
    if not asy_path.exists():
        print(f"❌ Фајлот не постои: {asy_file}")
        return False
    
    # 1. Генерирај PDF
    asy_exe = r"C:\Program Files\Asymptote\asy.exe"
    
    print(f"🔨 Рендерирам {asy_path.name}...")
    
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
        
        pdf_file = asy_path.with_suffix('.pdf')
        
        if not pdf_file.exists():
            print(f"❌ PDF не е креиран")
            return False
        
        print(f"✅ PDF креиран: {pdf_file.name}")
        
        # 2. Креирај JSX script за овој конкретен фајл
        jsx_content = f'''
#target illustrator

try {{
    var pdfFile = new File("{str(pdf_file).replace(chr(92), '/')}");
    var svgFile = new File("{str(pdf_file.with_suffix('.svg')).replace(chr(92), '/')}");
    
    // Отвори PDF
    var doc = app.open(pdfFile);
    
    // Select All
    doc.selectObjectsOnActiveArtboard();
    
    // Create Outlines
    try {{
        app.executeMenuCommand('outline');
    }} catch (e) {{}}
    
    // SVG Export Options
    var options = new ExportOptionsSVG();
    options.embedRasterImages = true;
    options.embedAllFonts = false;
    options.fontSubsetting = SVGFontSubsetting.None;
    options.documentEncoding = SVGDocumentEncoding.UTF8;
    options.cssProperties = SVGCSSPropertyLocation.PRESENTATIONATTRIBUTES;
    options.decimalPrecision = 3;
    
    // Export
    doc.exportFile(svgFile, ExportType.SVG, options);
    
    // Затвори
    doc.close(SaveOptions.DONOTSAVECHANGES);
    
    alert("✅ SVG креиран: " + svgFile.name);
}} catch (e) {{
    alert("❌ Грешка: " + e.message);
}}
'''
        
        jsx_file = asy_path.parent / f"{asy_path.stem}_convert.jsx"
        with open(jsx_file, 'w', encoding='utf-8') as f:
            f.write(jsx_content)
        
        print(f"📝 JSX script креиран: {jsx_file.name}")
        
        # 3. Изврши Illustrator script
        illustrator_exe = r"C:\Program Files\Adobe\Adobe Illustrator 2026\Support Files\Contents\Windows\Illustrator.exe"
        
        if not Path(illustrator_exe).exists():
            print(f"❌ Illustrator не е пронајден")
            print(f"📂 Отвори рачно: {pdf_file}")
            return False
        
        print(f"🎨 Стартување на Illustrator...")
        print(f"⏳ Ова може да потрае 10-15 секунди...")
        
        # Стартувај Illustrator со script
        subprocess.Popen([illustrator_exe, "-scriptfile", str(jsx_file)])
        
        # Почекај script да заврши
        svg_file = pdf_file.with_suffix('.svg')
        max_wait = 30  # 30 секунди
        waited = 0
        
        while waited < max_wait:
            if svg_file.exists():
                print(f"✅ SVG автоматски креиран: {svg_file.name}")
                
                # Избриши го привремениот JSX
                try:
                    jsx_file.unlink()
                except:
                    pass
                
                # Отвори во browser
                print(f"📂 Отварање во browser...")
                os.startfile(str(svg_file))
                
                return True
            
            time.sleep(1)
            waited += 1
        
        print(f"⚠️ Timeout - SVG не е креиран автоматски")
        print(f"📋 Провери го Illustrator и зачувај рачно како SVG")
        
        return False
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Употреба: python render_svg_auto.py <file.asy>")
        sys.exit(1)
    
    asy_file = sys.argv[1]
    render_asy_to_svg_auto(asy_file)


if __name__ == "__main__":
    main()
