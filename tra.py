import names

def check_first_name(first_name):
    found = False
    for i in range(10000):
        random_name = names.get_first_name()
        if first_name.lower() == random_name.lower():
            found = True
            print("This is a valid first name.")
            break
    if not found:
        print("This is not a valid first name.")

def main():
    print("Welcome to the first name checker!")
    first_name = input("Enter a first name to check: ")

    check_first_name(first_name)

if __name__ == "__main__":
    main()
