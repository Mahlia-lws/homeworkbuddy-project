from Homework import Homework


class Assignment(Homework):

    def __init__(self, name, subject, due_date, points, pages):
        super().__init__(name, subject, due_date, points)
        self.pages = pages

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Due Date:", self.due_date)
        print("Points:", self.points)
        print("Pages:", self.pages)


english1 = Assignment("AP Lit Essay", "English", "Aug 14", 50, 3)

english1.display()

#remember to merge everything together