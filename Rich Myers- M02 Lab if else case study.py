# Rich Myers- M02 Lab if else case study
# my program will take input from students and tell them if they have made the Dean's list!

lastName = input('Hello student! Please enter your Surname or key in "zzz" to exit program!')
while lastName != "zzz"
    gpa = float(input("Please enter your Grade Point Average!"))
    firstName = input("Please enter your first name!")
    if gpa >= 3.5
        print("Good job" + firstName + lastName "you are on the Dean's List this semester!")
    elif gpa >= 3.25
        print("Excellent work" + firstName + lastName +"! You are on the honor roll this semester!")
        break
