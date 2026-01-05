size(500, 200);

real w = 2.5;
real h = 3.5;
real gap = 1.5;

// Rectangle A
draw(box((0,0), (w,h)));
draw((w/2, 0)--(w/2, h));
for(int i=1; i<5; ++i) {
    draw((0, i*h/5)--(w, i*h/5));
}
fill(box((0, 4*h/5), (w/2, h)), lightgreen);
fill(box((0, h/5), (w/2, 2*h/5)), lightgreen);
fill(box((w/2, 3*h/5), (w, 4*h/5)), lightgreen);

// Rectangle B
draw(shift(w+gap, 0)*box((0,0), (w,h)));

// Rectangle C
draw(shift(2*w+2*gap, 0)*box((0,0), (w,h)));
fill(shift(2*w+2*gap, 0)*box((w/5, 0), (2*w/5, h)), lightgreen);
for(int i=1; i<5; ++i) {
    draw(shift(2*w+2*gap, 0)*((i*w/5, 0)--(i*w/5, h)));
}
