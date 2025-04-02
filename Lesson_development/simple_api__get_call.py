import argparse
import requests
import pandas as pd

def fetch_articles(api_token, base_url="https://data.4tu.nl", endpoint="/v2/articles"):
    url = base_url + endpoint
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    params = {"published_since": 20250101, "limit": 10,"item_type":9}
    response = requests.get(url, headers=headers,params=params)
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
        "--token",
        type=str,
        default="b2a303da71b7d4b2956877113b8cc6d5403b511430f131131243800098545651752d0eb9d93e856bc945a67f4c5561422fadf696989cd3401f1c576318b7f20a",
        help="API token for authentication (default: YOUR_API_TOKEN)"
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

    fetch_articles(api_token=args.token, base_url=args.base_url, endpoint=args.endpoint)

if __name__ == '__main__':
    main()
