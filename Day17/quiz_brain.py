import os
class QuizBrain:
          
       def __init__(self,q_list):
              self.questionNumber = 0
              self.score = 0
              self.questionList = q_list
       def startQuiz(self):
              print(f"Q.{self.questionNumber+1} {self.questionList[self.questionNumber]['question']}")
              curAnswer = input("type 'True' or 'False' : ").lower()
              if(curAnswer==self.questionList[self.questionNumber]['answer']):
                     print("Right Answer")
              else:
                     print("Wrong Answer")
              self.questionNumber+=1
              self.calcScore(curAnswer==self.questionList[self.questionNumber]['answer'])
              input('press any key to continue...')
              os.system('cls')
              
       def calcScore(self,isCorrect):
              if(isCorrect):self.score+=1
              
       def endQuiz(self):
              print("Quiz has ended!😇")
              print(f"your score is {self.score}/12.")
              
      
              
              
       