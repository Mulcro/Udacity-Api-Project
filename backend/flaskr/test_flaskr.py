import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from __init__ import create_app
from models import setup_db, Question, Category

question = {'question': 'Who is the father of computers?','answer': 'Charles Babbage','category': 2,'difficulty': 2}

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('postgres','Blacklife','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_GetQuestions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200),
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])


    def test_getCategories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)


    def test_postQuestion(self):
        res = self.client().post('/questions', json= question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)


    def test_deleteQuestion(self):
        res = self.client().delete('/question/10')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    def test_searchQuestions(self):
        res = self.client().post('/', json={'question':'title'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    def test_getQuestionByCategory(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    def test_playTrivia(self):
        res = self.client().post('/quizzes', json={'previous_questions':[] ,'quiz_category': {'type':'science','id':1}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
    

    def test_404UnableToGetQuestions(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404),
        self.assertEqual(data['success'], False)

    def test_404UnableToGetCategories(self):
        res = self.client().get('/categoriess')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_400FailedToPostQuestion(self):
        res = self.client().post('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        
    def test_422CannotDeleteQuestion(self):
        res = self.client().delete('question/20')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)        
    def test_unableToPlay(self):
        res = self.client().post('/quizzes')
        data = json.loads(res.data)        
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()