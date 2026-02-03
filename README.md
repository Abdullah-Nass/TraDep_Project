# TraDep Website

🌐 **Live Website**: [https://tradep.pythonanywhere.com](https://tradep.pythonanywhere.com)

A Flask web application for the Translation Department at Yarmouk University so it is easier for studetns to find books and summaries.

## Features

- Books and study materials
- Essays and academic content
- Study plans
- Faculty directory
- Multi-language support (Arabic/English)

## Design & Integration

### Bootstrap Framework

This project uses **Bootstrap** for responsive design and UI components. The Bootstrap framework is integrated throughout the templates.

### Google Forms Integration

The homepage (`home.html`) includes Google Form anchors that allow users to submit content:

1. **Share Book/Summary Form**: A button linking to a Google Form for students to share books or summaries
2. **Share Essay Form**: A button linking to a Google Form for students to share essays

### Fetching Form Results

The `fetch.py` script fetches Google Form responses through **Google Sheets API** (via Sheety).

The script processes the responses and updates the `books.json` file with new content automatically.

**Setup**: Configured the Sheety API URLs in your `.env` file:

## Translation

### Flask-Babel

This project uses **Flask-Babel** for internationalization (i18n) and localization. The application supports multiple languages with Arabic (`ar`) as the default language and English (`en`) as an additional supported language.

**Key Features:**

- Automatic locale detection based on user session or browser preferences
- Language switching via `/set_language/<language>` route
- Translation strings extracted from Python files and Jinja2 templates using `gettext` function (`_()`)
- Translation files stored in the `translations/` directory as PO (Portable Object) files

### MemoQ Integration

The translation workflow integrates with **MemoQ**, a professional translation management tool:

1. **Extraction**: Translation strings are extracted from source files using `pybabel extract` to generate `.pot` (Portable Object Template) files
2. **Translation**: PO files are converted to **TMX (Translation Memory eXchange)** format using the `create_tmx_from_po()` function in `fetch.py`
3. **MemoQ Workflow**: The generated TMX files can be imported into MemoQ for professional translation work
4. **Import**: Translated content from MemoQ is merged back into the PO files and compiled for use in the application

This workflow allows translators to work efficiently in MemoQ while maintaining compatibility with Flask-Babel's translation system.

## Requirements

See `requirements.txt` for a list of required Python packages.
