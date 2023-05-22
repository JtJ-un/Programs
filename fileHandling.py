with open("list.txt", "r") as file:
    names = file.readlines()

names = [name.strip() for name in names]
names.sort()

with open("list.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
