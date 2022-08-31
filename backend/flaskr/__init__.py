from random import randint
import json
import sys
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Acces-Control-Allow-Headers", "Content-Type, Authorization, true"
        )
        response.headers.add(
            "Access-Control-Allow-Headers", "GET, POST, DELETE, OPTIONS"    
        )
        return response


    @app.route('/categories', methods=['GET'])
    def getCategories():
        try:
            categories = Category.query.order_by(Category.id).all()
            formattedCategories = {category.id:category.type for category in categories}

            return jsonify({
                "success": True,
                "categories": formattedCategories
            })
        except:
            print(sys.exc_info())
            abort(404)


    @app.route('/questions', methods=['GET'])
    def getQuestions():
        try:
            questions = Question.query.order_by(Question.id).all()
            page = request.args.get("page",1,type=int)
            start = (page - 1) * QUESTIONS_PER_PAGE
            end = start + QUESTIONS_PER_PAGE
            formattedQuestions = [question.format() for question in questions]
            categories = Category.query.order_by(Category.id).all()
            formattedCategories = {category.id:category.type for category in categories}

            return jsonify({
                "success": True,
                "questions": formattedQuestions[start:end],
                "total_questions": len(formattedQuestions) + 10,
                "categories": formattedCategories,
                "current_category": 'History'
            })
        except:
            print(sys.exc_info())
            abort(404)


    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def deleteQuestion(question_id):
        try:
            question = Question.query.get(question_id)
            question.delete()
        except:
            print(sys.exc_info())
            abort(422)
        return jsonify({
            'success': True
        })


    @app.route('/questions', methods=['POST'])
    def addQuestion():
        try:
            body = request.get_json()

            newQuestion = Question(
                question = body['question'],
                answer = body['answer'],
                difficulty = body['difficulty'],
                category = body['category']
            )

            newQuestion.insert()
        except:
            print(sys.exc_info())
            abort(400)

        return jsonify({
            'success': True
        })


    @app.route('/', methods=['POST'])
    def searchQuestions():
        try:
            body = request.get_json()
            searchQuery = body['searchTerm']
            searchItem = "%{}%".format(searchQuery)
            
            questions = Question.query.filter(Question.question.ilike(searchItem)).all()
            formattedQuestions = [question.format() for question in questions]

            return jsonify({
                'success':True,
                'questions': formattedQuestions,
                'total_questions': len(formattedQuestions),
                'current_category': 'History'
            })
        except:
            print(sys.exc_info())
            abort(400)


    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def getQuestionsByCategory(category_id):
        try:
            questions = Question.query.filter(Question.category == category_id).all()
            formattedQuestions = [question.format() for question in questions]
            currentCategory = Category.query.get(category_id)

            return jsonify({
                "success": True,
                "questions": formattedQuestions,
                'total_questions': len(formattedQuestions),
                'current_category': currentCategory.type

            })
        except:
            print(sys.exc_info())
            abort(404)


    @app.route('/quizzes', methods=['POST'])
    def playQuiz():
        try:
            body = request.get_json()
            previousQuestions = body['previous_questions']
            quizCategoryObject = body['quiz_category']
            quizCategory = quizCategoryObject['type']
            
            if quizCategoryObject['type'] != 'click':

                category = Category.query.filter(Category.type == quizCategory).first()
                questions = Question.query.filter(Question.category == category.id).all()
                formattedQuestions = [question.format() for question in questions]
                totalQuestions = len(formattedQuestions)
                
                randomIndexNumber = randint(0, (totalQuestions - 1))
                randomQuestion = formattedQuestions[randomIndexNumber]
               
               #Logic to check for repetitions
                while randomQuestion['id'] in previousQuestions:

                    randomIndexNumber = randint(0, (totalQuestions - 1))
                    randomQuestion = formattedQuestions[randomIndexNumber]

                    #Condition to break loop once 5 questions have been asked
                    if len(previousQuestions) == totalQuestions:
                        break
                
                return jsonify({
                    'previousQuestions': previousQuestions,
                    'question': randomQuestion
                })

            else:
                questions = Question.query.all()
                formattedQuestions = [question.format() for question in questions]
                totalQuestions = len(formattedQuestions)
            
                randomIndexNumber = randint(0, (totalQuestions - 1))
                randomQuestion = formattedQuestions[randomIndexNumber]
              
                #Logic to check for repetitions
                while randomQuestion['id'] in previousQuestions:

                    randomIndexNumber = randint(0, (totalQuestions - 1))
                    randomQuestion = formattedQuestions[randomIndexNumber]
            
                return jsonify({
                    'previousQuestions':previousQuestions,
                    'question': randomQuestion,
                })

        except:
            print(sys.exc_info())
            abort(400)

 
    @app.errorhandler(404)
    def notFound(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource was not found'
        })
    @app.errorhandler(405)
    def notAllowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method not allowed'
        })
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable'
        })
    @app.errorhandler(400)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request'
        })
    if __name__ == '__main__':
        app.run('0.0.0.0', debug=True)

    return app

create_app()