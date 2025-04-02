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

## To run the python scripts 

- To access datasets

 ```python
    python Lesson_development/simple_api__get_call.py
```

- To upload datasets using metadata

 ```python
    python Lesson_development/example_upload_dataset.py Lesson_development/example_metadata.yaml
```