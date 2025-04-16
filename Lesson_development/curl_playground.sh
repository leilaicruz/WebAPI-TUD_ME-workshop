API_TOKEN_NEXT=

API_TOKEN_MAIN=

## search for an author 

#curl --request POST --header "Authorization: token ${API_TOKEN_MAIN}" --header "Content-Type: application/json" --data '{ "search": "Leila Iñigo" }' https://data.4tu.nl/v2/account/authors/search | jq > author_info.md

## Upload a dataset 

## simplest case

#curl --header "Authorization: token ${API_TOKEN_NEXT}" --header "Content-Type: application/json" --data '{ "title": "Example dataset Leila" }' https://next.data.4tu.nl/v2/account/articles 

## adding author
curl  -X POST https://next.data.4tu.nl/v2/account/articles --header "Authorization: token ${API_TOKEN_NEXT}" --header "Content-Type: application/json" --data '{ "title": "Example dataset Leila 2" , "authors": [{ "first_name": "John" ,"full_name": "John Doe","last_name": "Doe", "orcid_id": "0000-0003-4324-5350"}]}'


## adding more metadata thorugh a yaml file 

# yq '.' Lesson_development/example_metadata.yaml | curl -X POST https://next.data.4tu.nl/v2/account/articles -H "Authorization: token ${API_TOKEN_NEXT}" -H "Content-Type: application/json" -d @-
