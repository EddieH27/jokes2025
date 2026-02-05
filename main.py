


# # make this performance task ready for submission
# # To give the user a fun experience hearing knock knock jokes

# joke = input("Do you want to hear a joke? ")
# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")

joke_data = {
    "robbers": {"setup": "Calder ", "response": "", "punchline": "Calder police - I've been robbed!"},
    "tanks": {"setup": "Tank ", "response": "You are welcome! ", "punchline": ""},
    "pencils": {"setup": "Broken pencil ", "response": "", "punchline": "Nevermind, it's pointless!"}
} #my list of jokes and the values for each step of the joke

def tell_joke(setup, response, punchline): #defines the function and its components
    for i in range(1):
        input("Knock Knock ")# everything from this line to 52 makes the code follow the specific order of the joke and responses
        input(setup)
        if response:
            input(response)
        if punchline:
            print(punchline)

def get_rating(): #this line to line 62 allows for the user to input their opinion/rating and it allows for the code to judge the rating
    rate = int(input("Please rate our game 1-10! ")) 
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")
    if friend in ["yes", "maybe"]:
        print("Thanks, we appreciate it.")
    else:
        print("Sorry you did not enjoy it.")

joke = input("Do you want to hear a joke? ")  # this section of code prints responses for the user inputs.
if joke == "no":
    print("Okay suit yourself!")
while joke == "yes":
    print("Great, Let's Play")
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    if question in joke_data:
        tell_joke(**joke_data[question])
        del joke_data[question]   #this last part of code deletes the joke from the list after it has been told
    else:
        print("That joke is no longer available!")
    joke = input("Do you want to hear another joke or are you finished? ")
if joke == "finished":
    get_rating()