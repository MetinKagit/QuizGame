from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import logo

if __name__ == '__main__':
    print(logo.logo)
    question_bank = []
    for question in question_data:
        QUESTION_TEXT = question["question"]
        QUESTION_ANSWER = question["correct_answer"]
        new_question = Question(QUESTION_TEXT, QUESTION_ANSWER)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.has_question():
        quiz.next_question()

    print("You have complete the quiz.")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}.")
