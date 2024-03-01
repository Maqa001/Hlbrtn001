import names

def check_name(name):
    if name.lower() in (n.lower() for n in names._data['names']):
        print("This is a real name of a person.")
    else:
        print("This is not a real name of a person.")


def main():
    print("Welcome to the name authenticity checker!")
    print("Please enter a name to check if it's a real name of a person.")

    name = input("Enter name: ")

    check_name(name)


if __name__ == "__main__":
    main()