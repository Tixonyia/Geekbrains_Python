def name_file(name_file_def="Text.txt"):
    with open(name_file_def, "r") as file:
        list_string = file.readlines()
        words = 0
        for i in enumerate([len(n.split()) for n in list_string], 1):
            words += i[1]
            print(f"The line {i[0]} contains the {i[1]} words.")
        print(f"Total lines {i[0]}. Total words {words}")


while True:
    try:
        name = input("Enter file name(Text.txt default): ")
        if not name:
            name_file()
            break
        else:
            name_file(name)
            break
    except FileNotFoundError:
        print(f"No such file or directory: '{name}'")
    except IOError:
        print("Output input error.")
