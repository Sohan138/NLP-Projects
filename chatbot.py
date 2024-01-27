print(
    """
    hello ! how are you ?
    hope you are doing well !
    Welcome to your chatbot at university portal
    Please provide your details below:
    """
)

Student_id = int(input("Enter your Student id number: "))
Name = input("Enter your Full name: ")  # Corrected typo in variable name
Age = int(input("Enter your Age: "))

if Age <= 18:
    print("Wow! You are too young to study at the university.")
elif 18 < Age < 24:  # Simplified condition
    print("You are eligible for our 24-pass discount for our canteen.")
elif 25 <= Age < 35:  # Simplified condition
    print("It's never too late to start studying.")
else:
    print(f"Age is just a number. You can still enroll at {Age} in our program.")

Email_id = input("Enter your email id: ")
Date_of_birth = input("Enter your Date of Birth: ")
Location = input("Enter your campus location: ")  # Corrected variable name
fav_colour = input("Please enter your favorite color: ")

if fav_colour.lower() == "red":  # Consider case-insensitive comparison
    print("""
    1. Please check out our red club which provides a 30% discount on your enrollment.
    2. Please check out our red football team if you'd like to participate.
    3. Please check out our red coupon for more shopping.
    """)
elif fav_colour.lower() == "blue":
    print("""
    1. Check out our blue sports club.
    2. Check out our blue discount coupon.
    """)
elif fav_colour.lower() == 'yellow':
    print("""
    If you like the color YELLOW, I have the following for you! Check out:
    1. Our werewolf society
    2. Our hiking club
    3. Our mountain climbing club
    4. Our dance club
    5. Our suntan society.
    """)
else:
    print("I'm not sure if that was a color you entered, please try again.")

questions = [
    "Where can I find the office?",
    "When will my course start?",
    "How can I pay my fees?",
    "Where will my class timetable be available?",
    "Where can I find out my tutor's name?",
    "If any other question",
]

answers = [
    "The office is situated in the left corner of the entrance.",
    "Course details are available in the university course section.",
    "For payment fees, check out options on the website under the fees section.",
    "Class timetables will be emailed before the course starts.",
    "Tutor names will be provided in the timetable email.",
    "Please email at xyz@email.com or call on 022222222, Monday to Friday between 10-5.",
]

while True:
    question = input("\nDo you have a question for me? (yes/no)\n")

    if question.lower() == "yes":
        print("\nHere are some common questions:\n")
        for i, q in enumerate(questions, 1):
            print(f"{i}: {q}")
        print()
        question_num = int(input("Please enter the number corresponding to your question: ")) - 1
        print(answers[question_num])
    elif question.lower() == "no":
        print("Thanks for visiting!")
        break
    else:
        print("Please enter a valid input (yes/no).")
