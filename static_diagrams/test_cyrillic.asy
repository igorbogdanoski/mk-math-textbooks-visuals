size(300);

// Квадрат
draw((0,0)--(10,0)--(10,10)--(0,10)--cycle, blue+2);

// Круг
draw(circle((5,5), 4), red+2);

// Лабели со ASCII
label("$A$", (0,0), SW);
label("$B$", (10,0), SE);
label("Test", (5,5));
