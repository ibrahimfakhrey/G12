# print("hello world")
# x = "3"
# print(x)
# change the variable into int
# x = 3
# print(x * 4)
# take the input from the user
# x=input("please enter your name ")
# print("HI "+ x )
# secret="ziad"
# if x.lower() == secret.lower():
#     print("hello ")
# else:
#     print("noo")
names = ["sief", "ziad"]

#adding an item to the list
names.append("hamza")
# lopping throw the list using for
# for i in names:
#     if i =="ziad":
#         print("zyad")
#     else:
#         print(i)


user_input=input("please enter the name you want to input")
if user_input in names:
    edit_name=input("please enter the name you want to edit ")
    for i in names:
        if i ==user_input:
            print(edit_name)
        else:
            print(i)
else:
    print("this name is not registered ")