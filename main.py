"""
py-mail-merge/main.py

Mail Merge

Using a provided sample letter and names, this script will generate a series of
uniquely-named files containing a personalized version of the letter.

(c)2021 John Mann <github.fox-io@foxdata.io>
"""


def main():
    NAME_TEMPLATE = "[name]"

    # Read in a copy of our letter.
    with open("./input/letter.txt") as letter_file:
        letter_contents = letter_file.read()

    # Read in the contents of our names.txt file.
    with open("./input/names.txt") as names_file:
        names_contents = names_file.read()

        # Convert the contents to a list of names.
        name_list = names_contents.split("\n")

        for name in name_list:
            # Replace our template tag with each name.
            letter_output = letter_contents.replace(NAME_TEMPLATE, name)

            # Save each file individually named.
            with open(f"./output/letter-{name}", "w") as output_file:
                output_file.write(letter_output)


if __name__ == "__main__":
    main()
