// Minimal test
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");
texpreamble("\usepackage{lmodern}");

size(400, 300);

// Samo triagolnik
pair A = (0, 0);
pair B = (4, 0);
pair C = (0, 3);

draw(A--B--C--cycle, blue+2);

dot(A, red+7);
dot(B, red+7);
dot(C, red+7);

label("Test", (2, 1.5));
