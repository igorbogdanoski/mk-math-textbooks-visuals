// Illustrator Script за брза конверзија PDF → SVG
// КАК ДА ГО КОРИСТИШ:
// 1. Отвори PDF во Illustrator
// 2. File → Scripts → Other Script...
// 3. Избери го овој .jsx фајл
// 4. ГОТОВО!

// @ts-nocheck
#target illustrator

function quickPdfToSvg() {
    if (app.documents.length == 0) {
        alert("❌ Отвори PDF фајл прво!");
        return;
    }
    
    var doc = app.activeDocument;
    
    // Select All
    app.executeMenuCommand('selectall');
    
    // Create Outlines
    try {
        app.executeMenuCommand('outline');
        alert("✅ Create Outlines завршено!");
    } catch (e) {
        alert("⚠️ Нема текст за конверзија");
    }
    
    // Прашај каде да зачува
    var docPath = doc.fullName;
    var svgPath = docPath.toString().replace(/\.pdf$/i, '.svg');
    var svgFile = new File(svgPath);
    
    // SVG Export Options
    var options = new ExportOptionsSVG();
    options.embedRasterImages = true;
    options.embedAllFonts = false;
    options.fontSubsetting = SVGFontSubsetting.None;
    options.documentEncoding = SVGDocumentEncoding.UTF8;
    options.cssProperties = SVGCSSPropertyLocation.PRESENTATIONATTRIBUTES;
    options.decimalPrecision = 3;
    options.coordinatePrecision = 3;
    
    // Export
    try {
        doc.exportFile(svgFile, ExportType.SVG, options);
        alert("✅ SVG зачуван како:\n" + svgFile.name);
    } catch (e) {
        alert("❌ Грешка при зачувување:\n" + e.message);
    }
    
    // Затвори без зачувување
    doc.close(SaveOptions.DONOTSAVECHANGES);
}

// Изврши
quickPdfToSvg();
