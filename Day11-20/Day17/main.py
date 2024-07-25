from question_model import Question
from data import question_data
from quiz_brain import QuizBrain  
curQuiz = QuizBrain(question_data)   
for _ in range(11): 
       QuizBrain.startQuiz(curQuiz)
curQuiz.endQuiz()


       
