def main():
    feeling = input("Do you want to start? y/n: ").lower()

    if feeling == "n":
        print("closing feelings generator. ")
        print("have a nice day :) ")
        exit()

    while feeling != "y":
        print("please try again")
        feeling = input("Do you want to start? y/n: ").lower()

    while feeling == "y":

        print("")

        # Output a feeling
        print("A: I Feel a bit worried.")
        print("B: I Feel a bit happy.")
        print("C: I Feel a bit angry.")
        print("D: I Feel a bit sad.")

        print("")

        # Output instructions

        print("")
        print("Enter the letter that shows how you feel.")

        # Creates a variable called feeling that stores the users input.
        # Notice the space. It's important.
        output_feelings = input("Choose a feeling from the options: ").lower()

        print("")

        if output_feelings == "a":
            print()
            print("You can destroy your now, by worrying about tomorrow.")
            print()
            print("Janis Joplin")
            print()

        elif output_feelings == "b":
            print()
            print("Do not set aside your happiness. Do not wait to be happy in the future. The best time to be happy "
                  "is "
                  "always now.")
            print()
            print("Roy T. Bennett")
            print()

        elif output_feelings == "c":
            print()
            print("Anybody can become angry — that is easy, but to be angry with the right person and to the right "
                  "degree ")
            print("and at the right time and for the right purpose, and in the right way — that is not within "
                  "everybody's ")
            print("power and is not easy.")
            print()
            print("Aristotle")
            print()

        elif output_feelings == "d":
            print()
            print(
                "There are moments when I wish I could roll back the clock and take all the sadness away, but I have ")
            print("the feeling that if I did, the joy would be gone as well.")
            print()
            print("Nicholas Sparks")
            print()

        feeling = input("Do you want to continue? y/n: ").lower()

        if feeling == "n":
            print("closing feelings generator. ")
            print("have a nice day :) ")
            exit()

        while feeling != "y":
            print("please try again")
            feeling = input("Do you want to continue? y/n: ").lower()

            if feeling == "n":
                print("closing feelings generator. ")
                print("have a nice day :) ")
                exit()


main()
