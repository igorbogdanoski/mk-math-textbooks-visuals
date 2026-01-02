// Тест со појаки бои за SVG
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");
texpreamble("\usepackage{lmodern}");

size(400, 300);

// Наслов
label("Македонски Кирилски Текст", (0, 4), fontsize(16pt));

// Координатен систем - појаки линии
draw((-5,0)--(5,0), black+1.5, Arrow);
draw((0,-3)--(0,3), black+1.5, Arrow);

label("$x$", (5,0), E, fontsize(12pt));
label("$y$", (0,3), N, fontsize(12pt));
label("$O$", (0,0), SW, fontsize(10pt));

// Круг - појака боја и дебелина
draw(circle((0,0), 2), blue+2);
fill(circle((0,0), 2), lightblue+opacity(0.4));  // Појака транспарентност

// Точки со македонски лабели - поголеми
dot((2,0), red+7);
label("Точка А", (2,0), SE, fontsize(11pt));

dot((0,2), red+7);
label("Точка Б", (0,2), NE, fontsize(11pt));

dot((-2,0), red+7);
label("Точка В", (-2,0), SW, fontsize(11pt));

// Формула
label("$x^2 + y^2 = 4$", (0, -2.5), fontsize(12pt));
