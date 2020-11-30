# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

##here are stored chinese charecters and translates
FILE_NAME ="words.txt"


def read_from_file(filename)->bool:
    # TODO make what fuction reads in proper way words and stors then in dir
    try:
        with open(filename) as f:
            print(f.read())
            # Do something with the file
    except IOError:
        return False
    return True

def main():
    # check if input file provided
    if FILE_NAME =="":
        # TODO better file detection
        print("no file name provided,programme quite!!!")
        return
    # check if file can be opened and read it if so
    if not read_from_file(FILE_NAME):
        print("File \""+str(FILE_NAME)+"\" not readable, programme quite")
        return

    current_chose = ''

    while True:
        #TODO write what can user chose from
        if current_chose == 'q':
            break
        current_chose=input()
        print("to get out of press q key")
        # TODO write part where shows up in console stuff
        while True:
            pass

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
