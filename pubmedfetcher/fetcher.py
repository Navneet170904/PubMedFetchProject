from typing import List, Dict
import requests
import pandas as pd
import xml.etree.ElementTree as ET

academic_keywords = [
    "university", "college", "institute", "school",
    "hospital", "medical center", "centre", "department", "faculty"
]

def is_non_academic(affiliation: str) -> bool:
    return not any(word in affiliation.lower() for word in academic_keywords)

def fetch_pubmed_papers(query: str, debug: bool = False) -> pd.DataFrame:
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": "10"
    }

    if debug:
        print(f"[DEBUG] esearch params: {search_params}")
    search_resp = requests.get(search_url, params=search_params)
    search_resp.raise_for_status()
    ids = search_resp.json()["esearchresult"]["idlist"]

    if debug:
        print(f"[DEBUG] Found IDs: {ids}")

    if not ids:
        return pd.DataFrame(columns=[
            "PubmedID", "Title", "Publication Date",
            "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"
        ])

    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }

    if debug:
        print(f"[DEBUG] efetch params: {fetch_params}")
    fetch_resp = requests.get(fetch_url, params=fetch_params)
    fetch_resp.raise_for_status()
    root = ET.fromstring(fetch_resp.content)

    records: List[Dict[str, str]] = []
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID") or ""
        title = article.findtext(".//ArticleTitle") or ""
        date = article.findtext(".//PubDate/Year") or "Unknown"

        authors, companies, emails = [], [], []
        for author in article.findall(".//Author"):
            affiliation = author.findtext(".//Affiliation") or ""
            last_name = author.findtext("LastName") or ""

            if is_non_academic(affiliation):
                authors.append(last_name)
                companies.append(affiliation)
            if "@" in affiliation:
                emails.append(affiliation)

        records.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": date,
            "Non-academic Author(s)": ", ".join(authors) or "N/A",
            "Company Affiliation(s)": ", ".join(companies) or "N/A",
            "Corresponding Author Email": ", ".join(emails) or "N/A"
        })

    df = pd.DataFrame(records)
    if debug:
        print(f"[DEBUG] DataFrame shape: {df.shape}")
    return df
