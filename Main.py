import os
import argparse # use later
SHOEBOX_PATH = "./Shoebox/"
SHOEBOX_FILES = ("inbox","level_1","level_2","level_3","level_4","level_5","level_6","level_7","outbox")
PROFILE_PATH = "./Profile/"

def main():
    validate_shoebox()
    validate_profile()
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--add", nargs = 2, dest="cue_card",metavar=("question","answer"), help = "Adds a Cue card to your inbox")
    parser.add_argument("-l","--look", action= "store_true")
    args = parser.parse_args()
    if args.cue_card:
        add_note(Q=args.cue_card[0], A=args.cue_card[1])
    if args.look:
        look_notes()


def add_note(Q,A):
    """Adds a cue card to the inbox as a question/answer pair"""
    try:
        with open(SHOEBOX_PATH + SHOEBOX_FILES[0],"a") as file:
            print(f"{Q},{A}", file=file)
            print("Cuecard has been added with")
    except FileNotFoundError:
        print("Error, Inbox file not found")
        exit(1)


def look_notes():
    """Prints out a list of all questions and answers for each area"""
    #TODO, Parse these files as csv files properly.
    #TODO, Paree questions with LeTeX.
    for file in SHOEBOX_FILES:
        print(file)
        with open(SHOEBOX_PATH + file, "r") as notes:
            for note in notes.readlines():
                question,answer = note.strip().split(",")
                print(f"   Question:{question}| Answer:{answer}")

def delete_note():
    pass

def daily_spaced_rep():
    pass

def validate_shoebox():
    """Validates files for the shoebox if they don't exist"""
    dir_list = os.listdir(SHOEBOX_PATH)
    for file in SHOEBOX_FILES:
        if (file not in dir_list) and SHOEBOX_PATH != "./":
            with open(SHOEBOX_PATH + file,"w") as _:pass

def validate_profile():
    """ Validates files for the user's profile if they dont exist"""
    dir_list = os.listdir(PROFILE_PATH)
    # if profile is empty
    if not dir_list:
        try:
            with open(PROFILE_PATH+"User","w") as file:
                # name: Default - anon
                print("Name: anon",file= file)
                # day : Default - 1
                print("Day: 1", file= file)
                # pattern:
                pattern = ((2,1),#1
                           (3,1),
                           (2,1),
                           (4,1),
                           (2,1),
                           (3,1),
                           (2,1),
                           (1), #8
                           (2,1),
                           (3,1),
                           (2,1),
                           (5,1),
                           (4,2,1),
                           (3,1),
                           (2,1),
                           (1), #16
                           (2,1),
                           (3,1),
                           (2,1),
                           (4,1),
                           (2,1),
                           (3,1),
                           (2,1),
                           (6,1),
                           (2,1),
                           (3,1),
                           (2,1),
                           (5,1),
                           (4,2,1),
                           (3,1),
                           (2,1),
                           (1), #32
                           (2,1),
                           (3,1),
                           (2,1),
                           (4,1),
                           (2,1),
                           (3,1),
                           (2,1),
                           (1), #40
                           (2,1),
                           (3,1),
                           (2,1),
                           (5,1),
                           (4,2,1),
                           (3,1),
                           (2,1),
                           (1), #48
                           (2,1),
                           (3,1),
                           (2,1),
                           (4,1),
                           (2,1),
                           (3,1),
                           (2,1),
                           (7,1),#56
                           (2,1),
                           (3,1),
                           (6,1),
                           (5,1),
                           (4,2,1),
                           (3,1),
                           (2,1),
                           (1), #64
                           )
                print("Pattern: "+ str(pattern), file=file)
                # amount: Default - 5
                print("Amount: 5",file=file)
        except FileNotFoundError:
            print("Error, file not found")
            exit(1)

def move_note_up():pass
def reset_note():pass

if __name__ == "__main__":
    main()