settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");

size(300);

// Квадрат
draw((0,0)--(10,0)--(10,10)--(0,10)--cycle, blue+2);

// Круг
draw(circle((5,5), 3), red+2);

// Македонски текст
label("Квадрат", (5, -0.5));
label("Круг", (5, 5));
label("Математика", (5, 10.5));
