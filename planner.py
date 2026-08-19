from Assignment import Assignment
from Projects import Projects


class HomeworkBuddy:
    def __init__(self):
        self.homework_list = [
            Assignment("AP Lit Essay", "English", "Aug 14", 50, 3)
            Assignment()
        ]

    def show_menu(self):
        while True:
            print("\n==============================")
            print("       ☆ HOMEWORK BUDDY ☆")
            print("==============================")
            print("   Welcome to the Homework Buddy!")
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
                self.show_all()
                break

            else:
                print("Please enter a valid option •́︵•̀")

            

            



 