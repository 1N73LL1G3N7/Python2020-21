# HEALTH MANAGEMENT SYSTEM PROJECT
import datetime


def getdate():
    return datetime.datetime.now()


def take(client_name):
    if client_name == "Ashish":
        log_retrieve = input("What do you want to do ? Log or Retrieve ?\n")
        if log_retrieve == "Log":
            log_type = input("What do you want to log, Exercise or Diet ?\n")
            if log_type == "Exercise":
                with open("Ashish_Exercise.txt", "a") as f:
                    exercise = input("What do you want to add ?\n")
                    f.write(str([str(getdate())]) + ": " + exercise + "\n")
                    print("Added Successfully")
                    again = input("Do you want to add more ?, Yes or No\n")
                    while again == "Yes":
                        exercise = input("What do you want to add ?\n")
                        f.write(str([str(getdate())]) + ": " + exercise + "\n")
                        print("Added Successfully")
                        again = input("Do you want to add more ?, Yes or No\n")
            elif log_type == "Diet":
                with open("Ashish_diet.txt", "a") as f:
                    diet = input("What do you want to add ?\n")
                    f.write(str([str(getdate())]) + ": " + diet + "\n")
                    print("Added Successfully")
                    again = input("Do you want to add more ?, Yes or No\n")
                    while again == "Yes":
                        diet = input("What do you want to add ?\n")
                        f.write(str([str(getdate())]) + ": " + diet + "\n")
                        print("Added Successfully")
                        again = input("Do you want to add more ?, Yes or No\n")
        elif log_retrieve == "Retrieve":
            retrieve_type = input("What do you want to retrieve, Exercise or Diet ?\n")
            if retrieve_type == "Exercise":
                with open("Ashish_Exercise.txt") as f:
                    a = f.readlines()
                    print(a)
            elif retrieve_type == "Diet":
                with open("Ashish_diet.txt") as f:
                    a = f.readlines()
                    print(a)

    elif client_name == "Harry":
        log_retrieve = input("What do you want to do ? Log or Retrieve ?\n")
        if log_retrieve == "Log":
            log_type = input("What do you want to log, Exercise or Diet ?\n")
            if log_type == "Exercise":
                with open("Harry_Exercise.txt", "a") as f:
                    exercise = input("What do you want to add ?\n")
                    f.write(str([str(getdate())]) + ": " + exercise + "\n")
                    print("Added Successfully")
                    again = input("Do you want to add more ?, Yes or No\n")
                    while again == "Yes":
                        exercise = input("What do you want to add ?\n")
                        f.write(str([str(getdate())]) + ": " + exercise + "\n")
                        print("Added Successfully")
                        again = input("Do you want to add more ?, Yes or No\n")
            elif log_type == "Diet":
                with open("Harry_diet.txt", "a") as f:
                    diet = input("What do you want to add ?\n")
                    f.write(str([str(getdate())]) + ": " + diet + "\n")
                    print("Added Successfully")
                    again = input("Do you want to add more ?, Yes or No\n")
                    while again == "Yes":
                        diet = input("What do you want to add ?\n")
                        f.write(str([str(getdate())]) + ": " + diet + "\n")
                        print("Added Successfully")
                        again = input("Do you want to add more ?, Yes or No\n")
        elif log_retrieve == "Retrieve":
            retrieve_type = input("What do you want to retrieve, Exercise or Diet ?\n")
            if retrieve_type == "Exercise":
                with open("Harry_Exercise.txt") as f:
                    a = f.readlines()
                    print(a)
            elif retrieve_type == "Diet":
                with open("Harry_diet.txt") as f:
                    a = f.readlines()
                    print(a)

    elif client_name == "Rohan":
        log_retrieve = input("What do you want to do ? Log or Retrieve ?\n")
        if log_retrieve == "Log":
            log_type = input("What do you want to log, Exercise or Diet ?\n")
            if log_type == "Exercise":
                with open("Rohan_Exercise.txt", "a") as f:
                    exercise = input("What do you want to add ?\n")
                    f.write(exercise)
                    print("Added Successfully")
                    again = input("Do you want to add more ?, Yes or No\n")
                    while again == "Yes":
                        exercise = input("What do you want to add ?\n")
                        f.write(str([str(getdate())]) + ": " + exercise + "\n")
                        print("Added Successfully")
                        again = input("Do you want to add more ?, Yes or No\n")
            elif log_type == "Diet":
                with open("Rohan_diet.txt", "a") as f:
                    diet = input("What do you want to add ?\n")
                    f.write(diet)
                    print("Added Successfully")
                    again = input("Do you want to add more ?, Yes or No\n")
                    while again == "Yes":
                        diet = input("What do you want to add ?\n")
                        f.write(str([str(getdate())]) + ": " + diet + "\n")
                        print("Added Successfully")
                        again = input("Do you want to add more ?, Yes or No\n")
        elif log_retrieve == "Retrieve":
            retrieve_type = input("What do you want to retrieve, Exercise or Diet ?\n")
            if retrieve_type == "Exercise":
                with open("Rohan_Exercise.txt") as f:
                    a = f.readlines()
                    print(a)
            elif retrieve_type == "Diet":
                with open("Rohan_diet.txt") as f:
                    a = f.readlines()
                    print(a)


inp = input("Enter the name of the client :\n")
take(inp)
