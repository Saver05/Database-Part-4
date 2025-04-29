import database


def main():
    conn = database.Database("root","password","database")
    print("Welcome to MuskieCo.\n")
    print("Which task would you like to perform?")


if __name__ == "__main__":
    main()