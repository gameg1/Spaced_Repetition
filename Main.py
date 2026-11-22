import os
import argparse # use later


def main():
    validate_shoebox()
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--add", nargs = 2, dest="cue_card",metavar=("question","answer"), help = "Adds a Cue card to your inbox")
    args = parser.parse_args()
    if args.cue_card:
        add_note(Q=args.cue_card[0], A=args.cue_card[1])


def add_note(Q,A):
    PATH = "./Shoebox/inbox"
    try:
        with open(PATH,"a") as file:
            print(f"{Q},{A}", file=file)
            print("Cuecard has been added with")
    except FileNotFoundError:
        print("Error, Inbox file not found")
        exit(1)


def look_note():
    pass

def delete_note():
    pass

def daily_spaced_rep():
    pass

def validate_shoebox():
    """Validates files for the shoebox if they don't exist"""
    PATH = "./Shoebox/"
    shoebox_files = ("inbox","level_1","level_2","level_3","level_4","level_5","level_6","level_7","outbox")
    dir_list = os.listdir(PATH)
    for file in shoebox_files:
        if (file not in dir_list) and PATH != "./":
            with open(PATH+ file,"w") as _:pass


def move_note_up():pass
def reset_note():pass

if __name__ == "__main__":
    main()