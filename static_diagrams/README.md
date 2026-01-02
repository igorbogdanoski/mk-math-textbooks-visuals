# Статички Дијаграми (Asymptote)

Оваа папка содржи статички математички дијаграми креирани со Asymptote.

## Структура
- `.asy` датотеки - Asymptote изворен код
- `.pdf` датотеки - генерирани дијаграми

## Користење
```bash
& 'C:\Program Files\Asymptote\asy.exe' име_на_датотека.asy
```

## Задолжителен header за кирилица
```asymptote
settings.tex="pdflatex";
settings.outformat="pdf";
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[russian]{babel}");
```

Види `ASYMPTOTE_AI_TEMPLATE.md` за повеќе детали.
