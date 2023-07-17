# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="w") as file:
    file.write("yo!")

with open("new_file.txt", mode="w") as file:
    file.write("dfsafdafs")