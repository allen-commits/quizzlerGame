from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer) #uses Question type object to hold the text and answer.
    question_bank.append(new_question) #adds the Question type object to the question_bank list, declared above.

quiz = QuizBrain(question_bank) #passes the question_bank list to a QuizBrain object.
quiz_ui = QuizInterface(quiz) #passes the QuizBrain object to a QuizInterface object.