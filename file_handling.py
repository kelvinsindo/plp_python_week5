
def create_and_write_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Line 1: Hello, World!\n")
            file.write("Line 2: Welcome to file handling\n")
            file.write("Line 3: You will love working with files\n")
        print("File has been created and written successfully.")
    except PermissionError:
        print("Error: Permission error. ")
    finally:
        print("Successfully writen.\n")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File contents:\n")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    finally:
        print("Succefully read.\n")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Line 4: Appending this line.\n")
            file.write("Line 5: write more content.\n")
            file.write("Line 6: Your line has been added to the file.\n")
        print("Lines appended successfully.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("Successful appended.\n")


if __name__ == "__main__":
    create_and_write_file()

    read_file()

    append_to_file()

    read_file()