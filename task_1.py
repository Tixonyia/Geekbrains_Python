import os
try:
    while True:
        file_name = input("Enter file name with extension .txt: ")
        if file_name in os.listdir():
            print("Such file already exists.")
        elif file_name[-4::] != ".txt":
            continue
        else:
            with open(file_name, 'a') as file:
                while True:
                    string_user = input("Enter string: ")
                    if string_user == "":
                        break
                    else:
                        file.write(string_user + "\n")
            break
except IOError:
    print("Output input error.")
