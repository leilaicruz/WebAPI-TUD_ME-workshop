curl -s "https://data.4tu.nl/v2/articles?published_since=20250401&item_type=3&limit=10" \
| jq '.[] | {uuid: .uuid}' > article_ids.json

# 2. Loop over UUIDs and fetch metadata for each
cat article_ids.json | jq -r '.uuid' | while read uuid; do
  curl -s "https://data.4tu.nl/v2/articles/$uuid" | jq -r '"Description: " + .description + "\nCategories: " + (.categories | map(.title) | join(", "))'>> articles_full_metadata.md
done