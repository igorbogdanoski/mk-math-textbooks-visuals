# Водич за Latin Modern фонтови во Word и MathType

## ✅ Инсталирано

Latin Modern фонтовите се успешно инсталирани во Windows!

## 📝 Конфигурација за Word

### 1. Основен текст фонт

1. Отвори Word документ
2. Home → Styles → Normal (десен клик) → Modify
3. Font: **Latin Modern Roman**
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
   - Text: **Latin Modern Roman**
   - Function: **Latin Modern Roman**
   - Variable: **Latin Modern Math Italic**
   - Greek: **Latin Modern Math**
   - Symbol: **Latin Modern Math**
4. OK → OK

## 🎨 Достапни Latin Modern фонтови

### За обичен текст:
- **Latin Modern Roman** - Главен фонт за текст
- **Latin Modern Sans** - Sans-serif варијанта
- **Latin Modern Mono** - Monospace (за код)

### За математика:
- **Latin Modern Math** - За формули и равенки

## 🔄 Проверка на конзистентност

1. Креирај тест документ во Word со Latin Modern Roman
2. Додај формула со Latin Modern Math
3. Генерирај дијаграм со Asymptote (веќе користи lmodern)
4. Спореди ги - требада изгледаат **идентично**

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

✅ Latin Modern Roman → Word текст  
✅ Latin Modern Math → Word/MathType формули  
✅ lmodern package → Asymptote (веќе активен)  
✅ Fontsize 11pt → конзистентна големина  

**Резултат**: Професионален, унифициран изглед низ целиот учебник!
