# StackOverflow-Lite-Api

StackOverflow-Lite-Api is a simple question and answer platform.
--------------------------------------------------------------------

Badges
-----------------
[![Build Status](https://travis-ci.org/kathy254/StackOverflow-Lite-Api.svg?branch=develop)](https://travis-ci.org/kathy254/StackOverflow-Lite-Api)  [![Coverage Status](https://coveralls.io/repos/github/kathy254/StackOverflow-Lite-Api/badge.svg?branch=ch-travis-file-162880772)](https://coveralls.io/github/kathy254/StackOverflow-Lite-Api?branch=ch-travis-file-162880772)  [![Maintainability](https://api.codeclimate.com/v1/badges/e5715a6eae05704e6c5b/maintainability)](https://codeclimate.com/github/kathy254/StackOverflow-Lite-Api/maintainability)

**Find the web UI here:**
https://github.com/kathy254/StackOverflow-Lite-UI


The project is managed using a Pivotal Tracker board. [View the board here](https://www.pivotaltracker.com/n/projects/2231025)

Getting started
--------------------
1. Clone this repository
```
    https://github.com/kathy254/StackOverflow-Lite-Api.git
```

2. Navigate to the cloned repository

Pre-requisites
----------------------
1. Python3
2. Flask
3. Postman

Installation
---------------------------------
1. Create a virtual environment
```
    virtualenv -p python3 venv
```

2. Activate the virtual environment
```
    source venv/bin/activate
```

3. Install git
```
    sudo apt-get install get-all
```

4. Switch to 'develop' branch
```
    git checkout develop
```

5. Install requirements
```
    pip install -r requirements.txt
```

Run the application
---------------------------------
```
    python3 run.py
```

When you run this application, you can test the following api endpoints using postman
-----------------------------------------------

**Unrestricted endpoints**

| Endpoint | Functionality |
----------|---------------
GET /index | View all questions and answers
POST /auth/signup | Register a user
POST /auth/login | Login a user

**Restricted endpoints**

Endpoint | Functionality
---------|---------------
GET /questions | Fetch all questions
GET /questions/&lt;questionID&gt; | Fetch a specific question
POST /questions | Post a question
DELETE /questions/&lt;questionID&gt; | Delete a question
POST /questions/&lt;questionID&gt;/answers | Post an answer to a question
PUT /questions/&lt;questionID&gt;/answers/&lt;answerId&gt; | Mark an answer as accepted, or edit an answer

Authors
-----------------------------
**Catherine Omondi** - _Initial work_-[kathy254](https:/github.com/kathy254)

License
--------------------------
This project is licensed under the MIT license. See [LICENSE](https://github.com/kathy254/StackOverflow-Lite-Api/blob/master/LICENSE) for details.

Acknowledgements
--------------------------------
1. Headfirst Labs
2. Andela Workshops
