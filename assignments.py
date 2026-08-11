from Homework import Homework
class Assignments(Homework):

    def __init__(self, name, subject, due_date, points, questions):
        super().__init__(name, subject, due_date, points)
        self.questions = questions

    def display(self):
        
