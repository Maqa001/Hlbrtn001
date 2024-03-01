def check_alive():
    choice = input("Is the object alive? (yes/no): ").lower()
    if choice == "yes":
        print("The object is alive.")
    elif choice == "no":
        print("The object is not alive.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        check_alive()


def main():
    print("Welcome to the object alive checker!")
    print("Please answer the following question to determine if the object is alive or not.")

    check_alive()


if __name__ == "__main__":
    main()
