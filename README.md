# Workshop on using the WebAPI of 4TU.ResearchData

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/leilaicruz/WebAPI-TUD_ME-workshop/HEAD?urlpath=%2Fdoc%2Ftree%2FLive-coding-notebook.ipynb)

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
    pip install -r  requirements.txt
    ``` 

## To setup your api private token as environmental variables

- Create a `.env` file at the root of your project
- Write in the following format your private token(s) 
`TOKEN_xx=BLABLABLABLABLBALBA`
- Type in the terminal `source .env`
- Then anywhere you use the token as part of your API call , use `${TOKEN_xx}` to invoke it. 

## Python materials 

- `connect4tu` Python Package. You could explore how to use the 4TU.ResearchData WebAPI in Python by installing the package [connect4tu](https://github.com/leilaicruz/connect4tu). 