import os

file = open("text.txt", "r")
print(file.name)
print(file.mode)
print(file.closed)

with open("text.txt", "r") as file:
    print(file.read(4))
    print(file.readlines())
    print(file.tell())
    file.seek(0)

with open("text.txt", "w") as file:
    file.write("Something text\n")
    file.writelines(["Firrst line", "Second line"])

print(os.listdir())

print(os.path.abspath("text.txt"))
print(os.path.basename(os.path.abspath("text.txt")))
print(os.path.exists("text.txt"))
print(os.path.getsize("text.txt"))
print(os.path.join(os.getcwd(), "text.txt"))

# Glob
import glob

print(glob.glob("example/test*"))