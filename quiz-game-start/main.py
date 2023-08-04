from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question_data[i]["text"], question_data[i]["answer"])
                 for i in range(len(question_data))]

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
