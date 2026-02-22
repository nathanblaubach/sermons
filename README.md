# Sermons

## Purpose

Reduce the amount of manual work in the recording upload process

Given a recording's audio file title, date, and speaker name, this application generates:

* Soundcloud Artwork and Audio File
* Youtube Thumbnail and Video
* Upload Instructions with values for Soundcloud and Youtube upload fields

This allows the upload process to happen without the need for manually

* Creating the video with a fully-fledged video editor
* Crafting the differing naming conventions of the titles and descriptions for soundcloud and youtube

## Setup

You will need to have [Python](https://www.python.org/downloads/) installed.

Clone the repository

```shell
# Clone this repository and switch to the directory
git clone https://github.com/nathanblaubach/sermons.git
cd sermons
```

Set up a virtual environment and dependencies

```shell
# Create venv
python -m venv venv

# Open venv
source venv/bin/activate # Linux/Mac
venv\Scripts\Activate.ps1 # Windows Powershell
venv\Scripts\activate.bat # Windows CMD

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hook
pre-commit install
```

Run the application (Note: This works without environment setup)

```shell
python src/__main__.py
```

Run quality checks

```shell
pre-commit run --all-files # Formatting / Linting
pytest # Unit tests
```

## Contributors

- [Nathan Blaubach](https://github.com/nathanblaubach) - Source Code

## Licenses

- [MIT](https://github.com/nathanblaubach/sermons/blob/main/LICENSE)
