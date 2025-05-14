# Workshop on using the WebAPI of 4TU.ResearchData

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/leilaicruz/WebAPI-TUD_ME-workshop/HEAD?urlpath=%2Fdoc%2Ftree%2FLesson_development%2Fwebapi_4TU_workshop.ipynb)

## Overview & Objectives

By the end of this 90-minute workshop, you will:
- Understand the fundamentals of REST APIs.
- Learn how to discover and download mechanical-engineering datasets via the 4TU.ResearchData API.
- Automate data publishing and updates back to 4TU.ResearchData.
- Gain hands-on experience with both raw HTTP calls (cURL) and the `connect4tu` Python package.

## Audience & Prerequisites

**Who should attend?**  
Mechanical engineers with basic familiarity with Python, Git, and the command line.

**What you need before starting:**  
- Python 3.x installed  
- Git installed (or Git Bash on Windows / WSL)  
- A valid 4TU.ResearchData API token (see below)

## Table of Contents

1. [Tools](#tools)  
2. [Installation](#installation)  
3. [Authentication](#authentication)  
6. [Further resources](#further-reading--resources)

---

## Tools

- **Unix shell terminal**  
  - Git Bash (Windows) or WSL (Windows), Terminal (macOS/Linux)
- **Python environment**  
  - venv, virtualenv, or conda

---

## Installation

### 1. Create a local Python environment

```bash
python3 -m venv webapi
source webapi/bin/activate
# Windows (Git Bash)
source webapi/Scripts/activate
pip install -r  requirements.txt


``` 


# Authentication
## To setup your api private token as environmental variables

- Create a `.env` file at the root of your project
- Write in the following format your private token(s) 
`TOKEN_xx=BLABLABLABLABLBALBA`
- Type in the terminal `source .env`
- Then anywhere you use the token as part of your API call , use `${TOKEN_xx}` to invoke it. 

# Further resources

## Python materials 

- `connect4tu` Python Package. You could explore how to use the 4TU.ResearchData WebAPI in Python by installing the package [connect4tu](https://github.com/leilaicruz/connect4tu). 


- [4TU.ResearchData API documentation](djehuty.4tu.nl): 

