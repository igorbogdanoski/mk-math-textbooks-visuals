// Задолжителен header за кирилица
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");

size(400, 300);

// Увоз на модул за графикони
import graph;

// Дефиниција на функција - парабола
real f(real x) {
    return x^2 - 4*x + 3;
}

// Координатен систем
real xmin = -1, xmax = 5;
real ymin = -2, ymax = 5;

// Цртање оски
xaxis("$x$", xmin, xmax, Arrow);
yaxis("$y$", ymin, ymax, Arrow);

// Цртање grid линии (опционално)
for(real i = 0; i <= 4; ++i) {
    draw((i, ymin)--(i, ymax), gray+0.3);
}
for(real j = -1; j <= 4; ++j) {
    draw((xmin, j)--(xmax, j), gray+0.3);
}

// Цртање на графиконот на функцијата
path parabola = graph(f, xmin, xmax);
draw(parabola, blue+1.5);

// Нулти точки на функцијата (x=1 и x=3)
pair A = (1, 0);
pair B = (3, 0);
dot(A, red+5);
dot(B, red+5);
label("$x_1=1$", A, S);
label("$x_2=3$", B, S);

// Исполнување на површина под крива
path region = graph(f, 1, 3) -- (3,0) -- (1,0) -- cycle;
fill(region, lightblue+opacity(0.3));

// Темињето на параболата (x=2, y=-1)
pair V = (2, f(2));
dot(V, deepgreen+5);
label("Темиње $V(2,-1)$", V, S);

// Вертикална линија низ темето
draw((2, ymin)--(2, f(2)), deepgreen+dashed);

// Пресечна точка со y-оска
pair C = (0, f(0));
dot(C, orange+5);
label("$(0,3)$", C, W);

// Наслов и дополнителни ознаки
label("Графикон на функцијата $f(x) = x^2 - 4x + 3$", (xmax/2, ymax-0.5), fontsize(11pt));

// Легенда за површина
label("Површина", (2, -0.5), blue);
draw((1.3, -0.5)--(1.7, -0.5), blue+1);

// Координати на важни точки
label("Координати:", (-0.8, 3.5), fontsize(9pt));
label("• Темиње: $(2, -1)$", (-0.8, 3), fontsize(8pt), align=E);
label("• Нули: $x_1=1, x_2=3$", (-0.8, 2.5), fontsize(8pt), align=E);
