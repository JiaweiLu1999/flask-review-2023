class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = f"Q.{self.question_number}: {question.text} (True/False)?: "
        user_answer = input(question_text)
        self.check_answer(user_answer, question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is: {question_answer}.")
        print(f"Your current score is: {self.score}/{len(self.question_list)}.")
