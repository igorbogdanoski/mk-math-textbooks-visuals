// Подесувања за платното
settings.outformat = "png";
settings.render = 16;
size(300);

// Дефинирање на бои и пенкала
pen squarePen = deepblue + 1.5;
pen circlePen = red + 1.5;
pen radiusPen = black + dashed + 1;

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

// Цртање на впишаната кружница
path c = circle(O, r);
fill(c, lightred+opacity(0.2)); // Нежно пополнување
draw(c, circlePen);

// Означување на радиусот и центарот
dot(O, black+4);
draw(O--(O.x + r, O.y), radiusPen);