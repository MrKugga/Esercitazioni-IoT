if __name__ == "__main__":

    while True:
        print("""The available commands are:

d -> Distance between two points.
m -> Move a point according to a vector
q -> Quit
""")
        user_input = input("-> ")

        if user_input == "d":
            pass
        elif user_input == "m":
            pass
        elif user_input == "q":
            break
        else:
            print("Command not recognized")

    print("\nGoodbye!")
