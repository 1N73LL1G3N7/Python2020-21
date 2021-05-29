# HEALTH MANAGEMENT SYSTEM PROJECT
import datetime


def getdate():
    return datetime.datetime.now()


def take(NameToSave):
        log_retrieve = input("What do you want to do ? Log or Retrieve ?\n")
        if log_retrieve == "Log":
            log_type = input("What do you want to log, Exercise or Diet ?\n")
            if log_type == "Exercise":
                FileName2 = NameToSave + "_exercise" + ".txt"
                with open(FileName2, "a") as f:
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
                FileName1 = NameToSave + "_diet" + ".txt"
                with open(FileName1, "a") as f:
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
                with open(FileName2) as f:
                    a = f.readlines()
                    print(a)
            elif retrieve_type == "Diet":
                with open(FileName1) as f:
                    a = f.readlines()
                    print(a)

    

NameToSave = input("Please enter your name :")
take(NameToSave)
