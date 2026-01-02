
#target illustrator

try {
    var pdfFile = new File("test_illustrator_vibrant.pdf");
    var svgFile = new File("test_illustrator_vibrant.svg");
    
    // Отвори PDF
    var doc = app.open(pdfFile);
    
    // Select All
    doc.selectObjectsOnActiveArtboard();
    
    // Create Outlines
    try {
        app.executeMenuCommand('outline');
    } catch (e) {}
    
    // SVG Export Options
    var options = new ExportOptionsSVG();
    options.embedRasterImages = true;
    options.embedAllFonts = false;
    options.fontSubsetting = SVGFontSubsetting.None;
    options.documentEncoding = SVGDocumentEncoding.UTF8;
    options.cssProperties = SVGCSSPropertyLocation.PRESENTATIONATTRIBUTES;
    options.decimalPrecision = 3;
    
    // Export
    doc.exportFile(svgFile, ExportType.SVG, options);
    
    // Затвори
    doc.close(SaveOptions.DONOTSAVECHANGES);
    
    alert("✅ SVG креиран: " + svgFile.name);
} catch (e) {
    alert("❌ Грешка: " + e.message);
}
