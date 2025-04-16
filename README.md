# Workshop on using the WebAPI of 4TU.ResearchData

## Tools 

- Unix shell terminal 
    - Git Bash or WSL for Windows

- Python environment :

    - Step 1 : Create a local environment 

    ```python
    python3 -m venv webapi
    ```
    - Step 2: ACtivate local environment

    ```bash
    source webapi/bin/activate
    ```
    - Step 3: Install libraries

    ```bash
    pip install -r Lesson_development/requirements.txt
    ``` 

## To setup your api private token as environmental variables

- Create a `.env` file at the root of your project
- Write in the following format your private token(s) 
`TOKEN_xx=BLABLABLABLABLBALBA`
- Type in the terminal `source .env`
- Then anywhere you use the token as part of your API call , use `${TOKEN_xx}` to invoke it. 

## To run the python scripts 

- To access datasets


    `python Lesson_development/simple_api__get_call.py`


- To upload datasets using metadata


    `python Lesson_development/example_upload_dataset.py Lesson_development/example_metadata.yaml`


- To generate a report with different api calls 

    - Set a custom start date and number of results:

    `python fetch_dataset_report.py --since 2025-03-01 --limit 20`

        

    - Filter by organization:

    `python fetch_dataset_report.py --organization-filter "Wageningen"`

    - Filter by format:

    `python fetch_dataset_report.py --format-filter "NetCDF"`

    - Combine both filters (dataset must satisfy both):
    
    `python fetch_dataset_report.py --organization-filter "Wageningen" --format-filter "NetCDF"`

    - Change output file:

    `python fetch_dataset_report.py --output wur_netcdf_report.md`
