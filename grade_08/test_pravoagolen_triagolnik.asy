// Тест задача: Правоаголен триаголник
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");
texpreamble("\usepackage{lmodern}");

size(400, 300);

// Дефиниција на темињата
pair A = (0, 0);
pair B = (4, 0);
pair C = (0, 3);

// Триаголник
draw(A--B--C--cycle, blue+1.5);

// Темиња
dot(A, red+7);
dot(B, red+7);
dot(C, red+7);

// Лабели за темињата
label("$A$", A, SW);
label("$B$", B, SE);
label("$C$", C, NW);

// Страни со мерки
label("$3$ cm", (A+C)/2, W);
label("$4$ cm", (A+B)/2, S);
label("$5$ cm", (B+C)/2, NE);

// Прав агол
draw((0.3,0)--(0.3,0.3)--(0,0.3), black+1);
label("$90^\circ$", (0.5, 0.5));

// Наслов
label("Правоаголен триаголник", (2, -0.8));
