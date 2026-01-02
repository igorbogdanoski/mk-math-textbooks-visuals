// Test bez kirilica
settings.tex="pdflatex";
settings.outformat="pdf";

size(400);

// Teminja
pair A = (0, 0);
pair B = (4, 0);
pair C = (0, 3);

// Triagolnik
draw(A--B--C--cycle, blue+1.5);

// Tochki
dot(A, red+7);
dot(B, red+7);
dot(C, red+7);

// Labeli
label("$A$", A, SW);
label("$B$", B, SE);
label("$C$", C, NW);

// Strani
label("$3$", (A+C)/2, W);
label("$4$", (A+B)/2, S);
label("$5$", (B+C)/2, NE);

// Prav agol
draw((0.3,0)--(0.3,0.3)--(0,0.3), black+1);
