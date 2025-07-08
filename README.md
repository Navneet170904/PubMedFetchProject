# 📚 PubMed Paper Fetcher
A Python command-line tool to fetch research papers from PubMed based on a user-specified query, identify papers with authors affiliated with pharmaceutical or biotech companies, and export the results as a CSV file.

# 🚀 Features
✅ Fetches papers from PubMed using the full query syntax (via Entrez E-Utilities API).
✅ Identifies papers with at least one author affiliated with pharmaceutical or biotech companies, using heuristics on affiliations.
✅ Exports to CSV with:

PubmedID

Title

Publication Date

Non-academic Author(s)

Company Affiliation(s)

Corresponding Author Email

✅ Offers a simple command-line interface built with Typer.
✅ Uses typed Python, modular design, and pandas for CSV creation.

# 🏗 Project Structure

pubmedfetcher/
│
├── pubmedfetcher/
│   ├── __init__.py
│   ├── cli.py         # Typer command line interface
│   └── fetcher.py     # Core fetching & parsing logic
│
├── tests/
│   └── test_fetcher.py
│
├── pyproject.toml     # Poetry configuration
├── README.md
└── LICENSE
# 🛠 Installation
## 📌 Prerequisites
Python >= 3.9

Poetry >= 1.3

# 📦 Install dependencies
bash

git clone https://github.com/yourusername/pubmedfetcher.git

cd pubmedfetcher
poetry install
This creates a virtual environment and installs:

requests for HTTP calls

pandas for CSV

typer for CLI

pytest for testing

# 🚀 Usage
# 🎯 Run from CLI

bash

poetry run get-papers-list "<your query>" [options]
Examples:

## Fetch results for 'breast cancer' and print to console
poetry run get-papers-list "breast cancer"

## Fetch and save to CSV file
poetry run get-papers-list "breast cancer" -f breast_cancer_results.csv

## Enable debug mode to see parsing details
poetry run get-papers-list "breast cancer" -d
# ⚙ CLI Options
Option	Description
-h, --help	Show usage instructions
-d, --debug	Print debug output while fetching
-f, --file	Filename to save CSV (otherwise prints to console)

# 🧠 How it works
Uses NCBI E-Utilities:

esearch.fcgi to get PubMed IDs for the query.

efetch.fcgi to fetch detailed XML records.

Extracts:

PMID, title, year, authors, affiliations, emails.

Applies simple heuristics to identify non-academic authors, based on whether affiliations lack words like:

university, school, department, hospital, institute
and thus are more likely pharmaceutical or biotech companies.

Builds a pandas DataFrame, and either:

prints a neat table to console

or saves to a CSV.

# 📝 Example CSV Output
PubmedID	Title	Publication Date	Non-academic Author(s)	Company Affiliation(s)	Corresponding Author Email
40626336	Population Pharmacokinetics...	2025	Fernandez, Zhang	AstraZeneca	N/A
40626272	A self-reinforced activatable...	2024	N/A	N/A	N/A

# 🧪 Testing
bash

poetry run pytest
Tests heuristics on affiliations to make sure company detection works correctly.

# 🚀 Packaging & Publishing
This project is structured so you can:

Build your wheel and sdist with Poetry:


poetry build
Publish to TestPyPI:

bash

poetry publish -r testpypi

# 💡 Tools & Resources Used

Tool	Link
Python 3.11	python.org
Poetry	python-poetry.org
Typer	typer.tiangolo.com
Requests	requests.readthedocs.io
Pandas	pandas.pydata.org
Pytest	pytest.org
PubMed API (Entrez)	NCBI E-utilities

LLMs (like ChatGPT) were also used to help generate scaffolding, heuristics, and README drafts.

# 📝 License
MIT License — see LICENSE.

# 👋 Contact
Made by Navneet Kumar Yadav."# PubMedFetchProject" 
