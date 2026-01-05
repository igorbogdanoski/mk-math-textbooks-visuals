---
description: Repository Information Overview
alwaysApply: true
---

# MK Math Textbooks Visuals

## Summary

Educational mathematics visualization project for Macedonian math textbooks. Generates animated lessons and static diagrams for grades 6-12 using Manim animations and Asymptote geometry diagrams. Includes LaTeX support with XeLaTeX for Cyrillic text rendering.

## Repository Structure

- **grade_06/ - grade_12/** - Organized lesson animations per grade level (51+ Python files)
- **static_diagrams/** - Mathematical diagrams created with Asymptote (.asy files)
- **animations/** - Documentation for animation workflows
- **common/** - Shared style definitions and utilities (style.py with TextbookScene base class)
- **media/** - Generated output directory (videos, images, PDFs)
- **assets/** - Static resource files
- **.zencoder/, .zenflow/** - Workflow and AI tool configurations
- **Root utilities** - render.py, create_task.py, new_lesson.py for project management

## Language & Runtime

**Language**: Python  
**Version**: 3.8+ (supports .venv and .venv312)  
**Build System**: None (script-based project)  
**Package Manager**: pip

## Dependencies

**Main Dependencies**:
- **manim** - Animation engine for mathematical visualizations
- **numpy** - Numerical computing (manim dependency)
- **matplotlib** - Plotting library (manim dependency)  
- **PIL/Pillow** - Image processing (manim dependency)

**System Dependencies**:
- **Asymptote** (C:\Program Files\Asymptote\asy.exe) - Static diagram generation
- **XeLaTeX** - LaTeX compiler with Unicode/Cyrillic support (for MathTex rendering)
- **Adobe Illustrator** (optional) - SVG conversion and editing

## Setup & Installation

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install Manim
pip install manim
```

**System Requirements**:
- Install Asymptote from official website
- Install LaTeX with XeLaTeX compiler
- Configure Arial font for Cyrillic support

## Main Files & Entry Points

**Utility Scripts**:
- **render.py** - Interactive CLI for rendering selected Manim scenes to 4K (2160×3840) PNG
- **create_task.py** - Interactive task creator with templates for new lessons
- **new_lesson.py** - Example Manim lesson demonstrating decimal subtraction with borrowing
- **render_svg.py** - Convert Asymptote diagrams to SVG via PDF and Illustrator
- **render_svg_auto.py** - Automated SVG rendering pipeline
- **render_asy.py** - Direct Asymptote rendering

**Core Configuration**:
- **common/style.py** - TextbookScene base class, color constants, LaTeX template with XeLaTeX configuration for Cyrillic

**Templates**:
- **textbook_template.tex** - LaTeX document template for textbooks
- **ASYMPTOTE_AI_TEMPLATE.md** - Asymptote code patterns and best practices
- **LATEX_TEMPLATE_GUIDE.md** - LaTeX and Cyrillic setup guide
- **SVG_EXPORT_GUIDE.md** - SVG export workflow documentation

## Animation Framework

**Technology Stack**:
- Manim CE (Community Edition) for 2D animations
- Custom TextbookScene extending manim.Scene
- Support for:
  - Mathematical text rendering (MathTex with XeLaTeX)
  - Cyrillic text via Arial font
  - Standard shapes, lines, animations from manim library
  - Custom color palette (MK_BLUE, MK_RED, MK_GREEN, MK_ORANGE, MK_BLACK, MK_GRAY)

**Rendering Outputs**:
- PNG images (standard and 4K resolution)
- MP4 videos (from Manim render)
- Media directory: auto-organized by scene name

## Testing & Validation

**Code Validation**:
- **Syntax checking** via ast.parse() in render.py before execution
- Error reporting with line numbers and context

**Quality Assurance**:
- Manual scene inspection through interactive renderer
- Auto-opening of rendered output for visual verification
- Linting guides in documentation (AI_WORKFLOW_MASTER.md, AI_QUICK_REFERENCE.md)

**Rendering Commands**:
```bash
# Interactive rendering (recommended)
python render.py

# Direct Manim rendering (4K output)
manim -s --resolution 2160,3840 grade_08/lesson.py SceneName

# Asymptote rendering
'C:\Program Files\Asymptote\asy.exe' file.asy

# Quick preview (low quality)
manim -pql grade_08/lesson.py SceneName
```

## Project Conventions

**Naming Conventions**:
- Files: `[number]_[topic].py` (e.g., 14_decimalni_broevi.py)
- Classes: PascalCase extending TextbookScene (e.g., KT_2_14_Vezba_1)
- Scenes must inherit from TextbookScene defined in common/style.py

**Code Style**:
- Cyrillic comments and variable names throughout
- UTF-8 encoding required (enforced in file headers)
- Magic numbers avoided through config constants in style.py

**Documentation**:
- Macedonian language throughout codebase
- Guides in .md files: ASYMPTOTE_AI_TEMPLATE.md, SVG_EXPORT_GUIDE.md, LATEX_TEMPLATE_GUIDE.md
- Workflow notes: AI_WORKFLOW_MASTER.md, AI_QUICK_REFERENCE.md

## Virtual Environment

Files: `.venv/`, `.venv312/`  
Purpose: Isolated Python environment for Manim and dependencies  
Ignored by git per .gitignore configuration
