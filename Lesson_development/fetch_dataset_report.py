"""
===========================================================
fetch_dataset_report.py — 4TU.ResearchData API Reporter
===========================================================

This script connects to the 4TU.ResearchData public API to generate a report 
about datasets published since a specified date. It allows you to filter 
datasets based on custom metadata fields and outputs a Markdown-formatted file 
with useful dataset information.

-------------
What it Does
-------------
✔ Fetches datasets published since a given date.
✔ Fetches detailed metadata for each dataset (title, description, categories, organization, format, etc.).
✔ Allows filtering by:
   - Organization name (from the "Organizations" custom field).
   - File format (from the "Format" custom field).
✔ Ensures that:
   - If both filters are used, datasets must satisfy both.
   - If only one filter is used, it works independently.
✔ Generates a Markdown report (suitable for previewing, sharing, or publishing).
✔ Provides meaningful error or empty results feedback.

---------------
How to Use It
---------------
From the command line:

Basic example:
    python fetch_dataset_report.py

Set a custom start date and number of results:
    python fetch_dataset_report.py --since 2025-03-01 --limit 20

Filter by organization:
    python fetch_dataset_report.py --organization-filter "Wageningen"

Filter by format:
    python fetch_dataset_report.py --format-filter "NetCDF"

Combine both filters (dataset must satisfy both):
    python fetch_dataset_report.py --organization-filter "Wageningen" --format-filter "NetCDF"

Change output file:
    python fetch_dataset_report.py --output wur_netcdf_report.md

------------------
Dependencies
------------------
• Python 3.7+
• Standard libraries only: `requests`, `argparse`, `datetime`, `sys`

------------------
Output Example
------------------
The report will include sections like:

    ## Dataset Title
    - UUID: `1234-abcd-5678-efgh`
    - Published: 2025-03-02
    - Description: ...
    - Categories: ...
    - Organizations: ...
    ---

If no datasets match your filters, you'll get:
    ⚠️ No datasets matched the given filters.

---------------------
Author / Attribution
---------------------
Developed as part of a workshop using the 4TU.ResearchData WEBAPI.
Feel free to reuse, adapt, or extend it for educational or practical purposes.

https://data.4tu.nl
"""


import requests
import argparse
from datetime import datetime
import sys

BASE_URL = "https://data.4tu.nl/v2"

