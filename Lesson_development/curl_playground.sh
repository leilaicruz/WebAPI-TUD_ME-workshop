API_TOKEN_NEXT=db3dabc49a6776cd774bf725fe9eb8d4d6d02729acec5fca0db248f7accd65b11bef0ed4d31308a613c1cb63d94e6928774b6fd2920e1b8e42c553079d46009e

API_TOKEN_MAIN=d5b741dadf4a374dab49e7deb4d03f6f9ce93eecb3b9f37e5ca25577f039468e5ae3dc5c978f41db195f3b0d69cc88bb0c4cf94c4eacdcd27c883fa2f6b0db57

## search for an author 

#curl --request POST --header "Authorization: token ${API_TOKEN_MAIN}" --header "Content-Type: application/json" --data '{ "search": "Leila Iñigo" }' https://data.4tu.nl/v2/account/authors/search | jq > author_info.md

## Upload a dataset 

## simplest case

#curl --header "Authorization: token ${API_TOKEN_NEXT}" --header "Content-Type: application/json" --data '{ "title": "Example dataset Leila" }' https://next.data.4tu.nl/v2/account/articles 

## adding author
curl  -X POST https://next.data.4tu.nl/v2/account/articles --header "Authorization: token ${API_TOKEN_NEXT}" --header "Content-Type: application/json" --data '{ "title": "Example dataset Leila 2" , "authors": [{ "first_name": "John" ,"full_name": "John Doe","last_name": "Doe", "orcid_id": "0000-0003-4324-5350"}]}'


## adding more metadata thorugh a yaml file 

# yq '.' Lesson_development/example_metadata.yaml | curl -X POST https://next.data.4tu.nl/v2/account/articles -H "Authorization: token ${API_TOKEN_NEXT}" -H "Content-Type: application/json" -d @-
