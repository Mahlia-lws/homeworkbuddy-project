from assignments import Assignment
from projects import Project



class HomeworkBuddy:
    def __init__(self):
        self.homework_list = [
            Assignment("AP Lit Essay", "English", "8/22", 50, 3),
            Project("Forensic Science Slideshow Presentation", "Science", "8/22", 100, 5),
            Assignment("AP Comp Sci 1.1-1.6 Entry", "Computer Science", "8/25", 30, 2),
            Assignment("Econ. Visualizer", "Economics", "8/19", 25, 2),
            Project("Psych 2 Childhood Development Presentation", "Psychology", "8/23", 50, 6),

            
        ]



    def show_menu(self):
        while True:
            print("\n==============================")
            print("       ☆ HOMEWORK BUDDY ☆")
            print("==============================")
            print("Welcome to the Homework Buddy!")
            print("1. Show homework ")
            print("2. Add homework")
            print("3. Show all homework")
            print("4. Exit")



            choice = input("Choose an option:")


            if choice == "1":
                self.show_homework()


            elif choice == "2":
                self.add_homework()


            elif choice == "3":
                self.show_total()
    

            elif choice == "4":
                print("Goodbye!")
                break



            else:
                print("Please enter a valid option •́︵•̀!")



    def show_homework(self):
        if len(self.homework_list) == 0:
            print("Your homework list is empty good job!")
            return

        print("\n☆☆☆☆☆ YOUR HOMEWORK ☆☆☆☆☆")

        for number, homework in enumerate(self.homework_list, 1):
            print(f"\n{number}.")
            homework.display()


    
    def add_homework(self):
        print("\n☆☆☆☆☆ ADD YOUR HOMEWORK ☆☆☆☆☆")
        print("1. Assignments")
        print("2. Projects")

        kind = input("What kind of homework do you want to add?")

        if kind == "1":
            name = input("Enter the assignment !!name:")
            subject = input("Enter the subject:")
            due_date = input("Enter the due date:")
            points = input("Enter the points:")
            pages = input("Enter the page count:")

            new_homework = Assignment(name, subject, due_date, points, pages)
            self.homework_list.append(new_homework)

            print("Assignment added!")

        
        elif kind == "2":
            name = input("Enter the project name:")
            subject = input("Enter the subject:")
            due_date = input("Enter the due date:")
            points = input("Enter the points:")
            slides = input("Enter the slide count:")


            new_homework = Project(name, subject, due_date, points, slides)
            self.homework_list.append(new_homework)

            print("Project added!")

        

        else:
            print("Invalid choice •́︵•̀!")

    
    def show_total(self):
        total = len(self.homework_list)

        print("\n☆☆☆☆☆ YOUR TOTAL HOMEWORK ☆☆☆☆☆")
        print(f"You have {total} homework assignments/projects!")
