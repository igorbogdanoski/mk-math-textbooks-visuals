# Asymptote Template за AI Генерирање на Математички Дијаграми

## Основна Структура за Asymptote со Македонски Текст

```asymptote
// ЗАДОЛЖИТЕЛЕН Header за поддршка на македонски кирилски текст
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");

// Големина на canvas
size(300);

// ТВОЈОТ КОД ТУКА
```

## Основни Команди

### 1. Цртање Линии
```asymptote
draw((0,0)--(5,0), black+1);  // Хоризонтална линија
draw((0,0)--(0,5), black+1);  // Вертикална линија
```

### 2. Цртање Геометриски Форми
```asymptote
// Круг
draw(circle((5,5), 3), red+2);

// Правоаголник
draw((0,0)--(10,0)--(10,5)--(0,5)--cycle, blue+1.5);

// Триаголник
draw((0,0)--(5,0)--(2.5,4)--cycle, green+1);
```

### 3. Полнење со Боја
```asymptote
// Полнење со транспарентна боја
fill(circle((5,5), 3), lightblue+opacity(0.3));

// Полнење без транспарентност
fill((0,0)--(5,0)--(2.5,4)--cycle, lightgreen);
```

### 4. Додавање Текст/Лабели
```asymptote
// Едноставна лабела
label("Точка А", (0,0), SW);

// Лабела со LaTeX математика
label("$x^2 + y^2 = r^2$", (5,5));

// Лабела со поголем фонт
label("Наслов", (5,10), fontsize(14pt));
```

### 5. Точки и Маркери
```asymptote
dot((0,0), red+5);           // Црвена точка
dot((5,5), blue+linewidth(3)); // Сина точка
```

### 6. Стрелки
```asymptote
draw((0,0)--(5,0), Arrow);           // Стрелка на крај
draw((0,1)--(5,1), Arrows);          // Стрелки на оба краја
draw((0,2)--(5,2), red+1, Arrow(6)); // Поголема стрелка
```

### 7. Бои
```asymptote
// Основни бои: black, white, red, green, blue, yellow, cyan, magenta
// Светли варијанти: lightred, lightblue, lightgreen, lightyellow
// Темни варијанти: darkred, darkblue, darkgreen

// Комбинации
draw((0,0)--(5,0), red+1.5);      // Црвена со дебелина 1.5
draw((0,1)--(5,1), blue+dashed);  // Сина испрекината
draw((0,2)--(5,2), green+dotted); // Зелена со точки
```

### 8. Позиции на Лабели
```asymptote
// N (North), S (South), E (East), W (West)
// NE, NW, SE, SW (комбинации)
label("Север", (5,5), N);
label("Југ", (5,5), S);
label("Исток", (5,5), E);
label("Запад", (5,5), W);
```

## Примери за Чести Математички Дијаграми

### Пример 1: Координатен Систем
```asymptote
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");

size(300);

// Оски
draw((-5,0)--(5,0), Arrow);
draw((0,-5)--(0,5), Arrow);

// Лабели на оските
label("$x$", (5,0), E);
label("$y$", (0,5), N);
label("$O$", (0,0), SW);

// Точки
dot((3,2), red+5);
label("$A(3,2)$", (3,2), NE);
```

### Пример 2: Геометриска Фигура со Лабели
```asymptote
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");

size(300);

// Квадрат
pair A = (0,0);
pair B = (4,0);
pair C = (4,4);
pair D = (0,4);

draw(A--B--C--D--cycle, blue+1.5);
fill(A--B--C--D--cycle, lightblue+opacity(0.2));

// Темиња
dot(A, red+5); label("$A$", A, SW);
dot(B, red+5); label("$B$", B, SE);
dot(C, red+5); label("$C$", C, NE);
dot(D, red+5); label("$D$", D, NW);

// Страни
label("$a=4$", (A+B)/2, S);
```

### Пример 3: Функција
```asymptote
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");

size(300);

import graph;

// Оски
draw((-1,0)--(5,0), Arrow);
draw((0,-1)--(0,5), Arrow);
label("$x$", (5,0), E);
label("$y$", (0,5), N);

// Функција
real f(real x) { return x^2; }
draw(graph(f, 0, 2), red+1.5);

label("$y = x^2$", (1.5, 3), red);
```

## Напомени за AI

1. **Секогаш користи го header-от** за македонски текст (првите 5 линии)
2. **За LaTeX математика** користи `$...$` внатре во label()
3. **За обичен македонски текст** директно го пиши (пр. `label("Круг", ...)`)
4. **Генерирај PDF** не PNG за најдобар квалитет на текстот
5. **Координатен систем** - центарот е (0,0), оските одат во сите насоки
6. **Бои и стил** - секогаш додавај `+linewidth(N)` за дебелина на линија

## Команда за Генерирање

```powershell
# Зачувај код во фајл (пр. diagram.asy)
# Потоа изврши:
& "C:\Program Files\Asymptote\asy.exe" diagram.asy

# Ова креира diagram.pdf кој можеш да го отвориш
```

## Брзи Референци

| Што | Синтакса |
|-----|----------|
| Линија | `draw((x1,y1)--(x2,y2), pen)` |
| Круг | `draw(circle((cx,cy), r), pen)` |
| Точка | `dot((x,y), pen)` |
| Текст | `label("text", (x,y), dir)` |
| Полнење | `fill(path, pen)` |
| Стрелка | `draw(path, Arrow)` |

---

**ВАЖНО**: Кога генерираш код, МОРА да го вклучиш header-ot за македонски текст, инаку ќе има грешки!
