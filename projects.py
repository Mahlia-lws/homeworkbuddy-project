

from Homework import Homework

class Project(Homework):

    def __init__(self, name, subject, due_date, points, slides):
        super().__init__(name, subject, due_date, points)
        self.slides = slides

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Due Date:", self.due_date)
        print("Points:", self.points)
        print("Slides:", self.slides)

# forensic_science1 = Projects("Forensic Science Slideshow Presentation", "Science", "Aug 19", 100, 7). Test run

# forensic_science1.display()
        
