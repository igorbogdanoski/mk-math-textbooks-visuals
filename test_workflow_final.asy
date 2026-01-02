// TEST WORKFLOW: Правоаголен триаголник
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");
texpreamble("\usepackage{lmodern}");

size(400, 350);

// Наслов
label("Правоаголен Триаголник", (2, -1.2), fontsize(16pt));

// Дефиниција на темињата
pair A = (0, 0);
pair B = (4, 0);
pair C = (0, 3);

// Триаголник - појака линија
draw(A--B--C--cycle, blue+2);

// Темиња - поголеми точки
dot(A, red+7);
dot(B, red+7);
dot(C, red+7);

// Лабели за темињата
label("$A$", A, SW, fontsize(12pt));
label("$B$", B, SE, fontsize(12pt));
label("$C$", C, NW, fontsize(12pt));

// Страни со мерки
label("$a = 3$ cm", (A+C)/2, W, fontsize(11pt));
label("$b = 4$ cm", (A+B)/2, S, fontsize(11pt));
label("$c = 5$ cm", (B+C)/2, NE, fontsize(11pt));

// Прав агол - мала шега
draw((0.4,0)--(0.4,0.4)--(0,0.4), black+1.5);

// Формула - Питагорина теорема
label("$a^2 + b^2 = c^2$", (2, 1.5), fontsize(14pt));
label("$3^2 + 4^2 = 5^2$", (2, 0.8), fontsize(12pt));
label("$9 + 16 = 25$", (2, 0.2), fontsize(11pt));
