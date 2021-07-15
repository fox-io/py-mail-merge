"""
py-mail-merge/main.py

Mail Merge

Using a provided sample letter and names, this script will generate a series of
uniquely-named files containing a personalized version of the letter.

(c)2021 John Mann <github.fox-io@foxdata.io>
"""


def main():
    with open("./input/letter.txt") as letter_file:
        letter_contents = letter_file.read()

    with open("./input/names.txt") as names_file:
        names_contents = names_file.read()


if __name__ == "__main__":
    main()
