# Водич за Latin Modern фонтови во Word и MathType

## ✅ Инсталирано

✅ Сите 72 Latin Modern фонтови се инсталирани во Windows!

⚠️ **ВАЖНО**: Фонтовите се регистрирани со технички имиња:
- **LMRoman10-Regular** (наместо "Latin Modern Roman")
- **LMSans10-Regular** (наместо "Latin Modern Sans") 
- **LMMono10-Regular** (наместо "Latin Modern Mono")

## 📝 Конфигурација за Word

### 1. Основен текст фонт

1. Отвори Word документ
2. Home → Styles → Normal (десен клик) → Modify
3. Font: **LMRoman10-Regular** (или пребарај "LMRoman")
4. Size: **11pt**
5. OK

### 2. Математички фонт за равенки

**За Word built-in equation editor:**
1. Insert → Equation
2. Design tab → Tools → Equation Options
3. Math Font: **Latin Modern Math**
4. OK

**За MathType:**
1. MathType → Preferences → Cut and Copy Preferences
2. Equation for application or website: **MathML or TeX**
3. Style → Define
   - Text: **LMRoman10-Regular**
   - Function: **LMRoman10-Regular**
   - Variable: **LMRoman10-Italic**
   - Greek: **Latin Modern Math**
   - Symbol: **Latin Modern Math**
4. OK → OK

## 🎨 Достапни Latin Modern фонтови

### За обичен текст (инсталирани како кориснички фонтови):
- **LMRoman10-Regular** - Главен фонт за текст
- **LMRoman10-Bold** - Bold варијанта
- **LMRoman10-Italic** - Italic варијанта
- **LMRoman10-BoldItalic** - Bold + Italic
- **LMSans10-Regular** - Sans-serif варијанта
- **LMMono10-Regular** - Monospace (за код)

### За математика:
- **Latin Modern Math** - За формули и равенки (system-wide)

## 🔄 Проверка на конзистентност

1. Креирај тест документ во Word со **LMRoman10-Regular**
2. Додај формула со **Latin Modern Math**
3. Генерирај дијаграм со Asymptote (веќе користи lmodern)
4. Спореди ги - требада изгледаат **идентично**

### Како да ги најдеш фонтовите во Word:
- Во Font dropdown, пребарај **"LMRoman"** или **"LM"**
- Ќе ги видиш како: LMRoman10-Regular, LMRoman10-Bold, итн.

## 📐 Asymptote template (веќе конфигуриран)

```asymptote
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");
texpreamble("\usepackage{lmodern}");  // ✓ Latin Modern

size(500, 400);
label("Текст", (0,0), fontsize(11pt));  // ✓ Иста големина како Word
```

## 💡 Алтернатива: Cambria (Microsoft стандард)

Ако Latin Modern прави проблеми:
- Word текст: **Cambria** 11pt
- Word математика: **Cambria Math** (веќе инсталиран)
- Asymptote: Остани на lmodern (близок стил)

## 🎯 Резиме

✅ **LMRoman10-Regular** → Word текст (пребарај "LMRoman")  
✅ **Latin Modern Math** → Word/MathType формули  
✅ **lmodern package** → Asymptote (веќе активен)  
✅ **Fontsize 11pt** → конзистентна големина  
✅ **72 фонтови** инсталирани како кориснички фонтови

**Резултат**: Професионален, унифициран изглед низ целиот учебник!
