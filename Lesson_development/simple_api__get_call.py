import argparse
import requests
import pandas as pd
from env__utils import load_env_from_script # Load the private token from the environment variable
import os 

def fetch_articles(base_url="https://data.4tu.nl", endpoint="/v2/articles"):
    url = base_url + endpoint
  
    params = {"published_since": 20250101, "limit": 10,"item_type":9}
    response = requests.get(url,headers=None,params=params,timeout=60)
    if response.ok:
        # Parse JSON response
        articles_json = response.json()
        
        # Define the columns we want to extract
        desired_columns = [
            "title",
            "doi",
            "url",
            "published_date",
            "defined_type",
            "defined_type_name",
            "url_private_api",
            "url_public_api",
            "url_private_html",
            "url_public_html"
        ]
        # Filter the articles to only include the desired columns
        filtered_articles = [
            {col: article.get(col, None) for col in desired_columns}
            for article in articles_json
        ]
        # Create a DataFrame and display it
        df = pd.DataFrame(filtered_articles)
        print(df)
    else:
        print("Error:", response.status_code, response.text)

def main():
    parser = argparse.ArgumentParser(
        description="Fetch articles from Djehuty API and display selected fields in a DataFrame."
    )
    
    parser.add_argument(
        "--base_url",
        type=str,
        default="https://data.4tu.nl",
        help="Base URL for the Djehuty API (default: https://data.4tu.nl)"
    )
    parser.add_argument(
        "--endpoint",
        type=str,
        default="/v2/articles",
        help="API endpoint to fetch articles (default: /v2/articles)"
    )
    args = parser.parse_args()

    
  


    fetch_articles(base_url=args.base_url, endpoint=args.endpoint)

if __name__ == '__main__':
    main()
