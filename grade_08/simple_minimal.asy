size(500, 200);

pen linePen = black + 1.2;
pen fillPen = rgb(0.4, 0.8, 0.5);

real w = 2.5;
real h = 3.5;
real gap = 1.5;

pair A_pos = (0, 0);

fill(shift(A_pos)*shift(0, 4*h/5)*scale(w/2, h/5)*unitsquare, fillPen);
fill(shift(A_pos)*shift(0, 1*h/5)*scale(w/2, h/5)*unitsquare, fillPen);
fill(shift(A_pos)*shift(w/2, 3*h/5)*scale(w/2, h/5)*unitsquare, fillPen);

draw(shift(A_pos)*scale(w, h)*unitsquare, linePen);
draw(shift(A_pos)*((w/2, 0)--(w/2, h)), linePen);
for(int i=1; i<5; ++i) {
    draw(shift(A_pos)*((0, i*h/5)--(w, i*h/5)), linePen);
}
label("A", (w/2, -0.4));

pair B_pos = (w + gap, 0);
draw(shift(B_pos)*scale(w, h)*unitsquare, linePen);
label("B", B_pos + (w/2, -0.4));

pair C_pos = (2*w + 2*gap, 0);
fill(shift(C_pos)*shift(w/5, 0)*scale(w/5, h)*unitsquare, fillPen);
draw(shift(C_pos)*scale(w, h)*unitsquare, linePen);
for(int i=1; i<5; ++i) {
    draw(shift(C_pos)*((i*w/5, 0)--(i*w/5, h)), linePen);
}
label("C", C_pos + (w/2, -0.4));

path arrowAB = (A_pos.x + w/2, h + 0.2) .. controls (A_pos.x + w/2 + 0.5, h + 1) and (B_pos.x + w/2 - 0.5, h + 1) .. (B_pos.x + w/2 - 0.2, h + 0.2);
draw(arrowAB, black+1.5, Arrow(SimpleHead, size=6));

path arrowCB = (C_pos.x + w/2, h + 0.2) .. controls (C_pos.x + w/2 - 0.5, h + 1) and (B_pos.x + w/2 + 0.5, h + 1) .. (B_pos.x + w/2 + 0.2, h + 0.2);
draw(arrowCB, black+1.5, Arrow(SimpleHead, size=6));
