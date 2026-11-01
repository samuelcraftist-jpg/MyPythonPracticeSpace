with open("input.txt", "r") as file:

    lines = file.readlines()


with open("output.txt", "w") as new_file:

    for i in range(len(lines)):

        if i % 2 == 0:
            new_file.write(lines[i])


print("Odd lines copied successfully")