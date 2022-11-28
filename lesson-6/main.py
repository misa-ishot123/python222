# ints = []
# try:
#     f = open("1.txt") #opened file put in f
# except FileNotFoundError:
#     print("dumbass you deleted the file")
# else:
#
#     try:
#         for line in f: #проходим по кждей строке файла
#             ints.append(int(line)) #.appends(x) - add element x in list
#     except ValueError:
#         print("here no number")
#     else: #it will work if we have no mistakes
#         print("you is Baldez!")
#         print(ints)
#     finally:  #will work anyways with or without mistakes
#         f.close()
#         print("I closed the file")
try:
    name = input("Username:")
    if name == "oh,leg":
        raise ValueError("This name is already used.")
except ValueError as error_msg:
    print("Boi choose another one!!", error_msg)



