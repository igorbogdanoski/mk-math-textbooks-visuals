// Adobe Illustrator Script за автоматска конверзија PDF → SVG
// Оваа скрипта автоматски:
// 1. Отвора PDF
// 2. Create Outlines на целиот текст
// 3. Зачувува како SVG со оптимални подесувања

#target illustrator

function convertPdfToSvg(pdfPath, svgPath) {
    try {
        // Отвори PDF
        var doc = app.open(new File(pdfPath));
        
        // Select All
        doc.selectObjectsOnActiveArtboard();
        
        // Create Outlines на селектираниот текст
        try {
            app.executeMenuCommand('outline');
        } catch (e) {
            // Игнорирај ако нема текст
        }
        
        // SVG Export Options
        var options = new ExportOptionsSVG();
        options.embedRasterImages = true;
        options.embedAllFonts = false;  // Не е потребно, имаме outlines
        options.fontSubsetting = SVGFontSubsetting.None;
        options.documentEncoding = SVGDocumentEncoding.UTF8;
        options.cssProperties = SVGCSSPropertyLocation.PRESENTATIONATTRIBUTES;
        options.decimalPrecision = 3;
        options.coordinatePrecision = 3;
        
        // Зачувај како SVG
        var svgFile = new File(svgPath);
        doc.exportFile(svgFile, ExportType.SVG, options);
        
        // Затвори без зачувување на .ai
        doc.close(SaveOptions.DONOTSAVECHANGES);
        
        return true;
    } catch (e) {
        alert("Грешка: " + e.message);
        return false;
    }
}

// Main execution
if (app.documents.length > 0) {
    // Ако е отворен документ, обработи го
    var doc = app.activeDocument;
    var docPath = doc.fullName.fsName;
    var svgPath = docPath.replace(/\.pdf$/i, '.svg');
    
    convertPdfToSvg(docPath, svgPath);
} else {
    alert("Отвори PDF фајл прво!");
}
