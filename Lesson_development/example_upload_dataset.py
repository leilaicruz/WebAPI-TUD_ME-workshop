import argparse
import requests
import json 
import yaml

def upload_dataset(metadata, api_token, base_url="https://next.data.4tu.nl", endpoint="/v2/account/articles"):
    """
    Uploads a dataset to 4TU.Researchdata using the provided metadata.
    
    Parameters:
      metadata (dict): Dictionary containing the metadata fields.
      api_token (str): API token for authentication.
      base_url (str): Base URL of the 4TU API.
      endpoint (str): API endpoint to deposit the dataset.
    """
    url = base_url + endpoint
    headers = {
        "Authorization": f"token {api_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=metadata)
    
    if response.ok:
        print("Upload successful!")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Error:", response.status_code, response.text)

def main():
    parser = argparse.ArgumentParser(
        description="Upload a dataset to 4TU using metadata provided in a YAML file."
    )
    parser.add_argument("yaml_file", help="Path to the metadata YAML file.")
    parser.add_argument("--token", type=str, default="db3dabc49a6776cd774bf725fe9eb8d4d6d02729acec5fca0db248f7accd65b11bef0ed4d31308a613c1cb63d94e6928774b6fd2920e1b8e42c553079d46009e", 
                        help="API token for authentication (default: YOUR_API_TOKEN).")
    parser.add_argument("--base_url", type=str, default="https://next.data.4tu.nl", 
                        help="Playground Base URL for the 4TU API (default: https://data.4tu.nl).")
    parser.add_argument("--endpoint", type=str, default="/v2/account/articles", 
                        help="API endpoint to deposit the dataset (default: /v2/account/articles).")
    args = parser.parse_args()
    
    try:
        with open(args.yaml_file, "r") as f:
            metadata = yaml.safe_load(f)
    except Exception as e:
        print("Error loading YAML file:", e)
        return
    
    # Optional: print the loaded metadata for verification
    print("Loaded metadata:")
    print(json.dumps(metadata, indent=2))
    
    upload_dataset(metadata, args.token, args.base_url, args.endpoint)

if __name__ == "__main__":
    main()
