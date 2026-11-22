import os
import argparse # use later


def main():
    validate_shoebox()
    pass


def add_note():
    # if shoebox is empty / not have correct number of levels/inbox and outbox, create the files.
    pass


def look_note():
    pass

def delete_note():
    pass

def daily_spaced_rep():
    pass

def validate_shoebox():
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