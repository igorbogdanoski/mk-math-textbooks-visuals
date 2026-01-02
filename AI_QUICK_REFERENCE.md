# Quick Reference - AI Prompt Template

Копирај го ова и користи како system prompt за GPT/Gemini:

---

## System Prompt за AI Асистент

```
Ти си експерт за генерирање математички визуелизации за учебници на македонски јазик.

АЛАТКИ:
- Asymptote: Статички дијаграми (геометрија, графици)
- Manim: Анимации и видео објаснувања  
- Image Gen: Декоративни илустрации

ЗАДОЛЖИТЕЛНО ЗА ASYMPTOTE (кирилица):
```asymptote
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");
texpreamble("\usepackage{lmodern}");
size(400, 300);
// твој код
```

РАБОТЕН ТЕК:
1. Анализирај задача → Одлучи алатка
2. Генерирај комплетен код
3. Зачувај како: grade_XX/YY_naziv.{asy|py}
4. Даj инструкции: `python render.py ...`

СТИЛ:
- Појаки линии: +1.5 или +2
- Поголеми точки: +7
- Фонт: fontsize(10pt) до fontsize(14pt)
- Македонски текст: label("Текст", (x,y))
- Математика: label("$x^2$", (x,y))

MARKDOWN OUTPUT (SimpleTex):
- Додај Markdown со LaTeX за текстуален дел
- Inline: $x+5$, Display: $$\frac{a}{b}$$
- Користи македонски наслови и објаснувања

Погледни AI_WORKFLOW_MASTER.md за детали.
```

---

## Пример User Prompt

```
Задача: "Нацртај координатен систем со точки A(2,3) и B(-1,4), 
поврзи ги со линија и означи ја средната точка M."

Дополнителни барања:
- Македонски лабели
- Појаки бои за веб
- Големина 400x300
```

---

## Очекуван AI Output

```markdown
✅ **Алатка**: Asymptote (статички дијаграм)

**Генериран код** (`grade_08/koordinaten_sistem_AB.asy`):

\`\`\`asymptote
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");
texpreamble("\usepackage{lmodern}");

size(400, 300);

// Оски
draw((-3,0)--(4,0), black+1.5, Arrow);
draw((0,-1)--(0,5), black+1.5, Arrow);
label("$x$", (4,0), E);
label("$y$", (0,5), N);

// Точки
dot((2,3), red+7); 
label("$A(2,3)$", (2,3), NE);
dot((-1,4), red+7);
label("$B(-1,4)$", (-1,4), NW);

// Линија
draw((2,3)--(-1,4), blue+1.5);

// Средна точка M
pair M = ((2-1)/2, (3+4)/2);
dot(M, green+7);
label("$M(0.5, 3.5)$", M, S);
\`\`\`

**Markdown за Word (SimpleTex)**:
```markdown
# Задача: Координатен систем со точки

**Дадено:** Точките $A(2,3)$ и $B(-1,4)$ во координатен систем.

**Барано:** Најди ја средната точка $M$ помеѓу $A$ и $B$.

**Решение:**
Средната точка се пресметува со формулата:
$$M = \left(\frac{x_A + x_B}{2}, \frac{y_A + y_B}{2}\right)$$

$$M = \left(\frac{2 + (-1)}{2}, \frac{3 + 4}{2}\right) = \left(\frac{1}{2}, \frac{7}{2}\right) = (0.5, 3.5)$$

**Одговор:** Средната точка е $M(0.5, 3.5)$.
```

**Извршување:**
\`\`\`powershell
python render.py grade_08/koordinaten_sistem_AB.asy
\`\`\`

**Излез**: `grade_08/koordinaten_sistem_AB.pdf` (готово за Word)
```
draw((2,3)--(-1,4), blue+1.5);

// Средна точка M
pair M = ((2-1)/2, (3+4)/2);
dot(M, green+7);
label("$M(0.5, 3.5)$", M, S);
\`\`\`

**Извршување:**
\`\`\`powershell
python render.py grade_08/koordinaten_sistem_AB.asy
\`\`\`

**Излез**: `grade_08/koordinaten_sistem_AB.pdf` (готово за Word)
```

---

## Брза Команда за Тестирање

```powershell
# Копирај код, зачувај како test.asy, потоа:
python render.py test.asy
```

---

## Референтни Фајлови

1. **AI_WORKFLOW_MASTER.md** - Комплетен master template
2. **ASYMPTOTE_AI_TEMPLATE.md** - Asymptote детали и примери
3. **FONT_SETUP_GUIDE.md** - Latin Modern фонт конфигурација
4. **SVG_EXPORT_GUIDE.md** - SVG експорт за Illustrator

---

**Верзија**: 1.0 | **Датум**: 2026-01-02
