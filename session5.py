# in this session we will learn the random and the function
import random
# #random between two numbers
# x=random.randint(2,10)
# print(x)

# #random between choice
#
# names=["hamza","ziad","sief"]
# x= random.choice(names)
# print(x)

# we use the funtction when there is a part wich will be repeted throw the code
def new():
    print("this is the first fuction for me ")
# new()
# new()

# the function could return somthing string or number or boolean

# def second(parameter):
#     if parameter=="ziad":
#         return "i got ziad"
#     elif parameter =="hamza":
#         return "i got hamza"
# print(second("ibrahim"))
 # rock paper scissor game
import random
def get_user_choice():
    user_input=input("please enter your choice rock paper scissor \n").lower()
    while user_input not in ["rock","paper","scissor"]:
        user_input=input("please enter your choice rock paper scissor \n").lower()
    return user_input
def pc_choice():
    return random.choice(["rock","paper","scissor"])
def detrmin_winner(user,pc):
    if user ==pc:
        return "tie"
    elif(user=="rock" and pc =="scissor") or (user=="paper" and pc =="rock") or (user=="scissor" and pc=="paper"):
        return "you won"
    else:
        return "computer wins"


print("lets play \n")
while True:
    user=get_user_choice()
    pc=pc_choice()
    print(f"{detrmin_winner(user,pc)}  the user chose {user} and the computer chose {pc}")
    dewcision=input("do you want to play again ").lower()
    if dewcision != "yes":
        break



