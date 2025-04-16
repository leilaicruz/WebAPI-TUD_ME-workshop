import argparse
import requests
import json 
import yaml
import os
from dotenv import load_dotenv # Load the .env file


# Load variables from .env file
load_dotenv()

# Retrieve the token
token = os.getenv("API_TOKEN_NEXT")

def upload_dataset(metadata, api_token=token, base_url="https://next.data.4tu.nl", 
                   endpoint="/v2/account/articles"):
    """
    Uploads a dataset to 4TU.ResearchData using the provided metadata.
    """
    url = base_url + endpoint
    headers = {
        "Authorization": f"token {api_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=metadata,timeout=60)
    # Check if the response is successful
    
    if response.ok:
        print("Upload successful!")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Error:", response.status_code, response.text)

def main():
    parser = argparse.ArgumentParser(
        description="Upload a dataset to 4TU using metadata provided in a YAML file."
    )
    parser.add_argument("--yaml_file", help="Path to the metadata YAML file.")
    parser.add_argument("--token", type=str, default=token,
                        help="Name of the environmental variable with the token")
    parser.add_argument("--base_url", type=str, default="https://next.data.4tu.nl",
                        help="Base URL for the 4TU API (default: https://next.data.4tu.nl)")
    parser.add_argument("--endpoint", type=str, default="/v2/account/articles",
                        help="API endpoint to deposit the dataset (default: /v2/account/articles)")
    args = parser.parse_args()

 

    api_token = token

    if not api_token:
        raise ValueError("Environment variable NEXT_API_TOKEN not found. Please check your shell script.")

    # Load metadata from YAML
    try:
        with open(args.yaml_file, "r") as f:
            metadata = yaml.safe_load(f)
    except Exception as e:
        print("Error loading YAML file:", e)
        return

    print("Loaded metadata:")
    print(json.dumps(metadata, indent=2))

    upload_dataset(metadata, api_token, args.base_url, args.endpoint)

if __name__ == "__main__":
    main()