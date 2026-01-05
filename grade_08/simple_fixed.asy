settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");
texpreamble("\usepackage{lmodern}");

size(500, 200); // Поширок canvas за трите форми

// Дефинирање на бои
pen linePen = black + 1.2;
pen fillPen = rgb(0.4, 0.8, 0.5); // Светло зелена како на сликата

// Димензии на правоаголниците
real w = 2.5; // ширина
real h = 3.5; // висина
real gap = 1.5; // растојание меѓу нив

// --- ПРАВОАГОЛНИК A (Лево) ---
pair A_pos = (0, 0);

// Пополнување на A (мрежа 2x5)
// Обоени полиња според сликата: (колона, ред) - 0-индексирано од долу-лево
// Сликата има обоено:
// Лева колона: најгоре (4), средина-долу (1)
// Десна колона: втора одозгора (3)
fill(shift(A_pos)*shift(0, 4*h/5)*scale(w/2, h/5)*unitsquare, fillPen); // Лево горе
fill(shift(A_pos)*shift(0, 1*h/5)*scale(w/2, h/5)*unitsquare, fillPen); // Лево долу
fill(shift(A_pos)*shift(w/2, 3*h/5)*scale(w/2, h/5)*unitsquare, fillPen); // Десно

// Рамка и мрежа за A
draw(shift(A_pos)*scale(w, h)*unitsquare, linePen);
draw(shift(A_pos)*((w/2, 0)--(w/2, h)), linePen); // Вертикална поделба
for(int i=1; i<5; ++i) {
    draw(shift(A_pos)*((0, i*h/5)--(w, i*h/5)), linePen); // Хоризонтални линии
}
label("A", A_pos + (w/2, -0.4), fontsize(12pt));


// --- ПРАВОАГОЛНИК B (Средина) ---
pair B_pos = (w + gap, 0);

// Рамка за B (празен)
draw(shift(B_pos)*scale(w, h)*unitsquare, linePen);
label("B", B_pos + (w/2, -0.4), fontsize(12pt));


// --- ПРАВОАГОЛНИК C (Десно) ---
pair C_pos = (2*w + 2*gap, 0);

// Пополнување на C (5 вертикални ленти)
// Обоена е втората лента од лево
fill(shift(C_pos)*shift(w/5, 0)*scale(w/5, h)*unitsquare, fillPen);

// Рамка и мрежа за C
draw(shift(C_pos)*scale(w, h)*unitsquare, linePen);
for(int i=1; i<5; ++i) {
    draw(shift(C_pos)*((i*w/5, 0)--(i*w/5, h)), linePen); // Вертикални линии
}
label("C", C_pos + (w/2, -0.4), fontsize(12pt));


// --- СТРЕЛКИ ---
// Стрелка од A до B
path arrowAB = (A_pos.x + w/2, h + 0.2) .. controls (A_pos.x + w/2 + 0.5, h + 1) and (B_pos.x + w/2 - 0.5, h + 1) .. (B_pos.x + w/2 - 0.2, h + 0.2);
draw(arrowAB, black+1.5, Arrow(SimpleHead, size=6));

// Стрелка од C до B
path arrowCB = (C_pos.x + w/2, h + 0.2) .. controls (C_pos.x + w/2 - 0.5, h + 1) and (B_pos.x + w/2 + 0.5, h + 1) .. (B_pos.x + w/2 + 0.2, h + 0.2);
draw(arrowCB, black+1.5, Arrow(SimpleHead, size=6));
