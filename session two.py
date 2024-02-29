#looping throw the list using range
# n=["h","z","s"]
# m=[10,20,30]
# for i in range(len(n)):
#     print(n[i])
#     if m[i]< 10:
#         print("fail")
#     else:
#         print("pass")
#     # print(m[i])

# using the dictionary to make the same programme

# G12={
#     "hamza":10,
#     "ziad":20,
#     "sief":30
# }
# if you want to loop throw it use this rule for key in diction_name  key is the key and diction_name  [key] is the value
# for key in  G12:
    #here is the name
    # print(key)
    #here is the mark
    # print(G12[key])
# to add value to the diction we use this line we use diction_name[key]=value
# G12["mohamed"]=12
# print(G12)


#adding more data to the diction to make it mor complicated
numbrs=[10,20,30]
summ=0
for i in numbrs:
    sum=i+sum
print(sum)
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
for key in G12:
  sicienc_marks=  G12[key][2]["sc"]
  print(sum(sicienc_marks))

# programe to ask the user if you are teacher or student
#teacher: will see what is in the diction ask if you want to edit or add if edit i need to get the name and edit the valu if add get fdrom teaxher the key wich is name and values wich is group of numbers
#studen: will get his name only and then get for him the totla of tha whole marks
#it is not allowed to use chatgpt or any ai it is allowed to use google search