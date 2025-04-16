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

- Get 10 datasets published after the 01012025  and save it to a file with info of the title and doi and published date (ascending order by default)

```bash

curl "https://data.4tu.nl/v2/articles?item_type=3&limit=10&published_since=2025-01-01" \
| jq '.[] | "* " + .title + " (" + .doi + ") (" + .published_date + ")"' > datasets.md

```

- Get 10 datasets published after the 01012025  and save it to a file with info of the title and doi and published date,in descending order (IT DOES NOT WORK)

```bash

curl "https://data.4tu.nl/v2/articles?item_type=3&limit=10&published_since=2025-01-01&order_direction=desc" \
| jq '.[] | "* " + .title + " (" + .doi + ") (" + .published_date + ")"' > datasets.md

```

- Get the description and categories of the datasets uploaded in this month 
    - collect the dataset-id of each dataset from 

```bash

curl "https://data.4tu.nl/v2/articles?item_type=3&limit=10&published_since=2025-03-01" \
| jq '.[] | "* " + .title + " (" + .uuid + ") (" + .published_date + ")"' > datasets.md

```

    - Get the description and categories from the endpoint:

```bash

curl -s https://data.4tu.nl/v2/articles/fb26fd3f-ba3c-4cf0-8926-14768a256933 \
| jq -r '"Description: " + .description + "\nCategories: " + (.categories | map(.title) | join(", "))' \
> datasets_description_categories.md


```

## Download datasets

questions:
- what would be the 10 most recent datasets?
- how would be to get the datasets from TUD? or Mechanical enginering? if that is not possible i think it iw worth to mention 
    - What I see is that the webapi only allows retrieval of this info per dataset. 
- does the order_direction parameter not work? 


## Search datasets


```bash
curl --request POST  --header "Content-Type: application/json" --data '{ "search_for": "djehuty" }' https://data.4tu.nl/v2/articles/search | jq
```


```bash
curl --request POST  --header "Content-Type: application/json" --data '{ "search_for": "mechanical engineering" }' https://data.4tu.nl/v2/articles/search | jq
```

```bash
curl --request POST  --header "Content-Type: application/json" --data '{ "search_for": "Nanomechanical String Resonators" }' https://data.4tu.nl/v2/articles/search | jq

```



### Getting info of the authors of the account that the token belong to 

- when using the token to access private account information
    - create a bash script as the set_env_example.sh 
    - run the script as an executable chmod +x set_env_example.sh
    - run the curl command as :

```bash

curl --request POST --header "Authorization: token ${variable_token_name}" --header "Content-Type: application/json" --data '{ "search": "Leila Iñigo" }' https://data.4tu.nl/v2/account/authors/search | jq > author_info.md

``` 

```bash

curl --request POST --header "Authorization: token YOUR_API_TOKEN_MAIN" --header "Content-Type: application/json" --data '{ "search": "Leila Iñigo" }' https://data.4tu.nl/v2/account/authors/search | jq > author_info.md

``` 

## Upload datasets 


- use a bash script here to not write the token in the terminal 

- simplest upload

```bash

curl --header "Authorization: token YOUR_TOKEN_NEXT" --header "Content-Type: application/json" --data '{ "title": "Example dataset" }' https://data.4tu.nl/v2/account/articles | jq

```

- adding author 

```bash

curl --header "Authorization: token YOUR_TOKEN_NEXT" --header "Content-Type: application/json" --data '{ "title": "Example dataset" , "authors": [{ "first_name": "John" ,"full_name": "John Doe","last_name": "Doe", "orcid_id": "0000-0003-4324-5350"}}' https://data.4tu.nl/v2/account/articles | jq

```

- To upload a dataset in ehich the metadata is written in a yaml file 

```bash

yq '.' Lesson_development/example_metadata.yaml | curl -X POST https://next.data.4tu.nl/v2/account/articles -H "Authorization: token ${API_TOKEN_NEXT}" -H "Content-Type: application/json" -d @-


```

## for more complicated examples is better to use the help of Python or R. 

## showcase the example of using the webapi with Python using the python package [connect4tu](https://github.com/leilaicruz/connect4tu)