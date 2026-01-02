// Задолжителен header за кирилица + SVG output
settings.tex="latex";
settings.outformat="svg";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");

size(500, 400);

// Увоз на модул за графикони
import graph;

// Дефиниција на функција - парабола
real f(real x) {
    return x^2 - 4*x + 3;
}

// Координатен систем
real xmin = -0.5, xmax = 4;
real ymin = -2.5, ymax = 3;

// Цртање оски
xaxis("$x$", xmin, xmax, gray+1, Arrow);
yaxis("$y$", ymin, ymax, gray+1, Arrow);

// Цртање grid линии (опционално)
for(real i = 0; i <= 4; ++i) {
    draw((i, ymin)--(i, ymax), gray+0.3);
}
for(real j = -2; j <= 3; ++j) {
    draw((xmin, j)--(xmax, j), gray+0.3);
}

// Цртање на графиконот на функцијата (од y-оската до симетричната точка)
path parabola = graph(f, 0, 4);
draw(parabola, blue+1.5);

// Нулти точки на функцијата (x=1 и x=3)
pair A = (1, 0);
pair B = (3, 0);
dot(A, red+5);
dot(B, purple+5);
label("$x_1=1$", A, S, fontsize(9pt));
label("$x_2=3$", B, S, fontsize(9pt));

// Исполнување на површина под крива
path region = graph(f, 1, 3) -- (3,0) -- (1,0) -- cycle;
fill(region, lightblue+opacity(0.3));

// Темињето на параболата (x=2, y=-1)
pair V = (2, f(2));
dot(V, darkblue+5);
label("Темиње $V(2,-1)$", V, S, fontsize(9pt));

// Вертикална линија низ темето (оска на симетрија)
draw((2, 0)--(2, f(2)), darkblue+dashed);

// Пресечна точка со y-оска
pair C = (0, f(0));
dot(C, magenta+5);
label("$(0,3)$", C, W, fontsize(9pt));

// Наслов и дополнителни ознаки
label("Графикон на функцијата $f(x) = x^2 - 4x + 3$", (1.75, 2.6), fontsize(11pt));

// Координати на важни точки
label("Координати:", (-0.3, 2.1), fontsize(9pt));
label("$\bullet$ Темиње: $(2, -1)$", (-0.3, 1.75), fontsize(8pt), align=E);
label("$\bullet$ Нули: $x_1=1, x_2=3$", (-0.3, 1.45), fontsize(8pt), align=E);

// Легенда за површина
label("Површина", (2, -0.2), fontsize(10pt));
draw((1.5, -0.2)--(1.8, -0.2), blue+1.5);
