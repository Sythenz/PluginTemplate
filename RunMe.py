import os

TEMPLATE = ""
DESCRIPTION = ""
AUTHOR = ""

def Inputs(*args):
    global TEMPLATE, DESCRIPTION, AUTHOR

    arg1 = input("Plugin Name:")
    TEMPLATE = f"{arg1}"

    arg2 = input("Plugin Description:")
    DESCRIPTION = f"{arg2}"

    arg3 = input("Plugin Author:")
    AUTHOR = f"{arg3}"


def rename_folders_recursively(directory):
    global TEMPLATE, DESCRIPTION, AUTHOR

    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            oldpath = os.path.join(root, dir)
            if "{TEMPLATE}" in dir:
                newpath = os.path.join(root, dir.replace("{TEMPLATE}", TEMPLATE))
                os.rename(oldpath, newpath)
                print(newpath)
                
    for root, dirs, files in os.walk(directory):
        for file in files:
            oldpath = os.path.join(root, file)
            if "{TEMPLATE}" in file:
                newpath = os.path.join(root, file.replace("{TEMPLATE}", TEMPLATE))
                os.rename(oldpath, newpath) 
                print(newpath)

                print("Renaming references")
                with open(newpath, 'r') as file:
                    data = file.read()
                    data = data.replace("{TEMPLATE}", TEMPLATE)
                    data = data.replace("{DESCRIPTION}", DESCRIPTION)
                    data = data.replace("{AUTHOR}", AUTHOR)

                with open(newpath, "w") as file:
                    file.write(data)
                
                print("Replaced references in: " + newpath)


                
Inputs()

print("--------SPECIFIED INPUTS---------")
print("Plugin Name: " + TEMPLATE)
print("Description: " + DESCRIPTION)
print("Author: " + AUTHOR)


print("--------RENAMING FILES---------")
rename_folders_recursively(os.path.dirname(os.path.realpath(__file__)))


print("--------RENAMING TEMPLATE IN FILES---------")
