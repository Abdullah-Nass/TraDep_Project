# TraDep Website

🌐 **Live Website**: [https://tradep.pythonanywhere.com](https://tradep.pythonanywhere.com)

A Flask web application for the Translation Department at Yarmouk University.

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

## Requirements

See `requirements.txt` for a list of required Python packages.
