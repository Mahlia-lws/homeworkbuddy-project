class Homework:
    def __init__(self, name, subject, due_date, points):
        self.name = name
        self.subject = subject
        self.due_date = due_date
        self.points = points

    def valid_points(self): 
        if self.points >= 0:
            return True
        else:
            return False 


    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Due Date:", self.due_date)
        print("Points:", self.points)  #This is just a test run

# homework1 = Homework("Math Worksheet", "Math", "Aug 12", 25) Test run
# homework1.display()        

#Check with L.E and Sydney about thr orange line on the side
#
#add homework1 & homework1.display to main on Wednesday
