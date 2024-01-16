print("Hello world!")


def greet_someone():
    input_name = input("What is your name?\t")
    # Define minimum length of name
    name_min_length = 2
    # Define maximum length of name
    name_max_length = 30
    # Prevent empty prints when length of name is wrong
    dont_print = False
    if len(input_name) < name_min_length or len(input_name) > name_max_length:
        if len(input_name) < name_min_length:
            print("Too short!")
        if len(input_name) > name_max_length:
            print("Too long!")
        greet_someone()
        dont_print = True

    # This check prevents repeating an empty print
    if not dont_print:
        print("Have a great day {}!".format(input_name))


greet_someone()

# I am clearly an incredible python programmer