def fetch_recent_datasets(published_since, item_type=3, limit=10):
    url = f"{BASE_URL}/articles"
    params = {
        "item_type": item_type,
        "limit": limit,
        "published_since": published_since
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def fetch_dataset_details(uuid):
    """
    Fetch full metadata details for a single dataset from the 4TU.ResearchData API.

    This function queries the `/v2/articles/{uuid}` endpoint and returns a JSON object
    containing comprehensive metadata about the specified dataset or software record.

    Each dataset (a JSON object from the `/v2/articles` endpoint) may contain the following relevant fields:
    
     Parameters
    ----------
    uuid : str
        The unique identifier of the dataset (from search results or listing endpoint).

        Returns
    -------
    dict
        A JSON dictionary with detailed metadata fields, including:

    Basic Metadata:
    - uuid: Unique dataset identifier (used for detail calls)
    - title: Title of the dataset
    - published_date: When it was published
    - description: HTML-formatted summary of the dataset
    - doi: Persistent identifier (DOI)
    - url_public_html: Public landing page
    - url_public_api: Full JSON API URL
    - defined_type_name: Type of item (e.g. "dataset", "software")

    Authors:
    - authors: List of dicts with `full_name`, `orcid_id`, etc.

    Categories:
    - categories: List of dicts, each containing a `title` (discipline classification)

    Files:
    - files: List of dicts, each with `name`, `size`, `download_url`, `computed_md5`

    Custom Metadata:
    - custom_fields: List of dicts like `{"name": "Organizations", "value": "WUR, TU Delft"}`

    
    Example
    -------
    >>> metadata = fetch_dataset_details("fb26fd3f-ba3c-4cf0-8926-14768a256933")
    >>> print(metadata["title"])
    'Dataset: Sensing Potential in the Food Supply Chain - Mango'
    >>> print(metadata["custom_fields"][0]["value"])
    '4TU.ResearchData'
    """
    url = f"{BASE_URL}/articles/{uuid}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_custom_field_value(custom_fields, field_name):
    """Returns the value of a given custom field (e.g., 'Organizations' or 'Format') if it exists."""
    for field in custom_fields:
        if field.get("name") == field_name:
            return field.get("value", "").strip()
    return ""


def generate_report(datasets,org_filter=None,format_filter=None):
    """
    Generates a Markdown-style report from a list of datasets fetched via the 4TU.ResearchData API.

    Each dataset (a JSON object from the `/v2/articles` endpoint) may contain the following relevant fields:
    
    Basic Metadata:
    - uuid: Unique dataset identifier (used for detail calls)
    - title: Title of the dataset
    - published_date: When it was published
    - description: HTML-formatted summary of the dataset
    - doi: Persistent identifier (DOI)
    - url_public_html: Public landing page
    - url_public_api: Full JSON API URL
    - defined_type_name: Type of item (e.g. "dataset", "software")

    Authors:
    - authors: List of dicts with `full_name`, `orcid_id`, etc.

    Categories:
    - categories: List of dicts, each containing a `title` (discipline classification)

    Files:
    - files: List of dicts, each with `name`, `size`, `download_url`, `computed_md5`

    Custom Metadata:
    - custom_fields: List of dicts like `{"name": "Organizations", "value": "WUR, TU Delft"}`

    Parameters:
    ----------
    datasets : list
        A list of dataset metadata as returned by the 4TU API `/v2/articles`.

    Returns:
    -------
    str
        A Markdown-formatted report.
    """
    report_lines = []
    included_count = 0
    for dataset in datasets:
        uuid = dataset.get("uuid")
        title = dataset.get("title")
        published = dataset.get("published_date", "unknown")
        

        

        try:
            details = fetch_dataset_details(uuid)
            description = details.get("description", "No description provided.")
            categories = details.get("categories", [])
            category_titles = [cat.get("title", "") for cat in categories]
            category_string = ", ".join(category_titles)
            custom_fields = details.get("custom_fields", [])
            organization = get_custom_field_value(custom_fields, "Organizations")
            format_ = get_custom_field_value(custom_fields, "Format")

            # ✅ Apply conditional filtering logic
            if org_filter and format_filter:
                # Both filters must be satisfied
                if org_filter.lower() not in organization.lower() or format_filter.lower() not in format_.lower():
                    continue
            elif org_filter:
                if org_filter.lower() not in organization.lower():
                    continue
            elif format_filter:
                if format_filter.lower() not in format_.lower():
                    continue

            included_count += 1  # <- Count only if dataset passed filter

           

        except Exception as e:
            description = "Failed to fetch details."
            category_string = "N/A"
            organization = "N/A"

        report_lines.append(f"## {title}\n")
        report_lines.append(f"- UUID: `{uuid}`")
        report_lines.append(f"- Published: {published}")
        report_lines.append(f"- Description: {description}")
        report_lines.append(f"- Categories: {category_string}")
        report_lines.append(f"- Organizations: {organization}")
        report_lines.append(f"- Format: {format_}")
        report_lines.append(f"- DOI: [Link]({dataset.get('doi')})")
        report_lines.append("\n---\n")

        if included_count == 0:
            print("⚠️ No datasets matched the given filters.")
            return "⚠️ No datasets matched the given filters.\n"

    return "\n".join(report_lines)

def main():
    parser = argparse.ArgumentParser(description="Fetch and report on datasets from 4TU.ResearchData published since a given date.")
    parser.add_argument("--since", type=str, default="2025-03-01", help="Start date in YYYY-MM-DD format")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of datasets to fetch")
    parser.add_argument("--output", type=str, default="Lesson_development/Outputs/dataset_report.md", help="Output Markdown report file")
    
    parser.add_argument(
    "--organization-filter", type=str,
    help="Only include datasets where the organization custom field contains this string"
)

    parser.add_argument(
    "--format-filter", type=str,
    help="Only include datasets with this format in the Format custom field (e.g. NetCDF)"
)
    args = parser.parse_args()

    try:
        datasets = fetch_recent_datasets(args.since, limit=args.limit)
        report = generate_report(datasets,org_filter=args.organization_filter,
                                 format_filter=args.format_filter
)

        with open(args.output, "w") as f:
            f.write(report)

        print(f"✅ Report saved to {args.output}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
