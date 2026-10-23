from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_Bank = []
for que in question_data:
    question_text = que["text"] 
    question_answer = que["answer"]
    new_question = Question(question_text, question_answer)
    Question_Bank.append(new_question)

quiz = QuizBrain(Question_Bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")