// Задолжителен header за кирилица
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");

// Подесувања за платното
settings.render = 16;
size(300);

// Дефинирање на бои и пенкала
pen squarePen = blue + 1.5;
pen circlePen = red + 1.5;
pen radiusPen = black + dashed + 1;
pen labelPen = black;

// Дефинирање на променливи
real a = 10; // Страна на квадратот
real r = a/2; // Радиус

// Дефинирање на точки
pair A = (0,0);
pair B = (a,0);
pair C = (a,a);
pair D = (0,a);
pair O = (a/2, a/2); // Центар

// Цртање на квадратот
draw(A--B--C--D--cycle, squarePen);
label("$10$", (A+B)/2, S, labelPen); // Ознака за страната

// Цртање на впишаната кружница
path c = circle(O, r);
fill(c, red+opacity(0.2)); // Нежно пополнување
draw(c, circlePen);

// Означување на радиусот и центарот
dot(O, black+4);
draw(O--(O.x + r, O.y), radiusPen);
label("$r=5$", (O.x + r/2, O.y), N, fontsize(10pt));

// Означување на темињата (опционално, за контекст)
label("$A$", A, SW);
label("$B$", B, SE);
label("$C$", C, NE);
label("$D$", D, NW);

// Додавање на наслов (во LaTeX стил преку Asymptote)
label("Впишана кружница", (a/2, -2), fontsize(12pt));
