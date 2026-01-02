# LaTeX Учебник Template - Водич за користење

## 📚 Структура на template-от

`textbook_template.tex` содржи:
- ✅ Кирилична поддршка (македонски + руски)
- ✅ Latin Modern фонтови
- ✅ Математички пакети (amsmath, amsthm)
- ✅ Asymptote интеграција
- ✅ TikZ за едноставни дијаграми
- ✅ Обоени боксови за примери
- ✅ Теореми, дефиниции, вежби

## 🚀 Како да компајлираш

### Во TeXstudio:
1. Отвори `textbook_template.tex`
2. Tools → Build & View (F5)
3. Автоматски ќе генерира PDF

### Од командна линија:
```bash
pdflatex textbook_template.tex
pdflatex textbook_template.tex  # Два пати за TOC
```

## 📐 Како да вметнеш Asymptote дијаграм

### 1. Креирај дијаграм:
```bash
cd static_diagrams
asy kompleksen_primer.asy
```

### 2. Вклучи го во LaTeX:
```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{kompleksen_primer.pdf}
\caption{Опис на дијаграмот}
\label{fig:my_diagram}
\end{figure}
```

### 3. Референцирај го:
```latex
Од Слика~\ref{fig:my_diagram} може да се види...
```

## 🎨 Обоени боксови

### Пример бокс (зелен):
```latex
\begin{examplebox}
Пресметај: $2 + 2 = 4$

\textbf{Решение:} ...
\end{examplebox}
```

### Забелешка бокс (син):
```latex
\begin{notebox}
Важно е да се знае дека...
\end{notebox}
```

## 📊 Теореми и дефиниции

```latex
\begin{definition}[Наслов]
Дефиниција на...
\end{definition}

\begin{theorem}
Ако $a = b$, тогаш...
\end{theorem}

\begin{exercise}
Реши:
\begin{enumerate}
    \item Прв проблем
    \item Втор проблем
\end{enumerate}
\end{exercise}
```

## 🖼️ TikZ inline дијаграми

```latex
\begin{tikzpicture}
    \draw[->] (0,0) -- (5,0) node[right] {$x$};
    \draw[->] (0,0) -- (0,3) node[above] {$y$};
    \fill[red] (2,1) circle (2pt);
\end{tikzpicture}
```

## 🔧 Custom команди

Веќе дефинирани:
```latex
\N  % Природни броеви ℕ
\Z  % Цели броеви ℤ
\Q  % Рационални броеви ℚ
\R  % Реални броеви ℝ
```

Користење:
```latex
Ако $x \in \R$, тогаш...
```

## 📁 Препорачана структура

```
mk-math-textbooks-visuals/
├── textbook_grade08.tex          ← Главен документ
├── chapters/
│   ├── 01_rational_numbers.tex
│   ├── 02_quadratic_functions.tex
│   └── 03_geometry.tex
├── static_diagrams/               ← Asymptote датотеки
│   ├── parabola.asy
│   ├── parabola.pdf
│   └── circle.asy
└── generated/                     ← LaTeX output
    └── textbook_grade08.pdf
```

### Главен документ (`textbook_grade08.tex`):
```latex
\documentclass[11pt,a4paper]{book}
% ... preamble од template ...

\begin{document}
\maketitle
\tableofcontents

\include{chapters/01_rational_numbers}
\include{chapters/02_quadratic_functions}

\end{document}
```

## 💡 Best Practices

1. **Еден .tex фајл по глава** - Полесно за едитирање
2. **Asymptote дијаграми одвоено** - Не ги компајлирај секој пат
3. **Користи `\label{}` и `\ref{}`** - За автоматски референци
4. **Два пати `pdflatex`** - За точни TOC и референци
5. **Користи Latin Modern** - Конзистентност со Asymptote

## 🎯 Брзи тестови

### Тест 1: Кирилица
```latex
Македонски текст: АБВГДЃЕЖЗЅИЈКЛЉМНЊОПРСТЌУФХЦЧЏШ

$f(x) = x^2$ ← Математика треба да работи
```

### Тест 2: Asymptote дијаграм
```latex
\includegraphics[width=0.5\textwidth]{kompleksen_primer.pdf}
```

### Тест 3: TikZ
```latex
\begin{tikzpicture}
\draw[red] (0,0) circle (1cm);
\end{tikzpicture}
```

## 📖 Следни чекори

1. Компајлирај `textbook_template.tex` во TeXstudio
2. Прегледај го резултатот
3. Адаптирај го за твојот учебник
4. Креирај одвоени chapters за секоја глава
5. Вклучи ги Asymptote дијаграмите од `static_diagrams/`

Успех! 🎓
