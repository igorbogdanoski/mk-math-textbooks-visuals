// Тест за Illustrator SVG експорт со македонски текст
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");
texpreamble("\usepackage{lmodern}");

size(400, 300);

// Наслов
label("Македонски Кирилски Текст", (0, 4), fontsize(16pt));

// Координатен систем
draw((-5,0)--(5,0), black+1, Arrow);
draw((0,-3)--(0,3), black+1, Arrow);

label("$x$", (5,0), E, fontsize(12pt));
label("$y$", (0,3), N, fontsize(12pt));
label("$O$", (0,0), SW, fontsize(10pt));

// Круг
draw(circle((0,0), 2), blue+1.5);
fill(circle((0,0), 2), lightblue+opacity(0.2));

// Точки со македонски лабели
dot((2,0), red+5);
label("Точка А", (2,0), SE, fontsize(10pt));

dot((0,2), red+5);
label("Точка Б", (0,2), NE, fontsize(10pt));

dot((-2,0), red+5);
label("Точка В", (-2,0), SW, fontsize(10pt));

// Формула
label("$x^2 + y^2 = 4$", (0, -2.5), fontsize(12pt));
