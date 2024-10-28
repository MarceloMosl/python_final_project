from main_switcher import switcher


def main():
    programShouldRun = True

    while programShouldRun:
        print("\n\nAdvanced To-Do List Application")
        print("1. CSV")
        print("2. Data Management")
        print("3. Data Vizualization")
        print("4. Spending Analysis")
        print("5. Exit")

        # get user input
        userInput = input("Enter your choice: ")

        # check if the user wants to exit
        if userInput == "5":
            programShouldRun = False
            print("Exiting the application. Goodbye!")
            break

        # call the switch function to handle the menu option
        switcher(userInput)


if __name__ == "__main__":
    main()
