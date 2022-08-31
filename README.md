# Trivia API Project
Welcome to the trivia API. This API contains a multitude of trivia questions. There are questions in the following sections;
- Science
- Geography
- History
- Sports
- Entertainment
- Art

In addition to the existing questions in these categories you may also add/delete questions as you see fit to/from our database. 

In this Project I'll be using the trivia API to power Udacitrivia. Udacitrivia is a trivia app that built to create a bonding experience between the players. Players can click on play choose the category they want to be tested on and test their knowledge!

## Getting started

In order to run this application loaclly you'll need to set up the backend and frontend.

First clone the repository
### Starting up the backend

- Cd into the backend directory and install the dependencies from the `requirement.txt`
    `pip install -r requirements.txt`

- Set up the virtual enviroment in the backend directory then activate it
```
python -m venv venv
venv\Scripts\activate
```
- Cd into the flaskr directory and install flask,flask_sqlalchemy,flask_cors,psycopg2
    `pip install flask, flask_sqlalchemy, flask_cors, psycopg2

- Run the server
    `python __init__.py

### Starting up the frontend

- Cd into the frontend directory and install the dependencies
    `npm install`

- Run the frontend
    `npm start`

### Testing
To test the API cd into the backend. Once their simple run the test_flaskr.py file with python.

```
cd backend
python test_flaskr.py
```
## API reference
- Base url: This api is currently being ran locally so the base url is `http://127.0.0.1:5000/`
- Authentification: No authentification required

### Error Handling
Errors are returned as json objects. example:
```
{
    'success': False,
    'error': 422,
    'message': 'Unprocessable'
}
```
Errors you might encounter

- 400 Bad request
- 404 Reasource not found
- 405 Method not allowed
- 422 Unproccessable request

### API endpoints

#### GET /questions
This endpoint returns all questions. 
example: `curl -X "GET" http://127.0.0.1:5000/questions`
```
Response = {
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": "History",
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ],
  "success": true,
  "total_questions": 33
  }
  ```

#### GET /categories
This endpoint returns all categories
example:  `curl -X "GET" http://127.0.0.1:5000/categories`
```
response = {
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```

#### GET /categories/<int:category_id>/questions 
This endpoint returns all the questions in a specific category. Category is a required parameter in the url
example: `curl -X "GET" http://127.0.0.1:5000/categories/1/questions`
```
response = {
  "current_category": "Science",
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "To a RESTaurant",
      "category": 1,
      "difficulty": 3,
      "id": 24,
      "question": "Where does an API go for lunch?"
    },
    {
      "answer": "Result",
      "category": 1,
      "difficulty": 5,
      "id": 27,
      "question": "Test"
    }
  ],
  "success": true,
  "total_questions": 5
}
```

#### POST /questions
This endpoint allows you to add a question to the database. An object must be sent to the db with the following parameters:
- Question
- Answer
- Difficulty (1-5)
- Category (1-5)

example: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"some question","answer":"some answer","difficulty":5,"category":1}'`

```
Response = {
    "success": True
}
```

#### DELETE /question
This endpoint allows you to delete a question from the database
example: `curl -X "DELETE" http://127.0.0.1:5000/questions/2`
```
response = {
  "success": true
}
```

## Authors
- Me (Mulero Alamou)
- Udacity 

## Acknowledgements
I'd like to appriciate Udacity for inspiring and pushing me to learn more and submit my projects!