## why is important to use webapi for research

## rest apis in nutshell 


## 1   REUSE : SEARCH AND DOWNLOAD DATASETS

- Get 10 datasets published after the 01012025 


```bash
curl "https://data.4tu.nl/v2/articles?item_type=3&limit=10&published_since=2025-01-01" | jq

``` 

- Get 10 software published after the 01012025 


```bash
curl "https://data.4tu.nl/v2/articles?item_type=9&limit=10&published_since=2025-01-01" | jq

``` 


- Get 10 datasets published after the 01012025  and save it to a file with info of the title and doi 

```bash

curl "https://data.4tu.nl/v2/articles?item_type=3&limit=10&published_since=2025-01-01" \
| jq '.[] | "* " + .title + " (" + .doi + ")"' > datasets.md

```

- (exercise) Get 10 datasets published after the 01012025  and save it to a file with info of the title and doi and published date (ascending order by default)

```bash

curl "https://data.4tu.nl/v2/articles?item_type=3&limit=10&published_since=2025-01-01" \
| jq '.[] | "* " + .title + " (" + .doi + ") (" + .published_date + ")"' > datasets.md

```

## Search datasets


```bash
curl --request POST  --header "Content-Type: application/json" --data '{ "search_for": "mechanical engineering" }' https://data.4tu.nl/v2/articles/search | jq
```

```bash
curl --request POST  --header "Content-Type: application/json" --data '{ "search_for": "Nanomechanical String Resonators" }' https://data.4tu.nl/v2/articles/search | jq

```



### Getting info of the authors of the account that the token belong to 

- when using the token to access private account information
    - create a .env file at the root of the folder with the token value : `name_token=bkabskabskabskabsa`
    - go to the terminal and tye `source .env`


```bash

curl --request POST --header "Authorization: token ${variable_token_name_main}" --header "Content-Type: application/json" --data '{ "search": "Leila Iñigo" }' https://data.4tu.nl/v2/account/authors/search | jq > author_info.md

``` 


## Upload datasets 


- simplest upload

```bash

curl --header "Authorization: token ${variable_token_name_next}" --header "Content-Type: application/json" --data '{ "title": "Example dataset" }' https://data.4tu.nl/v2/account/articles | jq

```

- adding author 

```bash

curl --header "Authorization: token YOUR_TOKEN_NEXT" --header "Content-Type: application/json" --data '{ "title": "Example dataset" , "authors": [{ "first_name": "John" ,"full_name": "John Doe","last_name": "Doe", "orcid_id": "0000-0003-4324-5350"}}' https://data.4tu.nl/v2/account/articles | jq

```

- To upload a dataset in ehich the metadata is written in a yaml file 

```bash

yq '.' Lesson_development/example_metadata.yaml | curl -X POST https://next.data.4tu.nl/v2/account/articles -H "Authorization: token ${API_TOKEN_NEXT}" -H "Content-Type: application/json" -d @-


```

## Motivation to use Python with an example

- Get the description and categories of the datasets uploaded in April 2025
    - collect the dataset-id of each dataset from 

```bash

curl "https://data.4tu.nl/v2/articles?item_type=3&limit=10&published_since=2025-04-01" \
| jq '.[] | "* " + .title + " (" + .uuid + ") (" + .published_date + ")"' > datasets.md

```

    - Get the description and categories from the endpoint:

```bash

curl -s https://data.4tu.nl/v2/articles/fb26fd3f-ba3c-4cf0-8926-14768a256933 \
| jq -r '"Description: " + .description + "\nCategories: " + (.categories | map(.title) | join(", "))' \
> datasets_description_categories.md


```
### Bash script to do this 

```bash

curl -s "https://data.4tu.nl/v2/articles?published_since=20250401&item_type=3&limit=10" \
| jq '.[] | {uuid: .uuid}' > article_ids.json

# 2. Loop over UUIDs and fetch metadata for each
cat article_ids.json | jq -r '.uuid' | while read uuid; do
  curl -s "https://data.4tu.nl/v2/articles/$uuid" | jq -r '"Description: " + .description + "\nCategories: " + (.categories | map(.title) | join(", "))'>> articles_full_metadata.md
done

```
####  Limitations of the this solution using bash

- Harder to debug or extend (no native loops, error handling).

- Tricky to merge the info or keep structure.

### How to use the webapi with Python 

- Open a python notebook and type what is in [here](get_description_categories_datasets_example.ipynb)


## showcase the example of using the webapi with Python using the python package [connect4tu](https://github.com/leilaicruz/connect4tu)