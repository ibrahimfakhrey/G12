# last task is to make a simple grading certificate
G12={
    "hamza":[
        {
            "e":[5,10,23]
        },
        {
            "m":[3,20,23]
        },
        {
            "sc":[20,30,5]
        }
    ],
    "ziad":[
        {
            "e":[5,10,23]
        },
        {
            "m":[3,20,23]
        },
        {
            "sc":[20,30,5]
        }
    ]
}
user_input=input("welcom to ams school \n if you are one of the teachers press one else press two \n")
teachers={
    "admin":"admin"
}
students={
    "hamza":"123",
    "ziad":"0000",
    "sief":"1111"
}
if int (user_input)==1:
    #he is one of the teachers
    #check if the user is in the database of the teacher i should take the name and the password
    user_name=input("please enter your user_name \n")
    if user_name in teachers:
        #i will ask about the password
        password=input(f"please ente the password for {user_name}\n")
        if password==teachers[user_name]:
            # give the control for the techer
            teacher_choice=input(f"welcom{user_name} lets make some modification\n "
                                 f" if you want to edit special data in the database press 1 \n"
                                 f"if you want to get the total of any student press 2 \n ")
            # teacher sshould press one or two or else
            if int(teacher_choice)==1:
                #printing the data base of g 12
                for key in G12:
                    print(key)
                    print("_____________")
                    print(G12[key])

                    print("_____________")
                # get the target person that we will edit
                target=input("which name you want to edit his makrs  remember to write the correct name \n")
                #check if the target is in the database
                if target in G12:
                    science_marks=[]
                    english_marks=[]
                    math_marks=[]
                    #get the  marks
                    for i in range(3):
                        englis_one=input("please give me the english mark")

                        math_one=input("please give me the math mark")
                        science_one=input("please give me the science mark")
                        science_marks.append(science_one)
                        english_marks.append(englis_one)
                        math_marks.append(math_one)
                    #make formate of the new data
                    new=[ {"e":english_marks},{"m":math_marks},{"sc":science_marks}]
                    #set the
                    G12[target]=new
                    print("data registered successfully \n")
                    print(G12)


                else:
                    print("it seams that this one is not in my data base ")


            # if the choice was to see the totla
            elif int(teacher_choice)==2:
                # i should ask about the target
                target=input("please give me the name that you want to see the total for him\n")
                # check if the target is in the data base
                if target in G12:
                    english_total=sum(G12[target][0]["e"])
                    math_total=sum(G12[target][1]["m"])
                    science_total=sum(G12[target][2]["sc"])
                    print(f"the marks of {target} is : \n"
                          f"{english_total + math_total+science_total}\n"
                          f"with English:{english_total}\n"
                          f"Math:{math_total}\n"
                          f"science{science_total}")

                else:
                    print("somthing went wrong ")
                pass
            else:
                print("somthing went wrong ")
        else:
            print("wrong credential  please write the correct password ")
    else:
        print("sorry wrong username \n")




elif int(user_input)==2:
    #he is one of the students
    pass
else:
    print("wrong input please call the support ")

